import pytesseract
import numpy as np
import cv2 as cv
from datetime import datetime


def get_cur_zone(cur_img):

    top_left = (1770, 5)
    bottom_right = (1912, 20)

    zone_name_img = cur_img[
        top_left[1]:bottom_right[1],
        top_left[0]:bottom_right[0]
    ]

    zone_name_img = cv.cvtColor(zone_name_img, cv.COLOR_BGR2GRAY)
    zone_name_img = cv.threshold(zone_name_img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

    zone = pytesseract.image_to_string(zone_name_img)
    zone = zone.lower().strip()

    if zone == "valley of honor":
        zone = "Orgrimmar"
    # print(zone)

    return zone


def get_cur_time():

    current_time = datetime.now()
    hour = current_time.hour  # Extract the hour (0-23)

    # Determine if it's day or night
    if 6 <= hour < 18:
        return "Day"
    else:
        return "Night"