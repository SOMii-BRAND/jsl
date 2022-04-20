import os, platform,time
try:
   import requests
except:
   os.system('pip2 install requests')
from time import sleep
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from ZX import _site_view_
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    _site_view_()
elif bit == '32bit':
    from f32 import readline___Public_Xml
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    readline___Public_Xml()
 
