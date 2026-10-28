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
