import cv2
import pytesseract
import time

import numpy as np
from PIL import ImageGrab


def main():
    # maximums = calibrate()  <--- pass to emg_reader
    emg_reader()


def emg_reader():

    print("--- EMG Reader Activated ---")

    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    # TODO replace with vals from calibration
    channel_1_max = 0.2
    channel_2_max = 0.2
    channel_3_max = 0.2
    channel_4_max = 0.2

    while (True):

        # bbox = (Left, Top, Right, Bottom) in pixels
        # coords correspond to 'input vals' window open to half screen on laptop monitor
        capture = ImageGrab.grab(bbox=(0, 0, 646, 678))

        captured_str = pytesseract.image_to_string(
            cv2.cvtColor(np.array(capture), cv2.COLOR_BGR2GRAY),
            lang='eng')
        split_str = captured_str.split()

        channel_1_curr = float(split_str[-4])
        channel_2_curr = float(split_str[-3])
        channel_3_curr = float(split_str[-2])
        channel_4_curr = float(split_str[-1])

        if (channel_1_curr > channel_1_max):
            print("Channel 1 (L Forearm)")

        if (channel_2_curr > channel_2_max):
            print("Channel 2 (L Bicep)")

        if (channel_3_curr > channel_3_max):
            print("Channel 3 (R Forearm)")

        if (channel_4_curr > channel_4_max):
            print("Channel 4 (R Bicep)")


def calibrate():
    # Initializes the maximum values for all 4 channels.
    # Returns list: [channel_1_max, channel_2_max, channel_3_max, channel_4_max]

    input("Press enter to begin calibration:")

    print("start")
    end_time = time.time() + 5
    while time.time() < end_time:
        x = 1
    print("done")


# Entry
main()
