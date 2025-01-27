import cv2 as cv
import numpy as np
import pyautogui
import time
import threading
from threading import Thread
import os


class FishingAgent:
    def __init__(self, main_agent):
        self.main_agent = main_agent

        # interpolate here_path to get the path to the fishing target image
        here_path = os.path.dirname(os.path.realpath(__file__))
        self.fishing_target = cv.imread(
            os.path.join(
                here_path,
                "assets", "bobber.png"
            )
        )

        self.fishing_thread = None
        self.stop_event = threading.Event()
        self.is_preparing = False


    def cast_lure(self):
        print("Casting!")
        self.fishing = True
        self.cast_time = time.time()
        pyautogui.press('1')
        time.sleep(1)
        self.find_lure()


    def find_lure(self):
        start_time = time.time()
        lure_location = cv.matchTemplate(self.main_agent.cur_img, self.fishing_target, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(lure_location)
        self.lure_location = max_loc
        self.move_to_lure()


    def move_to_lure(self):
        if self.lure_location:
            pyautogui.moveTo(self.lure_location[0], self.lure_location[1], .2)
            self.watch_lure()
        else:
            print("Warning: Attempted to move to lure_location, but lure_location is None (fishing_agent.py line 32)")
            return False


    def watch_lure(self):
        time_start = time.time()
        while not self.stop_event.is_set():
            pixel = self.main_agent.cur_imgHSV[self.lure_location[1]][self.lure_location[0]]
            if self.main_agent.zone == "orgrimmar" and self.main_agent.cur_time == "Night":
                if pixel[0] <= 30 or pixel[1] <= 50 or pixel[2] <= 30:
                    print("Bite detected!")
                    print(pixel)
                    time.sleep(1)
                    break
                if time.time() - time_start >= 30:
                    print("Fishing timeout!")
                    break
            elif self.main_agent.zone == "orgrimmar" and self.main_agent.cur_time == "Day":
                if pixel[0] <= 50 or pixel[1] <= 50 or pixel[2] <= 50:
                    print("Bite detected!")
                    print(pixel)
                    time.sleep(1)
                    break
                if time.time() - time_start >= 30:
                    print("Fishing timeout!")
                    break
            elif self.main_agent.zone == "Barrens" and self.main_agent.cur_time == "Night":
                if pixel[0] <= 50:
                    print("Bite detected!")
                    print(pixel)
                    time.sleep(1)
                    break
                if time.time() - time_start >= 30:
                    print("Fishing timeout!")
                    break
            print(pixel)
        if not self.stop_event.is_set():  # Only pull the line if not stopping
            self.pull_line()


    def pull_line(self):
        pyautogui.rightClick()
        time.sleep(1)
        if not self.stop_event.is_set():
            self.run()


    def run(self):
        if self.main_agent.cur_img is None:
            print("Image capture not found!  Did you start the screen capture thread?")
            return
        print("Starting fishing thread in 3 seconds...")
        time.sleep(3)

        if self.stop_event.is_set():
            print("Fishing preparation stopped.")
            self.is_preparing = False
            return

        self.stop_event.clear()  # Reset the stop_fishing event

        self.fishing_thread = Thread(
            target=self.cast_lure,
            args=(),
            name="fishing thread",
            daemon=True)
        self.fishing_thread.start()
        self.is_preparing = False  # Reset preparing flag

    def stop_fishing(self):
        print("Stopping fishing thread...")
        self.stop_event.set()  # Signal the thread to stop

        # If the agent is in the preparation phase, wait for it to finish
        if self.is_preparing:
            print("Waiting for preparation to finish...")
            while self.is_preparing:
                time.sleep(0.1)

        # Stop the fishing thread if it exists and is running
        if self.fishing_thread and self.fishing_thread.is_alive():
            self.fishing_thread.join()  # Wait for the thread to finish
        print("Fishing thread stopped.")