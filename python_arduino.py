
import serial

import time

#time.clock - secondmeter

serial_arduino = serial.Serial('COM16', 9600)
message = ''
degree = chr(176)
while True:
    for i in range(6):
        message += str(serial_arduino.readline())
    message=message.replace('b','')
    message=message.replace('\\n','\n')
    message=message.replace('\\r','')
    message=message.replace('\'','')
    message=message.replace('\\x0',degree)
    data_file = open('Data_from_arduino.txt', 'a')
    data_file.write(time.asctime()+'\n')
    data_file.write(message)
    data_file.close()

    print(time.asctime())
    print(message)
    message = ''


