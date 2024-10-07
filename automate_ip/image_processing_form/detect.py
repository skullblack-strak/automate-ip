import sys
import time
from automate_ip.infomation.file_info import read, remove
from automate_ip.image_processing_form.auto_complete import write_form
from automate_ip.image_processing_form.detect_form import detect_form

def run():
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


if __name__ == "__detect__":
    sys.exit(run())