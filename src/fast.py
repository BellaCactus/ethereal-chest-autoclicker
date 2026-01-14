import pyautogui
import time

# To run this script, you must install pyautogui and opencv-python:
# pip install pyautogui
# pip install opencv-python

# --- --- FAILSAFE --- ---
# By setting this to True, you can stop the script at any time by moving
# your mouse cursor to any of the four corners of the screen.
pyautogui.FAILSAFE = True

# --- --- COORDINATES --- ---
# You MUST manually find and set these coordinates for your screen.
# Use a tool like pyautogui.displayMousePosition() or a screen ruler.
# These coordinates are for a 1440p (2560x1440) display.
# ---

# 1. Position of the robot/chest area on the main screen
CHEST_AREA_X, CHEST_AREA_Y = 320, 1050

# 2. Position of the "Open Ethereal Chest" button
OPEN_CHEST_BUTTON_X, OPEN_CHEST_BUTTON_Y = 1430, 760

# 3. Position of the chest image you click to open it (center of the pop-up)
CLICK_TO_OPEN_X, CLICK_TO_OPEN_Y = 1280, 770

# 4. Position of the outcome button (Equip/Close)
# This coordinate must be in a location where both the "Equip" and "Close"
# buttons can be clicked. You may need to find a single spot that works for both.
OUTCOME_BUTTON_X, OUTCOME_BUTTON_Y = 1280, 1220


def reliable_click(x, y):
    """Moves to coordinates and performs a more reliable mouse click."""
    pyautogui.moveTo(x, y, duration=0)  # Instant mouse movement
    pyautogui.mouseDown()
    time.sleep(0.01)  # Minimal pause to ensure click registers
    pyautogui.mouseUp()


# --- --- SCRIPT START --- ---
print("Auto-Clicker Started.")
print("Switch to your game window now. The script will begin in 3 seconds.")
print("!!! FAILSAFE: MOVE MOUSE TO ANY CORNER OF THE SCREEN TO STOP !!!")
time.sleep(3)
print("Clicks are active.")


try:
    # This loop will run forever until you stop it
    while True:
        # Step 1: Click the robot area
        print("Clicking robot area...")
        reliable_click(CHEST_AREA_X, CHEST_AREA_Y)
        time.sleep(0.05)  # Wait for the pop-up to load

        # Step 2: Click "Open Ethereal Chest"
        print("Clicking Open Ethereal Chest...")
        reliable_click(OPEN_CHEST_BUTTON_X, OPEN_CHEST_BUTTON_Y)
        time.sleep(0.05)  # Wait for the chest to appear

        # Step 3: Spam-click the chest to open it
        print("Spam-clicking the chest...")
        for _ in range(5):
            reliable_click(CLICK_TO_OPEN_X, CLICK_TO_OPEN_Y)
            time.sleep(0.01)

        # Step 4: Click the outcome button (Equip or Close)
        # This single click will handle both outcomes.
        print("Clicking outcome button...")
        reliable_click(OUTCOME_BUTTON_X, OUTCOME_BUTTON_Y)
        time.sleep(0.1)  # A small delay to ensure the screen transitions

except pyautogui.FailSafeException:
    print("\nFailsafe triggered. Script stopped.")
except KeyboardInterrupt:
    print("\nScript stopped by user (CTRL+C).")
except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("Auto-Clicker finished.")
