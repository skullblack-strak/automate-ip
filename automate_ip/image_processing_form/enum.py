from enum import Enum

class Input(Enum):
    PATIENT_ID = "patient_id"
    LAST_NAME = "last_name"
    MIDDLE_NAME = "middle_name"
    FIRST_NAME = "first_name"
    SEX = "sex"
    DATE_OF_BIRTH = "date_of_birth"
    COMMENT = "comment"

class Environment(Enum):
    SYSTEM_SECRET="SYSTEM_SECRET"
    INFOMATION_BASE_PATH="INFOMATION_BASE_PATH"
    INFOMATION_FILE_NAME="INFOMATION_FILE_NAME"