from customtkinter import *
from PIL import Image, ImageGrab
import numpy as np
import cv2 as cv
import time
from threading import Thread
from fishing.fishing_agent import FishingAgent
import map_reader
from gui import FishingApp
import pytesseract


class MainAgent:
    def __init__(self):
        self.agents = []
        self.fishing_thread = None
        self.fishing_agent = None

        self.cur_img = None
        self.cur_imgHSV = None

        self.zone = None
        self.cur_time = None
        self.fps = None

        self.start_screen_capture()

    def start_screen_capture(self):
        update_screen_thread = Thread(
            target=self.update_screen,
            name="update screen thread",
            daemon=True,
        )
        update_screen_thread.start()
    
    def update_screen(self):

        t0 = time.time()
        ex_time = 0

        while True:
            self.cur_img_grab = ImageGrab.grab()
            self.cur_img = np.array(self.cur_img_grab)
            self.cur_img = cv.cvtColor(self.cur_img, cv.COLOR_RGB2BGR)
            self.cur_imgHSV = cv.cvtColor(self.cur_img, cv.COLOR_BGR2HSV)

            self.zone = map_reader.get_cur_zone(self.cur_img)
            self.zone = self.zone.lower().strip()
            self.cur_time = map_reader.get_cur_time()

            ex_time = time.time() - t0
            self.fps = str(round(1 / ex_time))
            t0 = time.time()

    def start_fishing(self):
        if self.fishing_agent and self.fishing_agent.fishing_thread.is_alive():
            print("Fishing is already running!")
            return
        self.fishing_agent = FishingAgent(self)  # Create a new FishingAgent
        self.fishing_agent.run()

    def stop_fishing(self):
        if self.fishing_agent:
            print("Stopping fishing agent...")
            self.fishing_agent.stop_fishing()
            self.fishing_agent = None  # Reset the fishing agent
            print("Fishing agent stopped and reset.")

if __name__ == "__main__":
    main_agent = MainAgent()
    app = FishingApp(main_agent)