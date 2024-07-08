import pyscreeze
# import os

# print("Working dir:", os.getcwd())
# print("Files in here:", os.listdir("."))

def find_image_position():
    try:
        centerPositionImage = pyscreeze.locateCenterOnScreen('assets/image/title-new-infomation.png',confidence=0.9)
        print("success")
        return centerPositionImage
    except:
        print("catch")
        return
    
def find_image_position_test():
    try:
        centerPositionImage = pyscreeze.locateCenterOnScreen('assets/image/title-new-infomation.png',confidence=0.9)
        return centerPositionImage
    except:
        return


