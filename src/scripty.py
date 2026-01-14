import pyautogui
import time

# --- --- FAILSAFE --- ---
# By setting this to True, you can stop the script at any time by moving
# your mouse cursor to any of the four corners of the screen.
pyautogui.FAILSAFE = True

# --- --- COORDINATES FOR 1440p (2560x1440) --- ---
# Your corrected coordinates.

# 1. Position of the robot/chest area on the main screen
CHEST_AREA_X, CHEST_AREA_Y = 320, 1050

# 2. Position of the "Open Ethereal Chest" button
OPEN_CHEST_BUTTON_X, OPEN_CHEST_BUTTON_Y = 1430, 760

# 3. Position of the chest image you click to open it (center of the pop-up)
CLICK_TO_OPEN_X, CLICK_TO_OPEN_Y = 1280, 770

# 4. Position of the "Equip" button
EQUIP_BUTTON_X, EQUIP_BUTTON_Y = 1090, 1220

# 5. Position of the final click
FINAL_CLICK_X, FINAL_CLICK_Y = 1580, 950


# --- --- SCRIPT START --- ---
print("Auto-Clicker Started.")
print("Switch to your game window now. The script will begin in 3 seconds.")
print("!!! FAILSAFE: MOVE MOUSE TO ANY CORNER OF THE SCREEN TO STOP !!!")
time.sleep(3)
print("Clicks are active.")


def reliable_click(x, y):
    """Moves to coordinates and performs a more reliable mouse click."""
    pyautogui.moveTo(x, y, duration=0) # Instant mouse movement
    pyautogui.mouseDown()
    time.sleep(0.01) # Minimal pause to ensure click registers
    pyautogui.mouseUp()


try:
    # This loop will run forever until you stop it
    while True:
        # Step 1: Click the robot area
        reliable_click(CHEST_AREA_X, CHEST_AREA_Y)

        # Step 2: Click "Open Ethereal Chest"
        reliable_click(OPEN_CHEST_BUTTON_X, OPEN_CHEST_BUTTON_Y)

        # Step 3: Click the chest to open
        reliable_click(CLICK_TO_OPEN_X, CLICK_TO_OPEN_Y)
        # A tiny delay is kept here because the chest opening animation
        # is the most likely part of the sequence to need it.
        time.sleep(0.1)

        # Step 4: Click "Equip"
        reliable_click(EQUIP_BUTTON_X, EQUIP_BUTTON_Y)

        # Step 5: Click the final location
        reliable_click(FINAL_CLICK_X, FINAL_CLICK_Y)


except pyautogui.FailSafeException:
    print("\nFailsafe triggered. Script stopped.")
except KeyboardInterrupt:
    print("\nScript stopped by user (CTRL+C).")
except Exception as e:
    print(f"\nAn error occurred: {e}")