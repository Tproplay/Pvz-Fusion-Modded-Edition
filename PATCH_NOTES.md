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
