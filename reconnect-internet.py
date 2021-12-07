# Replace the name of interface

import urllib.request
import time
import os
import datetime

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def enable():
    os.system('netsh interface set interface name="Name of Interface" admin=ENABLED')

def disable():
    os.system('netsh interface set interface name="Name of Interface" admin=DISABLED')

print("Internet Reconnect is running.")
while True:
    time.sleep(60)
    if (not connect()):
        dt = datetime.datetime.now()
        print(str(dt) + " - Internet is restarting.")
        disable()
        enable()
    else:
        print("Internet is online.")