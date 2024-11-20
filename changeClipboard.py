import pyperclip
import time

def main():
    while True:
        current = pyperclip.paste()
        modified = current.replace('saline', 'plasma')
        modified = modified.replace('["ACE_fieldDressing",20]', '["ACE_fieldDressing",10],["ACE_packingBandage",10]')
        pyperclip.copy(modified)
        time.sleep(1)

if __name__ == "__main__":
    main()