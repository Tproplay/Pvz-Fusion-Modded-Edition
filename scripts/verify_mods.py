"""
Verification script for PvZ Fusion Modded Edition builds.
Scans the game directories to verify all mod author folders, required framework DLLs,
configurations, and skin assets.
"""

import os
import sys
from pathlib import Path


EXPECTED_MOD_DIRS = [
    "Mods - Ultimate Plant Pack",
    "Mods - Wuxuan Mengxi",
    "Mods - Inf75",
    "Mods - HengMing",
    "Mods - Salmon",
    "Mods - Community",
    "Mods - Murong Guqing",
    "Mods - LikeFengzi",
    "Mods - Ttpersik",
    "Mods - Tproplay",
]

CORE_FRAMEWORK_PLUGINS = [
    "CustomizeLib.BepInEx.dll",
    "MengxiLib.BepInEx.dll",
    "SkinLoader.dll",
    "AudioImportLib.BepInEx.dll",
    "AlmanacAdaptiveSliders.dll",
    "Fusion.Android.Compatibility.dll",
    "MemoryAOB.dll",
    "RHByteFiddler.dll",
    "DiscordRPC.dll",
]


def verify_build(build_path_str: str) -> bool:
    build_path = Path(build_path_str)
    print(f"\n==================================================")
    print(f"Verifying build: {build_path.name}")
    print(f"==================================================")

    if not build_path.exists():
        print(f"  [ERROR] Directory not found: {build_path}")
        return False

    all_passed = True

    # 1. Check Root Executable and Core Libraries
    game_exe = build_path / "PlantsVsZombiesRH.exe"
    memory_aob = build_path / "MemoryAOB.dll"
    bepinex_dir = build_path / "BepInEx"

    if game_exe.exists():
        print("  [OK] Game executable found (PlantsVsZombiesRH.exe)")
    else:
        print("  [ERROR] Missing PlantsVsZombiesRH.exe")
        all_passed = False

    if memory_aob.exists():
        print("  [OK] MemoryAOB.dll found in root")
    else:
        print("  [ERROR] Missing MemoryAOB.dll in root")
        all_passed = False

    # 2. Check BepInEx and Core Configuration
    bepinex_cfg = bepinex_dir / "config" / "BepInEx.cfg"
    if bepinex_cfg.exists():
        cfg_text = bepinex_cfg.read_text(encoding="utf-8", errors="ignore")
        if "[Logging.Console]" in cfg_text and "Enabled = true" in cfg_text:
            print("  [OK] BepInEx.cfg has Console logging enabled (prevents IOException handle crash)")
        else:
            print("  [WARNING] BepInEx.cfg console logging might be disabled")
    else:
        print("  [ERROR] Missing BepInEx.cfg")
        all_passed = False

    # 3. Check Core Framework Plugins
    plugins_dir = bepinex_dir / "plugins"
    if not plugins_dir.exists():
        print(f"  [ERROR] Missing plugins directory: {plugins_dir}")
        return False

    missing_core = []
    for dll in CORE_FRAMEWORK_PLUGINS:
        if not (plugins_dir / dll).exists():
            missing_core.append(dll)

    if not missing_core:
        print(f"  [OK] All {len(CORE_FRAMEWORK_PLUGINS)} core framework DLLs present in plugins root")
    else:
        print(f"  [ERROR] Missing core DLLs in plugins: {missing_core}")
        all_passed = False

    # 4. Check Categorized Mod Directories
    total_mods = 0
    print("\n  Categorized Mod Folders:")
    for mod_dir_name in EXPECTED_MOD_DIRS:
        mod_dir = plugins_dir / mod_dir_name
        if mod_dir.exists() and mod_dir.is_dir():
            dlls = list(mod_dir.glob("*.dll"))
            count = len(dlls)
            total_mods += count
            print(f"    - {mod_dir_name:<30}: {count:>3} DLLs")
        else:
            print(f"    - {mod_dir_name:<30}: [MISSING]")
            all_passed = False

    # Also count HengMing mods in BepInEx/Mods - HengMing
    hengming_root_mods = bepinex_dir / "Mods - HengMing"
    if hengming_root_mods.exists():
        hm_count = len(list(hengming_root_mods.glob("*.dll")))
        total_mods += hm_count
        print(f"    - {'BepInEx/Mods - HengMing':<30}: {hm_count:>3} DLLs")

    print(f"\n  [INFO] Total active mod DLLs: {total_mods}")

    # 5. Check SkinLoader & Skins
    skinloader_dir = build_path / "SkinLoader"
    plugins_skin = plugins_dir / "skin"
    if skinloader_dir.exists():
        subdirs = [d for d in skinloader_dir.iterdir() if d.is_dir()]
        print(f"  [OK] SkinLoader directory present ({len(subdirs)} custom plant skin directories)")
    else:
        print("  [WARNING] SkinLoader directory missing")

    if plugins_skin.exists():
        print("  [OK] plugins/skin directory present")

    if all_passed:
        print("\n  >>> BUILD VERIFICATION SUCCESSFUL <<<")
    else:
        print("\n  >>> BUILD VERIFICATION HAD ERRORS <<<")

    return all_passed


def main():
    root = Path(__file__).resolve().parent.parent
    packed = root / "PvZ Fusion 4.0.5 Modded (Packed)"
    testing = root / "PvZ Fusion 4.0.5 Modded (Testing)"

    success = True
    if packed.exists():
        if not verify_build(str(packed)):
            success = False
    else:
        print(f"Packed build not found at: {packed}")

    if testing.exists():
        if not verify_build(str(testing)):
            success = False

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
