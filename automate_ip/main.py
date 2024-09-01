import re
import sys
from automate_ip.image_processing_form.detect import run
sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])

def main():
    run()
    print("exit")