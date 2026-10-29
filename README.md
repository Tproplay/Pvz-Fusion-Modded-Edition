# Plants vs. Zombies: Fusion Modded Edition (English Version)

A comprehensive, optimized, and fully organized modded distribution for **Plants vs. Zombies: Fusion v4.0.5 (English Version)**.

This edition consolidates over **400+ community fusion plants, zombies, tools, and visual enhancements**, structured into dedicated author packages with pre-applied stability patches, crash fixes, and full English translation support.

---

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Mod Categories and Author Packs](#mod-categories-and-author-packs)
- [Pre-Applied Fixes and Optimizations](#pre-applied-fixes-and-optimizations)
- [Download Options](#download-options)
- [Installation Guide](#installation-guide)
  - [Option A: Standalone Full Game (Zero Setup)](#option-a-standalone-full-game-zero-setup)
  - [Option B: Mods and Framework Addon](#option-b-mods-and-framework-addon)
  - [Option C: Modular Multi-Part Packs](#option-c-modular-multi-part-packs)
- [In-Game Controls and Usage](#in-game-controls-and-usage)
- [Credits and Author Attributions](#credits-and-author-attributions)
- [Documentation](#documentation)

---

## Overview

Plants vs. Zombies: Fusion is a fan-created reimagining of PvZ that introduces multi-plant hybridization, custom mechanics, and unique boss encounters. 

This repository and release suite provide a complete, verified modpack for version 4.0.5. Loose mod files have been categorized into structured directories, dependency conflicts and memory issues have been resolved, and duplicate binaries have been purged to keep total install size under 2 GB.

---

## Key Features

- **400+ Hybrid Plants and Zombies**: Complete fusion trees spanning offensive, defensive, and economic plant hybrids.
- **Built-in Quality of Life Utilities**:
  - **Magnetar Client**: Custom mod menu, in-game speed multiplier, and debug toolset.
  - **Simple Spawner**: On-demand entity spawner to test plant and zombie interactions.
- **Pre-Configured English Localization**: Built-in XUnity.AutoTranslator and adaptive almanac UI sliders.
- **Optimized Performance**:
  - Removed intrusive background UI loops and sliding tabs.
  - Purged 114 MB of duplicate binaries.
  - Console encoding handle fixes to ensure every plugin loads reliably without crashing.

---

## Mod Categories and Author Packs

All plugins are organized inside `BepInEx/plugins/` by author and series:

| Category Folder | Mod Count | Description |
| :--- | :--- | :--- |
| **Mods - Ultimate Plant Pack** | 105 mods | Cosmic, divine, and celestial hybrid series (AstralGodCabbage, BloodMoonPhantomCabbage, etc.). |
| **Mods - Wuxuan Mengxi** | 99 mods | Plant mods created or adapted by Wuxuan Mengxi (BambooWoodMortar, ButterGloom, CoffeeBean, etc.). |
| **Mods - Inf75** | 58 mods | Full collection of inf75 fusion series plants and zombies. |
| **Mods - HengMing** | 36 mods | HengMing hybrid series, patched with clean UI and no intrusive side popups. |
| **Mods - Salmon** | 49 mods | SalmonCN plant creations along with the complete RogueShooting series. |
| **Mods - Community** | 28 mods | Independent creations by community contributors (Cassidy, Xingchen, Deqing, Soviet, etc.). |
| **Mods - Murong Guqing** | 19 mods | SuperMachine nut hybrids and specialized defense series. |
| **Mods - LikeFengzi** | 10 mods | Hypno and Gatling hybrid series by LikeFengzi. |
| **Mods - Ttpersik** | 3 mods | Portal and obsidian hybrid series by Ttpersik. |
| **Mods - Tproplay** | 2 mods | Magnetar Client and Simple Spawner utility suite. |

---

## Pre-Applied Fixes and Optimizations

This edition includes critical binary and configuration patches to ensure zero-crash gameplay:

1. **CustomizeLib Property Crash Fix**:
   - Resolved an `ArgumentException: Property set method not found` during `UIMgr.PostEnterMainMenu()` by patching getter-only calls to `TypeMgr.RedPlant` and `TypeMgr.UncrashablePlants`.
2. **MengxiLib SkinLoader Coroutine Fix**:
   - Prevented `NullReferenceException` crashes in `MengxiLib.BepInEx.Extensions.TryGetAsset` when skin asset bundles are missing or unreadable.
3. **RHByteFiddler and MemoryAOB Placement**:
   - Positioned `MemoryAOB.dll` and `RHByteFiddler.dll` in root locations required by preloader patchers and P/Invoke routines.
4. **HengMing Reminder and Side Tab Removal**:
   - Patched `HengMingModsLib.dll` IL instructions (`KindReminderPostLoad::Build`, `DriverTick`, `KindReminder::Build`) to eliminate intrusive sliding side menus, buttons, and per-frame UI polling.
5. **Console Encoding Handle Fix**:
   - Fixed `IOException: The handle is invalid` errors caused by mods invoking `Console.OutputEncoding = Encoding.UTF8` during plugin load.
6. **Binary Footprint Reduction**:
   - Converted duplicate 54 MB shadow binaries in `BepInEx/plugins/Mods - HengMing` to 0-byte placeholders as expected by preloader synchronization routines.

---

## Download Options

Releases are distributed through GitHub Releases and Google Drive:

- **GitHub Release Page**: [Plants vs. Zombies Fusion Modded Edition v4.0.5](https://github.com/Tproplay/Pvz-Fusion-Modded-Edition/releases/tag/v4.0.5)
- **Google Drive Release Mirror**: [Google Drive v4.0.5 Folder](https://drive.google.com/drive/folders/1UanI2jBlpPjW_sOuwN0sk-Rjg9fdUnM5?usp=sharing)

### Packages:

1. **Standalone Full Game (`PvZ_Fusion_4.0.5_Modded_Full_v4.0.5.zip`)**
   - Available on: **GitHub Releases** and **Google Drive**
   - Size: ~1.82 GB uncompressed
   - Ready to play immediately. Includes the full game engine, .NET 6 IL2CPP runtime, BepInEx 6, all 400+ mods, and configs.
   - [Google Drive Direct Download](https://drive.google.com/file/d/1AAwrQ5clL-nkzmCiPBjZWRrWymhkvpnw/view?usp=sharing)
   - [Google Drive Folder](https://drive.google.com/drive/folders/1cpAJlzO2BBXSU8YJv-_R8KNZdRfB4s9h?usp=sharing)

2. **Mods and Framework Addon (`PvZ_Fusion_4.0.5_Mods_Only_v4.0.5.zip`)**
   - Available on: **GitHub Releases** and **Google Drive**
   - Size: ~1.32 GB uncompressed
   - For players who already have a clean copy of PvZ Fusion 4.0.5. Contains `BepInExInstall.exe`, custom `Il2CppInterop` binaries, all 400+ mods, configs, and skins.
   - [Google Drive Direct Download](https://drive.google.com/file/d/1OYzv5slwjKCg9kF0bzTpiWiQO-ltttjq/view?usp=sharing)
   - [Google Drive Folder](https://drive.google.com/drive/folders/1T0RUbhGofIbrw8J7LD_iftwQMc7j0IwO?usp=sharing)

3. **Modular Multi-Part Packs**
   - Available on: **Google Drive ONLY**
   - 9 individual archives (`Part00` through `Part08`) allowing selective downloads for slower internet connections or custom mod setups:
     - [Google Drive Modular Folder](https://drive.google.com/drive/folders/1k0t127VL0vKr2A92BcRK_5HL8XkF2Jvz?usp=sharing)
     - [Part 00 - Prerequisites and Core](https://drive.google.com/file/d/136lw7RzBNXV7mRxglozCxYyRWDvaDgDb/view?usp=sharing)
     - [Part 01 - Wuxuan Mengxi Pack](https://drive.google.com/file/d/1l-CiAqlUdJn_3_vdUDD3a5EPaimYo_Cc/view?usp=sharing)
     - [Part 02 - Ultimate Plant Pack](https://drive.google.com/file/d/13X-55iWHtL4syfWCArPF9nzjHDxzBq_U/view?usp=sharing)
     - [Part 03 - Inf75 Pack](https://drive.google.com/file/d/1lI0PCNsxCPdq7xNigLVSiUveOH9-XXzt/view?usp=sharing)
     - [Part 04 - HengMing Pack](https://drive.google.com/file/d/1z8YzLMgTgpuis5WsMHUkkRiGtppT2tas/view?usp=sharing)
     - [Part 05 - Salmon Pack](https://drive.google.com/file/d/1qgTo4jAF8dY3A4pKp7mZdIxHzG4JJiPj/view?usp=sharing)
     - [Part 06 - Community Packs](https://drive.google.com/file/d/1uchVCD5_zPHeq9aAKUvBjykbzmXCBE-Y/view?usp=sharing)
     - [Part 07 - Tproplay Tools](https://drive.google.com/file/d/1hvBgL8Vtc5j7O-mBxBwyskgNZIAlGhkI/view?usp=sharing)
     - [Part 08 - Skin Packs](https://drive.google.com/file/d/1E7nt_IqIR1TVdQQpT996dYiNMrkl1kqQ/view?usp=sharing)

---

## Installation Guide

### Option A: Standalone Full Game (Zero Setup)
1. Download `PvZ_Fusion_4.0.5_Modded_Full_v4.0.5.zip`.
2. Extract the archive to any folder (for example, `C:\Games\PvZ Fusion Modded Edition\`).
3. Double-click `PlantsVsZombiesRH.exe` to play.

### Option B: Mods and Framework Addon
Use this option if you already have a clean installation of PvZ Fusion 4.0.5:
1. Download `PvZ_Fusion_4.0.5_Mods_Only_v4.0.5.zip`.
2. If BepInEx 6 is not yet installed:
   - Run `BepInExInstall.exe` included in the package.
   - Select your game's `PlantsVsZombiesRH.exe`.
   - Install BepInEx 6 (IL2CPP x64).
3. Copy the `BepInEx` folder from the package into your game root folder.
   - When prompted, choose **Replace the files in the destination** (this installs the custom `Il2CppInterop` runtime libraries).
4. Copy `MemoryAOB.dll` to the game root folder (beside `PlantsVsZombiesRH.exe`).
5. Copy the `SkinLoader` folder to the game root folder.
6. Launch `PlantsVsZombiesRH.exe`.

### Option C: Modular Multi-Part Packs
1. Download `Part00_Prerequisites_And_Core.zip` and extract it into your PvZ Fusion game directory.
2. Run `BepInExInstall.exe` if BepInEx 6 is not yet installed.
3. Download any combination of `Part01` through `Part08` and extract them directly into your game directory. Files are structured to merge cleanly into `BepInEx/plugins/`.
4. Launch `PlantsVsZombiesRH.exe`.

---

## In-Game Controls and Usage

- **Magnetar Client**: Press `F1` (or your configured shortcut) to open the mod configuration panel. Allows setting game speed, toggling cheats, and managing debug features.
- **Simple Spawner**: Access the spawner interface to place custom hybrid plants or test enemy waves.
- **Console Window**: On startup, a BepInEx console window will open. This is expected behavior required by the underlying .NET 6 IL2CPP runtime and mod initialization routines.

---

## Credits and Author Attributions

- **Modpack Maintenance & Fixes**:
  - **Tproplay**: Crash fixes (CustomizeLib property set crash fix, MengxiLib coroutine null check fix, BepInEx console encoding handle fix, HengMing reminder suppressor, memory patcher alignment), build verification, packaging, and distribution.
  - **❣✰𝓛𝓾𝓷𝓪✰❣**: Downloaded and collected all 400+ community fusion mods.
- **Original Game**: PopCap Games / EA
- **PvZ Fusion Original Creator**: Lan Pao Pao (Bluefly)
- **Mod Authors & Contributors**:
  - Ultimate Plant Pack Team
  - Wuxuan Mengxi
  - Inf75
  - HengMing
  - SalmonCN
  - Murong Guqing
  - LikeFengzi
  - Ttpersik
  - Cassidy, Xingchen, Deqing, Soviet, and Community Modders
- **Tooling & Frameworks**:
  - BepInEx Team (BepInEx 6 IL2CPP)
  - Il2CppInterop Team
  - HarmonyX / MonoMod
  - ProHatp (BepInExInstall)
  - XUnity.AutoTranslator Team

---

## Documentation

- Detailed technical changes, bugfix breakdowns, and history: see [PATCH_NOTES.md](PATCH_NOTES.md).
