#!/usr/bin/env python3
import pyautogui
if pyautogui.pixelMatchesColor(1750, 52,(109,162,34)):
    pyautogui.click(1750, 52)
else:
    import os
    def get_absolute_path(relative_path):
        this_file_path = os.path.realpath(__file__)
        this_file_directory = os.path.dirname(this_file_path)
        absolute_path = os.path.join(this_file_directory, relative_path)
        return absolute_path
    pyautogui.click(get_absolute_path('button.png'))
    




