import cv2
import numpy as np
import pyautogui as pg
from automate_ip.image_processing_form.enum import Input
from automate_ip.image_processing_form.image_processing import find_infomation_form, find_patient_input, find_name_input_group, find_first_name_input, find_last_name_input, find_sex_input, find_birth_date_input

def detect_infomation_form(screenshot: cv2.typing.MatLike, drew: bool = False):
    infomation_form = find_infomation_form()
    if infomation_form and drew:
        rectangle_infomation_form = cv2.rectangle(
            screenshot,
            (infomation_form.left, infomation_form.top),
            (infomation_form.left + infomation_form.width, infomation_form.top + infomation_form.height),
            (0, 0, 255),
            2
        )
        cv2.putText(rectangle_infomation_form, 'Infomation Form', (infomation_form.left, infomation_form.top-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    if infomation_form: 
        return pg.center(infomation_form)

def detect_patient(screenshot: cv2.typing.MatLike, drew: bool = False):
    patient_input = find_patient_input()
    if patient_input and drew:
        rectangle_patient_input = cv2.rectangle(
            screenshot,
            (patient_input.left, patient_input.top),
            (patient_input.left + patient_input.width, patient_input.top + patient_input.height),
            (0, 255, 0),
            2
        )
        cv2.putText(rectangle_patient_input, 'Patient', (patient_input.left, patient_input.top-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.circle(rectangle_patient_input, (pg.center(patient_input)), radius=0, color=(0, 255, 0), thickness=4)
    if patient_input: 
        return pg.center(patient_input)

def detect_input_group(screenshot: cv2.typing.MatLike, drew: bool = False) -> dict[str, pg.Point]:
    padding: int = 2
    name_input_group = find_name_input_group()
    if not name_input_group: 
        return dict({Input.FIRST_NAME.value:None,Input.LAST_NAME.value:None})
    last_name_input = find_last_name_input(region=(
        name_input_group.left + int(name_input_group.width / 2) + padding, 
        name_input_group.top + padding, 
        name_input_group.left + int(name_input_group.width/2) - padding, 
        name_input_group.top + name_input_group.height - padding))
    first_name_input = find_first_name_input(region=(
        name_input_group.left + padding, 
        name_input_group.top + padding, 
        name_input_group.left + int(name_input_group.width/2) - padding, 
        name_input_group.top + name_input_group.height - padding))
    if name_input_group and drew:
        rectangle_name_input_group = cv2.rectangle(
            screenshot,
            (name_input_group.left, name_input_group.top),
            (name_input_group.left + name_input_group.width, name_input_group.top + name_input_group.height),
            (255, 0, 0),
            2
        )
        cv2.putText(rectangle_name_input_group, 'Name Group', (name_input_group.left, name_input_group.top-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        rectangle_first_name = cv2.rectangle(
            screenshot,
            (first_name_input.left, first_name_input.top),
            (first_name_input.left + first_name_input.width, first_name_input.top + first_name_input.height),
            (255, 0, 255),
            2
        )
        cv2.putText(rectangle_first_name, 'First Name', (first_name_input.left, first_name_input.top-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
        cv2.circle(rectangle_first_name, (pg.center(first_name_input)), radius=0, color=(255, 0, 255), thickness=4)

        rectangle_last_name = cv2.rectangle(
            screenshot,
            (last_name_input.left + padding, last_name_input.top + padding),
            (last_name_input.left + last_name_input.width, last_name_input.top + last_name_input.height),
            (255, 0, 255),
            2
        )
        cv2.putText(rectangle_last_name, 'last Name', (last_name_input.left, last_name_input.top-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
        cv2.circle(rectangle_last_name, (pg.center(last_name_input)), radius=0, color=(255, 0, 255), thickness=4)
    d = dict({Input.FIRST_NAME.value:None,Input.LAST_NAME.value:None})
    if first_name_input: d[Input.FIRST_NAME.value] = pg.center(first_name_input)
    if last_name_input: d[Input.LAST_NAME.value] = pg.center(last_name_input)
    return d

def detect_sex(screenshot: cv2.typing.MatLike, drew: bool = False):
    sex_input = find_sex_input()
    if sex_input and drew:
        rectangle_sex_input = cv2.rectangle(
            screenshot,
            (sex_input.left, sex_input.top),
            (sex_input.left + sex_input.width, sex_input.top + sex_input.height),
            (0, 255, 255),
            2
        )
        cv2.putText(rectangle_sex_input, 'Sex', (sex_input.left, sex_input.top-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
        cv2.circle(rectangle_sex_input, (pg.center(sex_input)), radius=0, color=(0, 255, 255), thickness=4)
    if sex_input:
        return pg.center(sex_input)


def detect_birth_date(screenshot: cv2.typing.MatLike, drew: bool = False):
    birth_date_input = find_birth_date_input()
    if birth_date_input and drew:
        rectangle_birth_date_input = cv2.rectangle(
            screenshot,
            (birth_date_input.left, birth_date_input.top),
            (birth_date_input.left + birth_date_input.width, birth_date_input.top + birth_date_input.height),
            (255, 255, 0),
            2
        )
        cv2.putText(rectangle_birth_date_input, 'Birth Date', (birth_date_input.left, birth_date_input.top-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
        cv2.circle(rectangle_birth_date_input, (pg.center(birth_date_input)), radius=0, color=(0, 0, 255), thickness=4)
    if birth_date_input:
        return pg.center(birth_date_input)




def test_detect_form():
    # take a screenshot to locate objects on
    screenshot = pg.screenshot()

    # adjust colors
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # detect function
    detect_infomation_form(screenshot, True)
    detect_patient(screenshot, True)
    detect_input_group(screenshot, True)
    detect_sex(screenshot, True)
    detect_birth_date(screenshot, True)

    # display screenshot in a window
    cv2.imshow('Screenshot', screenshot)

    # escape condition
    cv2.waitKey(0)

    # clean up windows
    cv2.destroyAllWindows()


def detect_form():
    # take a screenshot to locate objects on
    screenshot = pg.screenshot()

    # adjust colors
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # detect function
    infomation_form = detect_infomation_form(screenshot)
    patient = detect_patient(screenshot)
    input_group = detect_input_group(screenshot)
    sex = detect_sex(screenshot)
    birth_date =detect_birth_date(screenshot)

    # escape condition
    cv2.waitKey(0)

    # clean up windows
    cv2.destroyAllWindows()

    return dict({
        Input.INFOMATION_FORM.value: infomation_form,
        Input.PATIENT_ID.value: patient,
        Input.FIRST_NAME.value: input_group[Input.FIRST_NAME.value],
        Input.LAST_NAME.value: input_group[Input.LAST_NAME.value],
        Input.SEX.value: sex,
        Input.DATE_OF_BIRTH.value: birth_date
    })
