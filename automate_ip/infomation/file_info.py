import os
from automate_ip.system.env import get_env
from automate_ip.image_processing_form.enum import Environment

def read():
    try:
        # Variables with environment
        base_path = get_env(Environment.INFOMATION_BASE_PATH.value)
        file_name = get_env(Environment.INFOMATION_FILE_NAME.value)

        # Using os.path.join() 
        file_path = os.path.normpath(os.path.join(base_path, file_name))
        with open(file_path, "r", encoding="utf-8") as file:
            text_file = file.read()
            if is_not_blank(text_file):
                return text_file.split(',')
            else:
                return []
    except:
        return
    
def remove():
    try:
        base_path = get_env(Environment.INFOMATION_BASE_PATH.value)
        for filename in os.listdir(base_path):
            file_path = os.path.join(base_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
    except:
        return

def is_not_blank(s:str):
    return bool(s and not s.isspace())
