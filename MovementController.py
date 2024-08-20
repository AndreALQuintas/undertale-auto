import pyautogui
import time
import keyboard
import threading

class MovementController:
    def __init__(self, x, y):
        heart_height = 36
        heart_width = 36

        self.x = x
        self.y = y

        self.min_x = 789 + heart_width // 2
        self.min_y = 520 + heart_height // 2

        self.max_x = 1102 - heart_width // 2
        self.max_y = 831 - heart_height // 2

        self.spd = 336  # pixeis por segundo

    def update_pos(self, x, y):
        self.x = x
        self.y = y

    def hold_key(self, key_to_hold, hold_duration):
        keyboard.press(key_to_hold)
        time.sleep(hold_duration)
        keyboard.release(key_to_hold)
        print(self.x, self.y)

    def moveLeft(self, pixel_distance):
        if self.x <= self.min_x: return

        if pixel_distance > self.x - self.min_x:
            pixel_distance = self.x - self.min_x + 5

        key_thread = threading.Thread(target=self.hold_key, args=("left", pixel_distance / self.spd))

        # Start the thread
        key_thread.start()

    def moveRight(self, pixel_distance):
        if self.x >= self.max_x: return

        if pixel_distance > self.max_x - self.x:
            pixel_distance = self.max_x - self.x + 5

        key_thread = threading.Thread(target=self.hold_key, args=("right", pixel_distance / self.spd))

        # Start the thread
        key_thread.start()

    def moveUp(self, pixel_distance):
        if self.y <= self.min_y: return

        if pixel_distance > self.y - self.min_y:
            pixel_distance = self.y - self.min_y + 5

        key_thread = threading.Thread(target=self.hold_key, args=("up", pixel_distance / self.spd))

        # Start the thread
        key_thread.start()

    def moveDown(self, pixel_distance):
        if self.y >= self.max_y: return

        if pixel_distance > self.max_y - self.y:
            pixel_distance = self.max_y - self.y + 5

        key_thread = threading.Thread(target=self.hold_key, args=("down", pixel_distance / self.spd))

        # Start the thread
        key_thread.start()