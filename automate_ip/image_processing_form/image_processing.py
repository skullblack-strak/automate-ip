import pyscreeze
import numpy as np
import pyautogui as pg
import cv2
import imutils

# print("Working dir:", os.getcwd())
# print("Files in here:", os.listdir("."))

def find_image_position():
    try:
        centerPositionImage = pyscreeze.locateCenterOnScreen('assets/image/title-new-infomation.png', grayscale=True, confidence=0.9)
        print("success")
        return centerPositionImage
    except:
        print("catch")
        return
    
def find_image_position_test():
    try:
        centerPositionImage = pyscreeze.locateCenterOnScreen('assets/image/title-new-infomation.png', grayscale=True, confidence=0.9)
        return centerPositionImage
    except:
        return

# ==================================================================
# ======================== new solution ============================ 
# ==================================================================
def find_infomation_form():
    try:
        form = pg.locateOnScreen('assets/image/patient-infomation-new.png', grayscale=True, confidence=0.9)
        return form
    except:
        return
    
def find_patient_input():
    try:
        input = pg.locateOnScreen('assets/image/patient-input.png', grayscale=True, confidence=0.9)
        return input
    except:
        return

def find_first_name_input():
    try:
        input = pg.locateOnScreen('assets/image/first-name-input.png', grayscale=True, confidence=0.9)
        return input
    except:
        return

def find_last_name_input():
    try:
        input = pg.locateOnScreen('assets/image/last-name-input.png', grayscale=True, confidence=0.9)
        return input
    except:
        return

def find_sex_input():
    try:
        input = pg.locateOnScreen('assets/image/sex-input.png', grayscale=True, confidence=0.9)
        return input
    except:
        return

def find_birth_date_input():
    try:
        input = pg.locateOnScreen('assets/image/birth-date-input.png', grayscale=True, confidence=0.9)
        return input
    except:
        return