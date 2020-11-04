

#!/usr/bin/env python3
import serial
import time
import requests
import math
import random
import json

TOKEN = "BBFF-afE7LF7xTEqvIwtQy49OGDgqr28g3u"
DEVICE_LABEL="raspberry"

def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
#temperatura, ph, condutividade e luminosidade
    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def main():
    try:
        line = ser.readline()
        line = line[:-1]
        print(line)
        payload = json.loads(line)
        print("[INFO] Attemping to send data")
        post_request(payload)
        print("[INFO] finished")
    except:
        pass
        print("[INFO] Error on post")


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    time.sleep(3)
    while (True):
        main()
        time.sleep(8)
        ser.flush()
