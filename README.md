# 77th JSOC 2024 November Medical change

This project automates the modification of player loadouts in the game *Arma 3*. 

## Overview

The Python scripts adjust medical items in player profiles by interacting with the game's interface. They replace items like saline with plasma and modify quantities of medical supplies.
These are in line with the latest 2024-11-20 Loadout changes regarding the medical test phase. 

## Features

- Automated replacement of medical items (e.g., saline to plasma).
- Modification of medical supply quantities: 20 Basic bandages -> 10 Basic bandages & 10 packing bandages

## Getting Started

This script clicks on certain parts of your screen and presses keys (ESC, Down Arrow, Enter) in order to:
1. Load in your loadout.
2. Export it to clipboard.
3. Modify this exported text to replace old medical equipment.
4. The modified text is copied back to your clipboard.
5. Use the Arsenal's import function to read the updated loadout.
6. Save it in place of the old loadout.

This is an automated way to bring all your loadouts up to standard, but there is no warranty attached.
Ultimately, you are responsible for your loadouts.

### Executable files

I provide compiled .exe files for both Arsenal systems (ACE and Vanilla). 
If you do not know how to run a python script I suggest that you use this method.
They can be found in the [Executables](./Executables/) directory for both Arsenal types.
Click on [automaticACE_simple.exe](./Executables/automaticACE_simple.exe) or [automaticVanilla_simple.exe](./Executables/automaticVanilla_simple.exe) then on the top right you will find a Download raw button like this:
![Download button](./Pictures/downloadButton.png) 


### How to use executables

After the download follow these instructions:
1. Backup your Arma3 profile. This prevents you from data loss and makes rolling back.
2. In your Windows settings set your primary Display Resolution to 1920x1080, and Scale to 100%. The script was made for UI elements displayed on screens like this to maximize accesibility.
3. Launch Arma3 with the modpack.
4. Open Options / Video / Display settings and set the Display mode to Fullscreen Window (run Arma3 on your primary display).
5. In the Main menu open Tutorials / Virtual (Vanilla) Arsenal or ACE Arsenal.
6. Stay on the opening view of the respective arsenal.
7. Run the downloaded executable as Administrator (it might work without it as well).
8. ALT+TAB back to Arma3, you have 10 seconds before clicking starts.
9. Let the script run, do not touch anything. 
10. By default it will check 100 ACE loadouts and 300 Vanilla arsenals.
11. If you have less or want to stop to check if everything is fine press BACKSPACE. This will stop the script. (If that does not work try to close the command window, bit difficult with all the clicking.) If you restart the script it will start from the beginning. 
12. Success! You should have plasma instead of saline and 10x Packing bandage and 10x Basic bandage instead of 20x Basic bandage. 
13. You have to manually modify your Medic loadouts to add the new equipment and remove extra Packing bandages.

I encourage you to check the corresponding .py scripts before you run executables on your system and if you can, I encourage you to run the python scripts.

### How to use scripts

1. **Install Python 3.x** on your system.
2. **Install Required modules**:
   - `pyautogui`
   - `pyperclip`
3. **Instead of Step 7, run one of the scripts**:
   - `automaticACE_simple.py`
   - `automaticVanilla_simple.py`

## Contact

For assistance, please contact [Spc.] LeX.