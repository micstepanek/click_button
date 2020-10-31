#!/usr/bin/env python3.6
import os
import pyautogui


def get_absolute_path(relative_path):
    this_file_path = os.path.realpath(__file__)
    this_file_directory = os.path.dirname(this_file_path)
    absolute_path = os.path.join(this_file_directory, relative_path)
    return absolute_path


pyautogui.click(get_absolute_path('print_friendly.png'))



