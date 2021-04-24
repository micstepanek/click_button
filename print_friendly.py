#!/usr/bin/env python3
import pyautogui
x = 1750 
y = 52
if pyautogui.pixelMatchesColor(x, y,(109,162,34)):
    pyautogui.click(x, y)
else:
    import os
    def get_absolute_path(relative_path):
        this_file_path = os.path.realpath(__file__)
        this_file_directory = os.path.dirname(this_file_path)
        absolute_path = os.path.join(this_file_directory, relative_path)
        return absolute_path
    pyautogui.click(get_absolute_path('print_friendly.png'))
    




