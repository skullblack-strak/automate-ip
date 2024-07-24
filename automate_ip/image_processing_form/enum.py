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

month_en = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

month_th = [
    "มกราคม",
    "กุมภาพันธ์",
    "มีนาคม",
    "เมษายน",
    "พฤษภาคม",
    "มิถุนายน",
    "กรกฎาคม",
    "สิงหาคม",
    "กันยายน",
    "ตุลาคม",
    "พฤศจิกายน",
    "ธันวาคม"]

month_th_to_num = {
    month_th[0]:"01",
    month_th[1]:"02",
    month_th[2]:"03",
    month_th[3]:"04",
    month_th[4]:"05",
    month_th[5]:"06",
    month_th[6]:"07",
    month_th[7]:"08",
    month_th[8]:"09",
    month_th[9]:"10",
    month_th[10]:"11",
    month_th[11]:"12"}
