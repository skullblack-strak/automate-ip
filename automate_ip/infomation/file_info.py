import os
from automate_ip.system.env import get_env
from automate_ip.image_processing_form.enum import Environment

def read():
    try:
        # Variables with environment
        base_path = get_env(Environment.INFOMATION_BASE_PATH.value)
        file_name = get_env(Environment.INFOMATION_FILE_NAME.value)

        # Using os.path.join() 
        file_path = os.path.join(base_path, file_name) 
        with open(file_path, "r", encoding="utf-8") as file:
            text_file = file.read()
            if is_not_blank(text_file):
                # print("Files in here:", os.listdir("."))
                return text_file.split(',')
            else:
                return []
    except:
        return
    
def remove():
    try:
        # Variables with environment
        base_path = get_env(Environment.INFOMATION_BASE_PATH.value)
        file_name = get_env(Environment.INFOMATION_FILE_NAME.value)

        # Using os.path.join() 
        file_path = os.path.join(base_path, file_name) 
        os.remove(file_path)
    except:
        return

def is_not_blank(s:str):
    return bool(s and not s.isspace())