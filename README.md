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
They can be found in the Executables directory for both Arsenal types.


1. **Install Python 3.x** on your system.
2. **Install required modules**:
   - `pyautogui`
   - `pyperclip`
3. **Run of the scripts**:
   - `automaticACE_simple.py`
   - `automaticVanilla_simple.py`

## Dependencies

- Python 3.x
- `pyautogui` module
- `pyperclip` module

## Contact

For assistance, please contact [Spc.] LeX.