# import time
# from automate_ip.infomation.file_info import read, remove
# from automate_ip.image_processing_form.auto_complete import form
from automate_ip.image_processing_form.image_processing import find_infomation_form, find_patient_input, find_first_name_input, find_last_name_input, find_sex_input, find_birth_date_input

# while True:
#     centerPositionImage = find_infomation_form()
#     # if centerPositionImage:
#     #      # read infomation file
#     #     infomation = read()
#     #     if not (infomation is None):
#     #         if len(infomation):
#     #             # auto complete from
#     #             form(centerPositionImage.x, centerPositionImage.y, infomation)
#     #             # remove infomation
#     #             remove()
#     #         else:
#     #             remove()
#     # delay time
#     time.sleep(0.1)

# packages
import cv2
import numpy as np
import pyautogui as pg

# take a screenshot to locate objects on
screenshot = pg.screenshot()

# adjust colors
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

infomation_form = find_infomation_form()
print(infomation_form)
if infomation_form:
    cv2.rectangle(
    screenshot,
    (infomation_form.left, infomation_form.top),
    (infomation_form.left + infomation_form.width, infomation_form.top + infomation_form.height),
    (0, 0, 255),
    2
    )

patient_input = find_patient_input()
if patient_input:
    cv2.rectangle(
        screenshot,
        (patient_input.left, patient_input.top),
        (patient_input.left + patient_input.width, patient_input.top + patient_input.height),
        (0, 255, 0),
        2
    )

first_name_input = find_first_name_input()
if first_name_input:
    cv2.rectangle(
    screenshot,
    (first_name_input.left, first_name_input.top),
    (first_name_input.left + first_name_input.width, first_name_input.top + first_name_input.height),
    (255, 0, 0),
    2
    )

last_name_input = find_last_name_input()
if last_name_input:
    cv2.rectangle(
        screenshot,
        (last_name_input.left, last_name_input.top),
        (last_name_input.left + last_name_input.width, last_name_input.top + last_name_input.height),
        (255, 0, 255),
        2
    )


sex_input = find_sex_input()
if sex_input:
    cv2.rectangle(
        screenshot,
        (sex_input.left, sex_input.top),
        (sex_input.left + sex_input.width, sex_input.top + sex_input.height),
        (0, 255, 255),
        2
    )

birth_date_input = find_birth_date_input()
if birth_date_input:
    cv2.rectangle(
        screenshot,
        (birth_date_input.left, birth_date_input.top),
        (birth_date_input.left + birth_date_input.width, birth_date_input.top + birth_date_input.height),
        (255, 255, 0),
        2
    )

# display screenshot in a window
cv2.imshow('Screenshot', screenshot)

# escape condition
cv2.waitKey(0)

# clean up windows
cv2.destroyAllWindows()