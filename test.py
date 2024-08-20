import pyautogui
import keyboard
import time
import random
from PIL import ImageGrab, Image

def start_timer():
    random.seed()

    num_list = []
    start_time = time.time()
    while keyboard.is_pressed('right arrow'):
        elapsed_time = time.time() - start_time
        if round(elapsed_time, 3) % 0.5 == 0 and round(elapsed_time, 2) not in num_list:
            print(f"RAWR Timer: {elapsed_time:.2f} seconds")

            num_list.append(round(elapsed_time, 2))
        print(f"Timer: {elapsed_time:.2f} seconds", end='\r')
    print(f"Timer stopped. {elapsed_time} seconds")

if __name__ == "__main__":
    print("Press and hold the 'right arrow' key to start the timer...")
    keyboard.wait('right arrow')
    print("Timer started. Release the 'right arrow' key to stop it.")
    start_timer()

