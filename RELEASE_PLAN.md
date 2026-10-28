# PvZ Fusion Modded Edition - Release Plan & Distribution Draft

## 1. Overview & Distribution Strategy

| Release Package | Distribution Channels | Target Size (Est. Zip) | Description |
| :--- | :--- | :--- | :--- |
| **Package 1: Full Game (Standalone)** | **GitHub Releases** + **Google Drive** | ~1.15 GB (~1.98 GB uncompressed) | Complete game + BepInEx 6 + .NET 6 + all 400+ mods + bugfixes. Zero setup: Extract & Play. |
| **Package 2: Mods & Framework (Addon)** | **GitHub Releases** + **Google Drive** | ~750 MB (~1.34 GB uncompressed) | For existing clean PvZ Fusion 4.0.5 installs. Includes `BepInExInstall.exe`, custom `Il2CppInterop`, all 400+ mods, configs, and skins. |
| **Package 3: Modular Multi-Part Packs** | **Google Drive ONLY** | 9 parts (~25 MB to ~300 MB each) | Modular downloads for bandwidth constraints or custom loadouts (Core framework + individual author packs). |

---

## 2. Release Draft Metadata & Release Notes

### Tag & Title
- **Tag**: `v1.0.0-fusion-4.0.5`
- **Release Title**: `Plants vs. Zombies Fusion Modded Edition (Eng Ver.) v1.0.0`

### Proposed Release Notes (GitHub & Drive Description)
```markdown
# Plants vs. Zombies Fusion Modded Edition - Release v1.0.0 (PvZ Fusion 4.0.5)

Welcome to the all-in-one Modded Edition for **Plants vs. Zombies: Fusion 4.0.5 (English Version)**!
Featuring **400+ community fusion plants, zombies, tools, and visual enhancements**, fully organized, optimized, and patched for stability and performance.

### ✨ What's Included:
- **400+ Mods Fully Organized**:
  - 🌟 **Ultimate Plant Pack** (105 mods): Cosmic, divine, and celestial fusion plants.
  - 🌸 **Wuxuan Mengxi** (99 mods): Complete plant collection by 梧萱梦汐X.
  - 💥 **Inf75** (58 mods): Full `inf75` fusion roster.
  - 🍃 **HengMing Series** (36 plant mods + library): Cleaned of intrusive side tabs & popups.
  - 🐟 **Salmon Series** (49 mods): SalmonCN plants + full RogueShooting series.
  - 🤝 **Community & Collaborations** (60 mods): Murong Guqing, LikeFengzi, Ttpersik, Cassidy, Xingchen, Deqing, Soviet, and more.
  - 🛠️ **Tproplay Utilities**: Built-in **Magnetar Client** (game speed, mod menu, debug tools) & **Simple Spawner**.
- **Critical Crash Fixes Pre-Applied**:
  - `CustomizeLib` getter-only property crash fixed.
  - `MengxiLib` SkinLoader AssetBundle null-reference coroutine crash fixed.
  - `RHByteFiddler` and `MemoryAOB.dll` preloader placement fixed.
  - HengMing side sliding menu and loading popup neutralized.
  - Duplicate assembly footprint purged (saved >110 MB).
- **Full English Translation & Adaptive Almanac UI**:
  - Pre-installed `XUnity.AutoTranslator` & adaptive sliders.

---

### 📦 Download Options:

1. **Standalone Full Game (`PvZ_Fusion_4.0.5_Modded_Full_v1.0.0.zip`)**
   - Ideal for players who want to jump straight in with no setup.
   - Extract anywhere and run `PlantsVsZombiesRH.exe`.

2. **Mods & Framework Addon (`PvZ_Fusion_4.0.5_Mods_Only_v1.0.0.zip`)**
   - For players who already have a clean install of PvZ Fusion 4.0.5.
   - Includes `BepInExInstall.exe`, custom `Il2CppInterop` binaries, all 400+ mods, configs, and skins.
   - Follow the included `README_INSTALL.txt`.

3. **Modular Parts (Available on Google Drive)**
   - For selective downloads or slower internet connections.
   - Install `Part00_Prerequisites_And_Core.zip` first, then add any chosen author packs.
```

---

## 3. Package File Structures

### Package 1: Full Game (`PvZ_Fusion_4.0.5_Modded_Full_v1.0.0.zip`)
```
PvZ Fusion 4.0.5 Modded Edition/
├── PlantsVsZombiesRH.exe
├── UnityPlayer.dll
├── UnityCrashHandler64.exe
├── GameAssembly.dll
├── MemoryAOB.dll
├── doorstop_config.ini
├── README_START.txt
├── PlantsVsZombiesRH_Data/
├── dotnet/
├── SkinLoader/
└── BepInEx/
    ├── config/
    ├── core/
    ├── interop/
    ├── patchers/
    ├── Mods - HengMing/
    └── plugins/
        ├── Mods - Ultimate Plant Pack/
        ├── Mods - Wuxuan Mengxi/
        ├── Mods - Inf75/
        ├── Mods - HengMing/
        ├── Mods - Salmon/
        ├── Mods - Community/
        ├── Mods - Murong Guqing/
        ├── Mods - LikeFengzi/
        ├── Mods - Ttpersik/
        ├── Mods - Tproplay/
        ├── skin/
        ├── res/
        ├── XUnity.AutoTranslator/
        └── [Core helper DLLs & resources]
```

### Package 2: Mods & Framework Addon (`PvZ_Fusion_4.0.5_Mods_Only_v1.0.0.zip`)
```
PvZ_Fusion_4.0.5_Mods_Only/
├── BepInExInstall.exe              <-- Automated installer tool
├── MemoryAOB.dll                   <-- To place alongside game exe
├── README_INSTALL.txt              <-- Step-by-step instructions
├── SkinLoader/                     <-- Custom plant/zombie skins
└── BepInEx/
    ├── config/                     <-- Preconfigured BepInEx & mod settings
    ├── patchers/                   <-- Patcher_RHByteFiddler.dll, HengMingModsLib.Preloader.dll
    ├── core/                       <-- Custom Il2CppInterop.Common.dll, Runtime.dll, etc.
    ├── Mods - HengMing/            <-- 36 HengMing plant mods
    └── plugins/                    <-- All 10 author mod directories & assets
```

### Package 3: Modular Multi-Part Packs (Google Drive Only)
```
Modular_Packs/
├── Part00_Prerequisites_And_Core.zip (~25 MB)
│   ├── BepInExInstall.exe
│   ├── MemoryAOB.dll
│   ├── README_MODULAR.txt
│   └── BepInEx/
│       ├── core/ (Custom Il2CppInterop.Common.dll & Runtime.dll)
│       ├── patchers/
│       ├── config/
│       └── plugins/ (CustomizeLib, MengxiLib, SkinLoader, DiscordRPC, AutoTranslator, etc.)
├── Part01_Wuxuan_Mengxi_Pack.zip      (~300 MB zip / 491 MB raw: 99 mods)
├── Part02_Ultimate_Plant_Pack.zip     (~130 MB zip / 208 MB raw: 105 mods)
├── Part03_Inf75_Pack.zip              (~100 MB zip / 164 MB raw: 58 mods)
├── Part04_HengMing_Pack.zip           (~35 MB zip / 55 MB raw: 36 mods + Lib)
├── Part05_Salmon_Pack.zip             (~45 MB zip / 78 MB raw: 49 mods + RogueShooting)
├── Part06_Community_Packs.zip         (~95 MB zip / 156 MB raw: Community, Murong, LikeFengzi, Ttpersik)
├── Part07_Tproplay_Tools.zip          (~1 MB zip / 2 MB raw: Magnetar Client & Simple Spawner)
└── Part08_Skin_Packs.zip              (~110 MB zip / 175 MB raw: plugins/skin & SkinLoader)
```

---

## 4. Draft README Instructions

### `README_INSTALL.txt` (For Package 2 - Mods Only)
```
================================================================================
  Plants vs. Zombies: Fusion 4.0.5 Modded Edition - Mods Installation Guide
================================================================================

PREREQUISITES:
- A clean installation of Plants vs. Zombies: Fusion v4.0.5 (English or Chinese).

INSTALLATION STEPS:

Step 1: Install BepInEx (if not already installed)
--------------------------------------------------
1. Run "BepInExInstall.exe" located in this folder.
2. Select your game's executable ("PlantsVsZombiesRH.exe").
3. Choose BepInEx 6 (IL2CPP x64) and complete installation.
   * If BepInEx 6 is already installed, proceed to Step 2.

Step 2: Copy Mod & Framework Files
-----------------------------------
1. Copy the "BepInEx" folder from this package into your game root folder.
   - When prompted by Windows, choose "Replace the files in the destination"
     (this replaces BepInEx\core\ with the custom Il2CppInterop libraries required by these mods).
2. Copy "MemoryAOB.dll" into your game root folder (in the same directory as PlantsVsZombiesRH.exe).
3. Copy the "SkinLoader" folder into your game root folder.

Step 3: Launch & Enjoy
----------------------
1. Start "PlantsVsZombiesRH.exe".
2. The BepInEx console window will open and load all 400+ mods automatically.
3. In-game:
   - Press F1 / configured hotkey to open Magnetar Client for cheats, debug tools, and speed control.
   - Use Simple Spawner to summon custom fusion plants and zombies.
================================================================================
```

### `README_MODULAR.txt` (For Package 3 - Modular Multi-Part)
```
================================================================================
  PvZ Fusion 4.0.5 Modded Edition - Modular / Multi-Part Installation Guide
================================================================================

HOW TO USE MODULAR PARTS:

1. MANDATORY FIRST STEP:
   - Download and extract "Part00_Prerequisites_And_Core.zip" into your game directory.
   - Run BepInExInstall.exe if BepInEx 6 is not installed yet.
   - Ensure MemoryAOB.dll is in the same directory as PlantsVsZombiesRH.exe.

2. CHOOSE YOUR MOD PACKS:
   - You can download ANY or ALL of Part01 through Part08 depending on your preferences:
     * Part01: Wuxuan Mengxi (99 mods)
     * Part02: Ultimate Plant Pack (105 mods)
     * Part03: Inf75 (58 mods)
     * Part04: HengMing (36 mods)
     * Part05: Salmon & RogueShooting (49 mods)
     * Part06: Community Authors (60 mods)
     * Part07: Tproplay Tools (Magnetar Client + Spawner)
     * Part08: Skin Packs (Custom Skins)

3. EXTRACT TO INSTALL:
   - Extract each chosen part directly into your PvZ Fusion game root folder.
   - All paths are structured to merge seamlessly into BepInEx\plugins\.
================================================================================
```

---

## 5. Google Drive Folder Layout

```
Google Drive Root
└── PvZ Fusion 4.0.5 Modded Edition (v1.0.0 Release)/
    ├── 1. Full Game (Standalone)/
    │   └── PvZ_Fusion_4.0.5_Modded_Full_v1.0.0.zip
    ├── 2. Mods & Framework Only (Addon)/
    │   └── PvZ_Fusion_4.0.5_Mods_Only_v1.0.0.zip
    └── 3. Modular Packs (Multi-Part)/
        ├── README_MODULAR.txt
        ├── Part00_Prerequisites_And_Core.zip
        ├── Part01_Wuxuan_Mengxi_Pack.zip
        ├── Part02_Ultimate_Plant_Pack.zip
        ├── Part03_Inf75_Pack.zip
        ├── Part04_HengMing_Pack.zip
        ├── Part05_Salmon_Pack.zip
        ├── Part06_Community_Packs.zip
        ├── Part07_Tproplay_Tools.zip
        └── Part08_Skin_Packs.zip
```
