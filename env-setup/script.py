import os
import re
import pyautogui
from dotenv.main import load_dotenv,find_dotenv,set_key
information_path =  pyautogui.prompt(text='', title='ที่อยู่ไฟล์บัตรประชาชน' , default='')
information_file =  pyautogui.prompt(text='', title='ชื่อไฟล์บัตรประชาชน' , default='')
path = re.sub(r'(\\)', '/', information_path)

def set_env(key:str, val):
    dotenv_file = find_dotenv()
    load_dotenv(dotenv_file)
    os.environ[key] = val
    set_key(dotenv_file, key, os.environ[key])
    return os.environ[key]

def get_env(key:str):
    dotenv_file = find_dotenv()
    load_dotenv(dotenv_file)
    return os.environ[key]

env_file = '../.env'

# Check if the .env file exists
if not os.path.exists(env_file):
    # Create the .env file and write default content
    with open(env_file, 'w') as f:
        f.write(f"INFOMATION_BASE_PATH='{path}'\n")
        f.write(f"INFOMATION_FILE_NAME='{information_file}'\n")
else:
    set_env("INFOMATION_BASE_PATH",path)
    set_env("INFOMATION_FILE_NAME",information_file)