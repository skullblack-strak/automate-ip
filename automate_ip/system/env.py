import os
from dotenv.main import load_dotenv,find_dotenv,set_key
load_dotenv()

def set_env(key:str, val):
    dotenv_file = find_dotenv()
    load_dotenv(dotenv_file)
    os.environ[key] = val
    # Write changes to .env file.
    set_key(dotenv_file, key, os.environ[key])
    return os.environ[key]

def get_env(key:str):
    dotenv_file = find_dotenv()
    load_dotenv(dotenv_file)
    return os.environ[key]