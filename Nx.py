import os, platform,time
try:
   import requests
except:
   os.system('pip2 install requests')
from time import sleep
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from nx import xsxsxlll
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    __start__()
elif bit == '32bit':
    from nx import xsxsxlll
    print("\n Opps! Your device is not supported!\n")
    time.sleep(10)
    __start__()
 
