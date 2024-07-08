import pyautogui
import pyperclip 
from automate_ip.image_processing_form.enum import Input

# mold input list
class mold:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

def setup_input_list():
    # creating list
    input_list_in_form = []

    # appending instances to list 257 322
    # input_list_in_form.append(mold(Input.PATIENT_ID.value, 80, 0))
    # input_list_in_form.append(mold(Input.FIRST_NAME.value, 400, 90))
    # input_list_in_form.append(mold(Input.LAST_NAME.value, 80, 90))
    # input_list_in_form.append(mold(Input.MIDDLE_NAME.value, 230, 90))
    # # input_list_in_form.append(mold(Input.SEX.value, 150, 220))
    # input_list_in_form.append(mold(Input.DATE_OF_BIRTH.value, 150, 255))
    # input_list_in_form.append(mold(Input.COMMENT.value, 257, 468))

    input_list_in_form.append(mold(Input.PATIENT_ID.value, 60, 60))
    input_list_in_form.append(mold(Input.FIRST_NAME.value, 380, 150))
    input_list_in_form.append(mold(Input.LAST_NAME.value, 60, 150))
    input_list_in_form.append(mold(Input.MIDDLE_NAME.value, 220, 150))
    # input_list_in_form.append(mold(Input.SEX.value, 150, 220))
    input_list_in_form.append(mold(Input.DATE_OF_BIRTH.value, 120, 320))
    input_list_in_form.append(mold(Input.COMMENT.value, 0, 525))
    return input_list_in_form


def form(x:int, y:int, infomation:list[str]):
    input_list_in_form = setup_input_list()
    for id_list, info in enumerate(infomation):
        pyautogui.click(x+input_list_in_form[id_list].x, y+input_list_in_form[id_list].y)
        text = infomation[id_list]
        pyperclip.copy(text)
        print("text",text)
        pyautogui.hotkey("ctrl", "v")

def move_to(x:int, y:int):
    pyautogui.click(x, y)
