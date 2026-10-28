# PvZ Fusion Modded Edition - Release Plan and Distribution

## 1. Overview and Distribution Strategy

| Release Package | Distribution Channels | Target Size (Est. Zip) | Description |
| :--- | :--- | :--- | :--- |
| **Package 1: Full Game (Standalone)** | **GitHub Releases** + **Google Drive** | ~1.82 GB uncompressed / ~1.15 GB zip | Complete game + BepInEx 6 + .NET 6 + all 400+ mods + bugfixes. Zero setup: Extract and Play. |
| **Package 2: Mods and Framework (Addon)** | **GitHub Releases** + **Google Drive** | ~1.32 GB uncompressed / ~750 MB zip | For existing clean PvZ Fusion 4.0.5 installs. Includes BepInExInstall.exe, custom Il2CppInterop, all 400+ mods, configs, and skins. |
| **Package 3: Modular Multi-Part Packs** | **Google Drive ONLY** | 9 parts (~1 MB to ~300 MB each) | Modular downloads for bandwidth constraints or custom loadouts (Core framework + individual author packs). |

---

## 2. Release Metadata and Release Notes

### Tag and Title
- **Tag**: v4.0.5
- **Release Title**: Plants vs. Zombies Fusion Modded Edition v4.0.5

### Release Notes (GitHub and Drive Description)
```markdown
# Plants vs. Zombies Fusion Modded Edition (English Version) - Release v4.0.5

Welcome to the ultimate modded edition for Plants vs. Zombies: Fusion 4.0.5 (English Version).
Featuring 400+ community fusion plants, zombies, tools, and enhancements, organized by author and pre-patched for stability and peak performance.

### Highlights and Included Features:
- Over 400+ Mods Categorized by Author:
  - Ultimate Plant Pack (105 mods): Cosmic, divine, and celestial fusion plants.
  - Wuxuan Mengxi (99 mods): Complete plant series by Wuxuan Mengxi.
  - Inf75 (58 mods): Full inf75 fusion plant and zombie series.
  - HengMing Series (36 plant mods and library): Neutralized side tabs and popups.
  - Salmon Series (49 mods): SalmonCN plants and the complete RogueShooting series.
  - Community and Collaborations (60 mods): Murong Guqing, LikeFengzi, Ttpersik, Cassidy, Xingchen, Deqing, Soviet, and more.
  - Tproplay Utilities: Magnetar Client (game speed control, debug menus, cheat toggles) and Simple Spawner.
- Critical Stability and Bug Fixes Pre-Applied:
  - CustomizeLib getter-only property crash fixed.
  - MengxiLib SkinLoader AssetBundle null-reference coroutine crash fixed.
  - RHByteFiddler preloader detection and MemoryAOB.dll placement fixed.
  - HengMing side sliding menu and startup popup silenced at the IL level.
  - BepInEx console encoding handle issue resolved for reliable mod loading.
  - 114 MB of duplicate binaries removed.
- English Translation and UI Fixes:
  - Pre-installed XUnity.AutoTranslator and adaptive almanac sliders.

---

### Download Packages Available Here:
1. Standalone Full Game (PvZ_Fusion_4.0.5_Modded_Full_v4.0.5.zip): Extract and play immediately (zero setup required).
2. Mods and Framework Addon (PvZ_Fusion_4.0.5_Mods_Only_v4.0.5.zip): For existing clean installs of PvZ Fusion 4.0.5. Includes BepInExInstall.exe, custom Il2CppInterop binaries, all 400+ mods, configs, and skins.

(Note: For modular part-by-part downloads, check our official Google Drive mirror).
```

---

## 3. Package File Structures

### Package 1: Full Game (PvZ_Fusion_4.0.5_Modded_Full_v4.0.5.zip)
- Distribution: GitHub Release + Google Drive
- Directory Layout:
  - PlantsVsZombiesRH.exe
  - UnityPlayer.dll
  - UnityCrashHandler64.exe
  - GameAssembly.dll
  - MemoryAOB.dll
  - doorstop_config.ini
  - README_START.txt
  - PlantsVsZombiesRH_Data/
  - dotnet/
  - SkinLoader/
  - BepInEx/
    - config/
    - core/
    - interop/
    - patchers/
    - Mods - HengMing/
    - plugins/
      - Mods - Ultimate Plant Pack/
      - Mods - Wuxuan Mengxi/
      - Mods - Inf75/
      - Mods - HengMing/
      - Mods - Salmon/
      - Mods - Community/
      - Mods - Murong Guqing/
      - Mods - LikeFengzi/
      - Mods - Ttpersik/
      - Mods - Tproplay/
      - skin/
      - res/
      - XUnity.AutoTranslator/
      - [Core helper DLLs and resources]

### Package 2: Mods and Framework Addon (PvZ_Fusion_4.0.5_Mods_Only_v4.0.5.zip)
- Distribution: GitHub Release + Google Drive
- Directory Layout:
  - BepInExInstall.exe (Automated installer tool)
  - MemoryAOB.dll (To place alongside game exe)
  - README_INSTALL.txt (Step-by-step instructions)
  - SkinLoader/ (Custom plant and zombie skins)
  - BepInEx/
    - config/ (Preconfigured BepInEx and mod settings)
    - patchers/ (Patcher_RHByteFiddler.dll, HengMingModsLib.Preloader.dll)
    - core/ (Custom Il2CppInterop.Common.dll, Runtime.dll, etc.)
    - Mods - HengMing/ (36 HengMing plant mods)
    - plugins/ (All 10 author mod directories and assets)

### Package 3: Modular Multi-Part Packs (Google Drive Only)
- Part00_Prerequisites_And_Core.zip (~4.86 MB)
  - BepInExInstall.exe
  - MemoryAOB.dll
  - README_MODULAR.txt
  - BepInEx/core/ (Custom Il2CppInterop.Common.dll and Runtime.dll)
  - BepInEx/patchers/
  - BepInEx/config/
  - BepInEx/plugins/ (CustomizeLib, MengxiLib, SkinLoader, DiscordRPC, AutoTranslator, etc.)
- Part01_Wuxuan_Mengxi_Pack.zip (~490 MB raw: 99 mods)
- Part02_Ultimate_Plant_Pack.zip (~205 MB raw: 105 mods)
- Part03_Inf75_Pack.zip (~163 MB raw: 58 mods)
- Part04_HengMing_Pack.zip (~55 MB raw: 36 mods + Lib)
- Part05_Salmon_Pack.zip (~77 MB raw: 49 mods + RogueShooting)
- Part06_Community_Packs.zip (~155 MB raw: Community, Murong, LikeFengzi, Ttpersik)
- Part07_Tproplay_Tools.zip (~1.28 MB raw: Magnetar Client and Simple Spawner)
- Part08_Skin_Packs.zip (~175 MB raw: plugins/skin and SkinLoader)

---

## 4. Google Drive Hierarchy

- Pvz Fusion Modded Edition/
  - v4.0.5/
    - 1. Full Game (Standalone)/
      - PvZ_Fusion_4.0.5_Modded_Full_v4.0.5.zip
    - 2. Mods Only (Addon)/
      - PvZ_Fusion_4.0.5_Mods_Only_v4.0.5.zip
    - 3. Modular Multi-Part Packs/
      - README_MODULAR.txt
      - Part00_Prerequisites_And_Core.zip
      - Part01_Wuxuan_Mengxi_Pack.zip
      - Part02_Ultimate_Plant_Pack.zip
      - Part03_Inf75_Pack.zip
      - Part04_HengMing_Pack.zip
      - Part05_Salmon_Pack.zip
      - Part06_Community_Packs.zip
      - Part07_Tproplay_Tools.zip
      - Part08_Skin_Packs.zip
