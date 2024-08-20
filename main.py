import pyautogui
import keyboard
import time
import random
from PIL import ImageGrab, Image
import win32gui
import win32api
from MovementController import MovementController

spd = 336 #pixeis por segundo
heart_height = 36
heart_width = 36

min_x = 789
min_y = 520

max_x = 1102
max_y = 831

dc = win32gui.GetDC(0)
green = win32api.RGB(0, 255, 0)

heart_img = Image.open("./imgs/heart36-v2.png")

def draw_rectangle_heart(location):
    x, y, width, height = location
    for i in range(x - 1, x + width + 1):
        win32gui.SetPixel(dc, i, y - 10, green)
        win32gui.SetPixel(dc, i, y + height + 10, green)


def find_heart(confidence=0.75):

    # Search for the image on the screen
    location = pyautogui.locateOnScreen(heart_img, confidence=confidence)

    if location is not None:
        """x, y, width, height = location
        center_x = x + width / 2
        center_y = y + height / 2"""
        return location
    else:
        return None

Player = None

while True:
    position = find_heart()

    if position:
        if Player == None:
            Player = MovementController(position.left, position.top)

        Player.update_pos(position.left, position.top)

        if keyboard.is_pressed("w"):
            Player.moveUp(200)

        if keyboard.is_pressed("s"):
            Player.moveDown(200)

        if keyboard.is_pressed("a"):
            Player.moveLeft(200)

        if keyboard.is_pressed("d"):
            Player.moveRight(200)

        if keyboard.is_pressed("q"):
            Player.moveLeft(200)
            Player.moveUp(200) 
        #draw_rectangle_heart(position)
    else:
        print("Image not found on the screen.")
    time.sleep(1/60)