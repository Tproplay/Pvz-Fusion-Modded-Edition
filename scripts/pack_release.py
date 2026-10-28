"""
Release Packaging Script for Plants vs. Zombies Fusion Modded Edition.
Creates distribution ZIP archives using standard Python libraries.

Supports packaging:
  1. Full Game Standalone (PvZ_Fusion_4.0.5_Modded_Full_v4.0.5.zip)
  2. Mods & Framework Addon (PvZ_Fusion_4.0.5_Mods_Only_v4.0.5.zip)
  3. Modular Multi-Part Packs (Part00 through Part08)
"""

import argparse
import hashlib
import os
import shutil
import sys
import zipfile
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
PACKED_DIR = ROOT_DIR / "PvZ Fusion 4.0.5 Modded (Packed)"
DIST_DIR = ROOT_DIR / "dist"
MODULAR_DIR = DIST_DIR / "modular"
VERSION = "v4.0.5"


def compute_sha256(filepath: Path) -> str:
    sha = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(1024 * 1024):
            sha.update(chunk)
    return sha.hexdigest()


def zip_directory_contents(source_dir: Path, zip_file: zipfile.ZipFile, base_arc: str = ""):
    for root, _, files in os.walk(source_dir):
        for f in files:
            full_path = Path(root) / f
            rel_path = full_path.relative_to(source_dir)
            arc_name = str(Path(base_arc) / rel_path).replace("\\", "/")
            zip_file.write(full_path, arc_name)


def pack_full():
    print(f"\n[1/3] Packaging Standalone Full Game...")
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    out_zip = DIST_DIR / f"PvZ_Fusion_4.0.5_Modded_Full_{VERSION}.zip"
    if out_zip.exists():
        out_zip.unlink()

    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        zip_directory_contents(PACKED_DIR, zf)

    size_mb = out_zip.stat().st_size / (1024 * 1024)
    print(f"  [OK] Created {out_zip.name} ({size_mb:.2f} MB)")
    print(f"  SHA-256: {compute_sha256(out_zip)}")


def pack_mods_only():
    print(f"\n[2/3] Packaging Mods and Framework Addon...")
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    out_zip = DIST_DIR / f"PvZ_Fusion_4.0.5_Mods_Only_{VERSION}.zip"
    if out_zip.exists():
        out_zip.unlink()

    installer = ROOT_DIR / "BepInExInstall.exe"
    memory_aob = PACKED_DIR / "MemoryAOB.dll"

    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        if installer.exists():
            zf.write(installer, "BepInExInstall.exe")
        if memory_aob.exists():
            zf.write(memory_aob, "MemoryAOB.dll")

        # Include SkinLoader
        skinloader = PACKED_DIR / "SkinLoader"
        if skinloader.exists():
            zip_directory_contents(skinloader, zf, "SkinLoader")

        # Include BepInEx components
        bepinex_src = PACKED_DIR / "BepInEx"
        for sub in ["config", "patchers", "core", "Mods - HengMing", "plugins"]:
            sub_path = bepinex_src / sub
            if sub_path.exists():
                zip_directory_contents(sub_path, zf, f"BepInEx/{sub}")

    size_mb = out_zip.stat().st_size / (1024 * 1024)
    print(f"  [OK] Created {out_zip.name} ({size_mb:.2f} MB)")
    print(f"  SHA-256: {compute_sha256(out_zip)}")


def pack_modular():
    print(f"\n[3/3] Packaging Modular Multi-Part Packs...")
    MODULAR_DIR.mkdir(parents=True, exist_ok=True)

    plugins_dir = PACKED_DIR / "BepInEx" / "plugins"
    bepinex_dir = PACKED_DIR / "BepInEx"
    installer = ROOT_DIR / "BepInExInstall.exe"
    memory_aob = PACKED_DIR / "MemoryAOB.dll"

    # Part 00: Prerequisites & Core
    p00_zip = MODULAR_DIR / "Part00_Prerequisites_And_Core.zip"
    with zipfile.ZipFile(p00_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        if installer.exists():
            zf.write(installer, "BepInExInstall.exe")
        if memory_aob.exists():
            zf.write(memory_aob, "MemoryAOB.dll")
        for sub in ["core", "patchers", "config"]:
            p = bepinex_dir / sub
            if p.exists():
                zip_directory_contents(p, zf, f"BepInEx/{sub}")
        # Core plugins
        for f in plugins_dir.glob("*.dll"):
            zf.write(f, f"BepInEx/plugins/{f.name}")
        for folder in ["res", "XUnity.AutoTranslator", "Magnetar Data", "Magnetar Translation"]:
            p = plugins_dir / folder
            if p.exists():
                zip_directory_contents(p, zf, f"BepInEx/plugins/{folder}")
    print(f"  [OK] Created {p00_zip.name}")

    # Parts 01-07: Author Packs
    pack_map = {
        "Part01_Wuxuan_Mengxi_Pack.zip": ["Mods - Wuxuan Mengxi"],
        "Part02_Ultimate_Plant_Pack.zip": ["Mods - Ultimate Plant Pack"],
        "Part03_Inf75_Pack.zip": ["Mods - Inf75"],
        "Part04_HengMing_Pack.zip": ["Mods - HengMing"],
        "Part05_Salmon_Pack.zip": ["Mods - Salmon"],
        "Part06_Community_Packs.zip": ["Mods - Community", "Mods - Murong Guqing", "Mods - LikeFengzi", "Mods - Ttpersik"],
        "Part07_Tproplay_Tools.zip": ["Mods - Tproplay"],
    }

    for zip_name, mod_folders in pack_map.items():
        out_p = MODULAR_DIR / zip_name
        with zipfile.ZipFile(out_p, "w", zipfile.ZIP_DEFLATED) as zf:
            for mf in mod_folders:
                folder_p = plugins_dir / mf
                if folder_p.exists():
                    zip_directory_contents(folder_p, zf, f"BepInEx/plugins/{mf}")
            # HengMing also includes BepInEx/Mods - HengMing
            if "Mods - HengMing" in mod_folders:
                hm_root = bepinex_dir / "Mods - HengMing"
                if hm_root.exists():
                    zip_directory_contents(hm_root, zf, "BepInEx/Mods - HengMing")
        print(f"  [OK] Created {out_p.name}")

    # Part 08: Skin Packs
    p08_zip = MODULAR_DIR / "Part08_Skin_Packs.zip"
    with zipfile.ZipFile(p08_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        skinloader = PACKED_DIR / "SkinLoader"
        if skinloader.exists():
            zip_directory_contents(skinloader, zf, "SkinLoader")
        for skin_f in ["skin", "MoreGloves", "MoreShovels"]:
            p = plugins_dir / skin_f
            if p.exists():
                zip_directory_contents(p, zf, f"BepInEx/plugins/{skin_f}")
    print(f"  [OK] Created {p08_zip.name}")


def main():
    parser = argparse.ArgumentParser(description="Package PvZ Fusion Modded Edition releases.")
    parser.add_argument("--full", action="store_true", help="Build standalone full game zip")
    parser.add_argument("--mods", action="store_true", help="Build mods only addon zip")
    parser.add_argument("--modular", action="store_true", help="Build modular multi-part zips")
    parser.add_argument("--all", action="store_true", help="Build all packages")
    args = parser.parse_args()

    if not any([args.full, args.mods, args.modular, args.all]):
        parser.print_help()
        sys.exit(0)

    if args.all or args.full:
        pack_full()
    if args.all or args.mods:
        pack_mods_only()
    if args.all or args.modular:
        pack_modular()

    print("\n[DONE] Packaging complete.")


if __name__ == "__main__":
    main()
