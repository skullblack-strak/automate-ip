import automate_ip.image_processing_form.detect_form as detect_form
import re
import sys
sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
# from automate_ip.image_processing_form.image_processing import find_image_position, find_image_position_test
# from automate_ip.image_processing_form.auto_complete import move_to

# from automate_ip.infomation.file_info import read

def run():
    detect_form
    # print(read() is not None)
    # print(find_image_position())
    print("end")