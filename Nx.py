import os, platform
try:
   import requests
except:
   os.system('pip2 install requests')
 
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from nx import __start__
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    __start__()
elif bit == '32bit':
    from nx import __start__
    print("\n Your device is not supported!\n")
    time.sleep(10)
    __start__()
 
