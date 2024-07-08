import time
from automate_ip.infomation.file_info import read, remove
from automate_ip.image_processing_form.auto_complete import form
from automate_ip.image_processing_form.image_processing import find_image_position

while True:
    centerPositionImage = find_image_position()
    if centerPositionImage:
         # read infomation file
        infomation = read()
        if not (infomation is None):
            if len(infomation):
                # auto complete from
                form(centerPositionImage.x, centerPositionImage.y, infomation)
                # remove infomation
                remove()
            else:
                remove()
    # delay time
    time.sleep(0.1)