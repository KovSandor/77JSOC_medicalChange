import pyautogui
import time
import pyperclip
from pynput.keyboard import Key, Controller, Listener, KeyCode
import threading
import sys

keyboard = Controller()
stop_script = False  # Flag to control the script

# Define the failsafe key combination (e.g. Backspace)
FALLBACK_COMBINATION = {Key.backspace}

# Set to keep track of currently pressed keys
current_keys = set()


# Callback function when a key is pressed.
# Adds the key to current_keys and checks for the failsafe combination.
def on_press(key):
    global stop_script
    current_keys.add(key)
    if all(k in current_keys for k in FALLBACK_COMBINATION):
        stop_script = True
        return False  # Stop the listener


# Callback function when a key is released.
# Removes the key from current_keys.
def on_release(key):
    try:
        current_keys.remove(key)
    except KeyError:
        pass


# Initializes and starts the keyboard listener.
def listen_failsafe():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


# Start the listener in a separate thread
listener_thread = threading.Thread(target=listen_failsafe, daemon=True)
listener_thread.start()

# User Input Section
def get_user_inputs():
    print("\n" + "="*50)
    print(" Arma3 Loadout Modification Script ".center(50, "="))
    print("="*50 + "\n")

    print("Run as Administrator using 1920x1080 resolution, 100% scaling.")
    print("="*50 + "\n")

    
    # Prompt 1: Backup Confirmation
    backup_check = input("Have you made an Arma3 profile backup? (y/n): ")
    if backup_check.strip().lower() not in ('y', 'yes'):
        print("\nBackup not confirmed. Exiting the script.")
        sys.exit()
    
    print("\n" + "-"*50 + "\n")

    print("Failsafe: BACKSPACE")
    print("You have 25 seconds to switch to Arma3 Arsenal screen.")
    
get_user_inputs()

# Define positions (manual measurements)
position_Load = (1055, 1055)
position_Export = (1250, 1055)
position_Import = (1450, 1055)
position_Save = (850, 1055)

# Wait for 25 seconds to switch to Arma3 Arsenal screen
time.sleep(25)

# Loop through the specified range of loadouts
for i in range(0, 300):
    if stop_script:
        print("Script stopped by user.")
        break

    # Click on Load
    pyautogui.click(position_Load)
    time.sleep(1)

    # Press Down arrow 'i' times
    for _ in range(i):
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        time.sleep(0.5)
        if stop_script:
            print("Script stopped by user.")
            break
    if stop_script:
        break

    # Press Enter to load
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1.5)

    # Click on Export
    pyautogui.click(position_Export)
    time.sleep(1.5)

    # Modify the clipboard content
    current = pyperclip.paste()
    modified = current.replace('saline', 'plasma')
    modified = modified.replace(
        'for "_i" from 1 to 20 do {this addItemToUniform "ACE_fieldDressing";};',
        'for "_i" from 1 to 10 do {this addItemToUniform "ACE_fieldDressing";};for "_i" from 1 to 10 do {this addItemToUniform "ACE_packingBandage";};'
    )
    modified = modified.replace(
        'for "_i" from 1 to 20 do {this addItemToVest "ACE_fieldDressing";};',
        'for "_i" from 1 to 10 do {this addItemToVest "ACE_fieldDressing";};for "_i" from 1 to 10 do {this addItemToVest "ACE_packingBandage";};'
    )
    modified = modified.replace(
        'for "_i" from 1 to 20 do {this addItemToBackpack "ACE_fieldDressing";};',
        'for "_i" from 1 to 10 do {this addItemToBackpack "ACE_fieldDressing";};for "_i" from 1 to 10 do {this addItemToBackpack "ACE_packingBandage";};'
    )

    # If you don't keep the 20 basic bandages in the same container... bad luck for you

    pyperclip.copy(modified)
    time.sleep(1.5)

    # Click on Import
    pyautogui.click(position_Import)
    time.sleep(1.5)

    # Click on Save
    pyautogui.click(position_Save)
    time.sleep(1.5)

    # Press Down arrow 'i + 2' times
    # When saving, the second press selects the 1st row
    for _ in range(i + 2):
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        time.sleep(0.5)
        if stop_script:
            print("Script stopped by user.")
            break
    if stop_script:
        break

    # Press Enter to save
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1.5)

print("\n" + "-"*50 + "\n")
print("Script has terminated.")