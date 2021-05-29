from pyautogui import *
import pyautogui
import time
import keyboard
import random
import _thread
import winsound


class Screen:

    def __init__(self, start, end, pods, levelup):
        self.x_start    = start[0]
        self.y_start    = start[1]
        self.x_end      = end[0]
        self.y_end      = end[1]
        self.x_center   = ((self.x_end - self.x_start) / 2) + self.x_start
        self.y_center   = ((self.y_end - self.y_start) / 2) + self.y_start
        self.x_pods     = pods[0]
        self.y_pods     = pods[1]
        self.x_append   = self.x_end - self.x_start
        self.y_append   = self.y_end - self.y_start
        self.x_level    = levelup[0]
        self.y_level    = levelup[1]

    @property
    def to_str(self):
        return self
