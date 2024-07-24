import pyautogui
import pyperclip 
from automate_ip.image_processing_form.enum import Input, month_th_to_num
import win32clipboard as cb

# mold input list
class mold:
    def __init__(self, name, infomation_index, working_style, x, y):
        self.name = name
        self.infomation_index = infomation_index
        self.working_style = working_style
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

    # input_list_in_form.append(mold(Input.PATIENT_ID.value, 0, "write", 60, 60))
    input_list_in_form.append(mold(Input.FIRST_NAME.value, 38, "copy", 380, 150))
    input_list_in_form.append(mold(Input.LAST_NAME.value, 39, "copy", 60, 150))
    # input_list_in_form.append(mold(Input.MIDDLE_NAME.value, 4, "write", 220, 150))
    input_list_in_form.append(mold(Input.SEX.value, 37, "click", 150, 280))
    input_list_in_form.append(mold(Input.DATE_OF_BIRTH.value, 40, "write", 120, 320))
    # input_list_in_form.append(mold(Input.COMMENT.value, 5, "write", 0, 525))
    return input_list_in_form


def form(base_x:int, base_y:int, infomation:list[str]):
    input_list_in_form = setup_input_list()
    for input in input_list_in_form:
        pyautogui.click(base_x+input.x, base_y+input.y)
        text = infomation[input.infomation_index]
        if input.name == Input.DATE_OF_BIRTH.value:
            text = mapDateTHToDateNum(text)
        print("text", text)
        if input.name == Input.SEX.value:
            mapSex(text, base_x+input.x, base_y+input.y)
        else:
            if input.working_style == "write":
                writeText(text)
            else:
                copyPasteText(text)

def move_to(x:int, y:int):
    pyautogui.click(x, y)

def copyPasteText(text:str):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v", interval=0.05)

def writeText(text:str):
    pyautogui.typewrite(text, interval=0.05)
    pyautogui.write(text, interval=0.05)

def copy(s):
    cb.OpenClipboard()
    cb.EmptyClipboard()
    cb.SetClipboardData(cb.CF_UNICODETEXT, str(s))
    cb.CloseClipboard()

def mapSex(sex:str, sex_x:int, sex_y:int):
    if sex == "Miss" or sex == "Missis":
        pyautogui.click(sex_x, sex_y+65)
    else:
        pyautogui.click(sex_x, sex_y+48)

def mapDateTHToDateNum(date_th:str):
    print("date_th", date_th)
    [day,month_th,year] = date_th.split(' ')
    year_th = int(year) - 543
    return f'{month_th_to_num[month_th]}/{day}/{year_th}'
