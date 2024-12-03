import serial
import requests
import random, time

flag = False
# config COM port
while(1):
    time.sleep(0.1)
    portName = input("Enter the port name:")
    if portName == "test":
       flag = True
       break
    try:
        # config COM port section
        ser = serial.Serial(
            port=portName,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0
        )
        break
    except:
       # Disconnected or port name Invaild
       print("Invaild Value")


while(1):
    time.sleep(0.1)
    if flag: 
        try:
            data = {'value': random.random()*100}
            print(requests.post("http://localhost:8000/sensor/setTemp", data).json())
        except:
            print("Could not connect Web Server")
        time.sleep(0.5)
        continue

    if ser.readable():
        smo = ser.readline()
        if not smo:
            continue
        print(smo)
        msg = smo.decode()[:len(smo)-1].split(" : ")
        cmd = msg[0]
        print(msg)
        try:
            data = {'value' : float(msg[1])}
        except:
            print("Invaild Value")
            continue

        if cmd not in ['Temp','Humi','Vib','Prox']:
            print("Invaild Command")
            continue
        try:
            requests.post("http://localhost:8000/sensor/set" + cmd, data = data)
        except:
            print("Invaild Command")