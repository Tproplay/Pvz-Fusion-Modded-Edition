# PvZ Fusion Modded Edition - Patch & Maintenance Notes

## Build Fixes & Error Resolutions

### 1. ID Dumper Removal
- Removed `BepInEx/plugins/PlantIdLogger.dll` and `BepInEx/plugins/PlantIdLogger/` (~18.6 MB text dumps) from both `Packed` and `Testing` builds.
- Prevents redundant disk I/O and spam logging of IDs on every game frame/load.

### 2. Google Drive Integration
- Connected to Google Drive via `gdrive` CLI (`cl/999922155`).
- Successfully verified authentication and read access; no files uploaded.

### 3. CustomizeLib NullReference / Property Set Fix
- **Error**: `Exception: System.ArgumentException: Property set method not found. at CustomizeLib.BepInEx.Patch.UIMgrPatch.TryRegisterTypeMgrSet`
- **Impact**: Caused `UIMgr.PostEnterMainMenu()` to crash before dispatching `CorePlugin.OnGameInitAction`, causing a cascading `NullReferenceException` in `CustomMenu_page3.AddCard`.
- **Fix**: Patched offset `0x12337` in `CustomizeLib.BepInEx.dll` replacing the illegal `property.SetValue(null, hashSet)` call with NOPs, since `TypeMgr.RedPlant` and `TypeMgr.UncrashablePlants` are getter-only in PvZ Fusion 4.0.5 and elements are already added in-place.

### 4. MengxiLib SkinLoader Coroutine Crash Fix
- **Error**: `Exception in IL2CPP-to-Managed trampoline: System.NullReferenceException at MengxiLib.BepInEx.Extensions.TryGetAsset[T](AssetBundle ab, String name, T& obj)`
- **Impact**: Aborted skin registration during `GameAPP.StartCoroutine(PatchMgr.RegisterSkin())`.
- **Fix**: Injected `ab != null` null check into `MengxiLib.BepInEx.Extensions.TryGetAsset` via dnlib to gracefully return `false` on missing or unreadable asset bundles instead of crashing the coroutine.

### 5. Missing Dependency Resolution (`GodMaliang.dll`)
- **Error**: `Could not load [神马良 1.0.0] because it has missing dependencies: com.pvzrh.launcher.ui`
- **Fix**: Removed `GodMaliang.dll` since the external launcher UI dependency is not present in the distribution.

### 6. SkinLoader Asset & Mod De-duplication
- Removed duplicate and corrupt skin files in `SkinLoader/`:
  - `SkinLoader/925/ObsidianPotatoNut_1`
  - `SkinLoader/930/SuperDoomScaredy_1` & `SuperDoomScaredy_2`
  - `SkinLoader/930(2)/`
  - `SkinLoader/931/ObsidianWallNut`
  - `SkinLoader/939/UltimateGatlingBlover_1`
- Removed duplicate `Compound+Z.dll` (identical hash to `Compound Z.dll`).

### 7. Removed IllustrationPlacement Mod
- Removed `BepInEx/plugins/IllustrationPlacement.dll` and its config `BepInEx/config/com.illustrationplacement.bepinex.cfg` from both `Packed` and `Testing` builds.

### 8. Installed Magnetar Client & Simple Spawner
- Downloaded `MagnetarClient-4.0.2-Bepinex.zip` from Google Drive (`19W-gSM7iMensOkqVbJdGm_crsCjbyv2X`).
- Deployed Magnetar Client into both builds:
  - `BepInEx/plugins/Mods - Tproplay/Magnetar Client.dll`
  - `BepInEx/plugins/DiscordRPC.dll`
  - `BepInEx/plugins/Magnetar Data/`
  - `BepInEx/plugins/Magnetar Translation/`
  - Verified `Newtonsoft.Json.dll` in `BepInEx/core/`.
  - Configs: `Magnetar_Client.cfg`, `Magnetar_bangbay.json`, `Magnetar_Default.json`.
- Deployed Simple Spawner:
  - `BepInEx/plugins/Mods - Tproplay/SimpleSpawner.Bepinex.dll`
  - Config: `BepInEx/config/com.tproplay.simplespawner.cfg` in both builds.

### 9. Grouped Mods by Authors & Packs
- Reorganized all 400+ plugin DLLs from a flat list into categorized author directories in both `Packed` and `Testing` builds:
  - `Mods - Ultimate Plant Pack` (105 DLLs): Divine/cosmic fusion series (`AstralGodCabbage`, `BloodMoonPhantomCabbage`, `DisillusionmentLaserPumpkin`, `UltimateSaintSeiyaCabbage`, `UltimateNineGirls`, etc.).
  - `Mods - Wuxuan Mengxi` (99 DLLs): Plant mods authored, co-authored, or adapted by 梧萱梦汐X (`BambooWoodMortar`, `BonkChoy2`, `ButterGloom`, `CherryFume`, `CoffeeBean`, etc.).
  - `Mods - Inf75` (58 DLLs): Complete collection of `inf75.*` mods (`BigDoomGatling`, `SuperDiamondNut`, `SuperDoomSqualour`, `WaterPot`, etc.).
  - `Mods - HengMing` (50 DLLs): Complete collection of HengMing's creations including `HengMingModsLib`, `StarUpDoomSniper`, `MagnetDoomBlover`, `Menu`, `ShootingMODGeneralLib`, and the `RogueShooting-*` series.
  - `Mods - Salmon` (49 DLLs): Complete collection of `salmon.*` mods (`BetterSuperMachine`, `Puff*SuperGatling`, `UltimateDoomMinigun`, `UltimateWinterMelon`, etc.).
  - `Mods - Community` (28 DLLs): Independent community mods (`Cassidy`, `Xingchen`, `Deqing`, `Soviet`, `EnchantingTable`, etc.).
  - `Mods - Murong Guqing` (19 DLLs): Mods created by 慕容孤晴 (`SuperMachine*` nut series, etc.).
  - `Mods - LikeFengzi` (10 DLLs): Mods created by 理科疯子 (`CherryHypnoGatlingBlover`, `HypnoDoomEmperor`, etc.).
  - `Mods - Ttpersik` (3 DLLs): Mods created by Ttpersik (`BigPortalGatling`, `SuperFireGatling`, `SuperObsidianGatling`).
  - `Mods - Tproplay` (2 DLLs): `Magnetar Client.dll` and `SimpleSpawner.Bepinex.dll`.
  - Kept critical shared framework libraries and resource folders at `BepInEx/plugins/` root: `CustomizeLib.BepInEx.dll`, `MengxiLib.BepInEx.dll`, `SkinLoader.dll`, `AudioImportLib.BepInEx.dll`, `AlmanacAdaptiveSliders.dll`, `Fusion.Android.Compatibility.dll`, `MemoryAOB.dll`, `DiscordRPC.dll`, `res/`, `skin/`, `MoreGloves/`, `MoreShovels/`, and translation folders.

### 10. RHByteFiddler Patcher & MemoryAOB Placement Fix
- **Error**: `RHByteFiddler警告: 未检测到以下必要文件: RHByteFiddler.dll` and `System.DllNotFoundException: Unable to load DLL 'MemoryAOB.dll'`.
- **Root Cause**: `BepInEx/patchers/Patcher_RHByteFiddler.dll` explicitly checks for `BepInEx/plugins/RHByteFiddler.dll` at the root of `plugins/`. When grouped into a subfolder, the preloader check failed. In addition, `RHByteFiddler.dll` P/Invokes `MemoryAOB.dll`, which Windows resolves from the application root or plugins directory.
- **Fix**:
  - Restored `RHByteFiddler.dll` to `BepInEx/plugins/` root in both Packed and Testing builds.
  - Placed `MemoryAOB.dll` in both `BepInEx/plugins/` and the game root directory.
  - Placed `HengMingModsLib.dll` in `BepInEx/plugins/` root to satisfy `HengMingModsLib.Preloader.dll`.

### 11. Magnetar Client Config Cleanup
- Removed `Magnetar_Client.cfg`, `Magnetar_bangbay.json`, and `Magnetar_Default.json` from `BepInEx/config/` across both release (`Packed`) and testing builds.

### 12. Suppressed HengMing Reminder UI & Side Sliding Menu
- **Target UI Elements**:
  - In-game sliding side menu ("Warm reminder from Heng Ming" / "创作者名单" with side tab `create make who`).
  - Loading screen popup reminder ("恒暝的温馨提示").
- **Root Cause**:
  - `HengMingModsLib.dll` -> `HengMingModsLib.LoadUI.Widgets.KindReminderPostLoad::Build()` creates `KindReminderPostLoadCanvas`, sliding panel UI, button triggers, and a frame driver component (`KindReminderPostLoad/Driver`) that polled mouse position and transform lerping every frame.
  - `HengMingModsLib.LoadUI.Widgets.KindReminder::Build()` creates the loading screen reminder canvas and text.
- **Fix**:
  - Patched `HengMingModsLib.dll` in both `Packed` and `Testing` builds using `dnlib`:
    - `KindReminderPostLoad::Build()`, `DriverTick()`, `Toggle()`, `ShowFromSide()`, and `HideToSide()` bodies replaced with single `ret` instructions.
    - `KindReminder::Build()` and `Tick()` bodies replaced with single `ret` instructions.
  - Completely eliminates creation of the side panel, tab button, and their per-frame CPU tick overhead without breaking mod loading.

### 13. Mod Pack Size & Performance Optimization
- **Duplicate HengMing Binaries Cleaned**:
  - `BepInEx/plugins/Mods - HengMing` contained full 54 MB copies of the 36 HengMing plant DLLs that were already present in `BepInEx/Mods - HengMing`.
  - Converted `BepInEx/plugins/Mods - HengMing` DLLs to 0-byte placeholders as designed by `HengMingModsLib.Preloader.SyncPlaceholderDlls`.
  - Re-routed non-HengMing DLLs (`RogueShooting-*`, `ShootingMODGeneralLib.dll`) to `Mods - Salmon` and `MagnetDoomBlover.dll`, `Menu.dll`, `StarUpDoomSniper.dll` to `Mods - Community`.
  - Reduced total package footprint below 2 GB (freed ~114 MB across both builds).
- **BepInEx Performance Configuration**:
  - `[Logging.Disk] InstantFlushing = false`: Disabled instant disk flushing during frame loops.

### 14. Fixed Mod Loading Failure (`IOException: The handle is invalid`)
- **Error**: Dozens of mods failed to load with `System.IO.IOException: The handle is invalid. at System.ConsolePal.SetConsoleOutputEncoding(Encoding enc) at System.Console.set_OutputEncoding(Encoding value)` during `Chainloader.LoadPlugin()`.
- **Root Cause**: Many precompiled mod DLLs (`Patcher_RHByteFiddler`, `HengMingModsLib`, `ArmyCactus`, `BigFireGatling`, etc.) explicitly call `Console.OutputEncoding = Encoding.UTF8` during initialization. In .NET 6 (Windows GUI process), when `[Logging.Console] Enabled = false`, no console handle exists (`INVALID_HANDLE_VALUE`), causing `SetConsoleOutputCP` to throw an unhandled `IOException`, crashing mod initialization and breaking cascading dependencies (including Almanac plant menus).
- **Fix**: Restored `[Logging.Console] Enabled = true` and `[IL2CPP] UpdateInteropAssemblies = true` in `BepInEx/config/BepInEx.cfg` across both `Packed` and `Testing` builds, providing valid handles and restoring proper plugin loading.


