import time
from automate_ip.infomation.file_info import read, remove
from automate_ip.image_processing_form.auto_complete import form, write_form
# from automate_ip.image_processing_form.image_processing import find_image_position

# while True:
#     centerPositionImage = find_image_position()
#     if centerPositionImage:
#          # read infomation file
#         infomation = read()
#         if not (infomation is None):
#             if len(infomation):
#                 # auto complete from
#                 form(centerPositionImage.x, centerPositionImage.y, infomation)
#                 # remove infomation
#                 remove()
#             else:
#                 remove()
#     # delay time
#     time.sleep(0.1)

from automate_ip.image_processing_form.detect_form import detect_form

while True:
    continue_loop = False
    center_position_input = detect_form()
    if center_position_input["infomation_form"]:
        for input_val in center_position_input.values():
            print("input", input_val)
            if input_val is None:
                print("The form is not ready.")
                continue_loop = True
                break
        if continue_loop: continue
         # read infomation file
        infomation = read()
        if not (infomation is None):
            if len(infomation):
                write_form(center_position_input, infomation)
                # remove infomation
                remove()
            else:
                remove()
        else:
            print("infomation data not found")
    else:
        print("infomation form not found")
    # delay time
    time.sleep(0.1)