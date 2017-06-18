from time import sleep
from requests import get
import serial

URL = "http://192.168.1.4"
INPUT_URL = URL+"/pir/add"

ser = serial.Serial('COM3', 115200) # Establish the connection on a specific port

while True:
    val = ser.readline().split(':') # Read the newest output from the Arduino
    if len(val) == 2:
        print "id = "+val[0]
        print "status = "+val[1]
        url = INPUT_URL+"?id="+val[0]+"?status="+val[1]
        r = get(url)
        print r.json()

    sleep(.1)