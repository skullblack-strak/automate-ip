import re
import sys
from .image_processing_form.detect import run
from windows_toasts import Toast, WindowsToaster
sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])

def show_toast():
    toaster = WindowsToaster('AutomateIP')
    newToast = Toast()
    newToast.text_fields = ['running autocomplete NAVIS-EX form']
    toaster.show_toast(newToast)

def main():
    show_toast()
    run()
    print("exit")
