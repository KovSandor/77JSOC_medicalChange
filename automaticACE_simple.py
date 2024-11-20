import pyautogui
import time
import pyperclip
from pynput.keyboard import Key, Controller, Listener, KeyCode
import threading
import sys

keyboard = Controller()
stop_script = False  # Flag to control the script

# Define the failsafe key combination (e.g., Backspace)
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

    print("Press BACKSPACE to STOP")
    print("You have 10 seconds to switch to Arma3 Arsenal screen.")

get_user_inputs()

# Define positions (manual measurements)
position_Loadout = (700, 1050)
position_Export = (870, 1050)
position_Import = (1040, 1050)
position_Load = (1500, 940)
position_Save = (1250, 940)


# Wait for 5 seconds to switch to Arma3 Arsenal screen
time.sleep(10)

# Loop through the specified range of loadouts
for i in range(1, 100):
    if stop_script:
        print("Script stopped by user.")
        break
    
    # Click on Loadout
    pyautogui.click(position_Loadout)
    time.sleep(0.5)
    
    # Press Down arrow 'i' times
    for _ in range(i):
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        time.sleep(0.3)
        if stop_script:
            print("Script stopped by user.")
            break
    if stop_script:
        break
    
    # Click on Load
    pyautogui.click(position_Load)
    time.sleep(0.7)
    
    # Press ESC
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(0.3)
    
    # Click on Export
    pyautogui.click(position_Export)
    time.sleep(0.7)

    # Modify the clipboard content
    current = pyperclip.paste()
    modified = current.replace('saline', 'plasma')
    modified = modified.replace('["ACE_fieldDressing",20]', '["ACE_fieldDressing",10],["ACE_packingBandage",10]')
    pyperclip.copy(modified)
    time.sleep(0.3)
    
    # Click on Import
    pyautogui.click(position_Import)
    time.sleep(0.7)
    
    # Click on Loadout again
    pyautogui.click(position_Loadout)
    time.sleep(0.7)
    
    # Press Down arrow 'i' times
    for _ in range(i):
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        time.sleep(0.3)
        if stop_script:
            print("Script stopped by user.")
            break
    if stop_script:
        break
    
    # Click on Save
    pyautogui.click(position_Save)
    time.sleep(0.7)
    
    # Press ESC
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(0.3)

print("\n" + "-"*50 + "\n")
print("Script has terminated.")