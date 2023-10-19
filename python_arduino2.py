import serial

import time

#time.clock - secondmeter

serial_arduino = serial.Serial('COM16', 9600)
degree = chr(176)

def change_inlet_str(curr_str):
    del_tuple = ('b','\\n','\\r','\'','\\x0')
    for i in del_tuple:
        if i != '\\x0':
            curr_str = curr_str.replace(i,'') 
        else:
            curr_str = curr_str.replace(i,degree) 
    return curr_str

data_arduino = []

while True:
    for i in range(6):
        data_arduino.append(change_inlet_str(str(serial_arduino.readline())))
    data_file = open('Data_from_arduino.txt', 'a')
    t = time.asctime()
    data_file.write(t +'\n')
    print(t)
    for i in data_arduino:
        print(i)
        data_file.write(i+'\n')
    data_file.close()
    #print(data_arduino)
    data_arduino = []



# degree = chr(176)
# row = "asc\nyujb\\x0\n123\\r"
# def change_in_str(curr_str):
#     curr_str = curr_str.replace('b','')
#     curr_str = curr_str.replace('\\n','\n')
#     curr_str = curr_str.replace('\\r','')
#     curr_str = curr_str.replace('\'','')
#     curr_str = curr_str.replace('\\x0',degree)
#     return curr_str
# print(row)
# print()
# row = change_in_str(row)
# print(row)