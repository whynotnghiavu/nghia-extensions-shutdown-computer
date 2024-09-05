import os
import time


def shutdown_computer():
    if os.name == 'nt':
        os.system('shutdown /s /t 15')
    elif os.name == 'posix':
        time.sleep(15)
        os.system('shutdown now')
    else:
        print("Không thể tắt máy tự động trên hệ điều hành này.")


shutdown_computer()
