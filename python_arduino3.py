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

def change_str_data_arduino(curr_str):
    del_tuple = ('Temperature','Humidity',' ','°C','=','%')
    for i in del_tuple:
          curr_str = curr_str.replace(i,'')
    return curr_str

data_arduino = []
data_dict = []

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
    for i in range(len(data_arduino)):
        data_arduino[i] = change_str_data_arduino(data_arduino[i])
    #print(data_arduino)
    data_dict.append({
        "Date": t, 
        "DHT22_temperature, °C":data_arduino[1], 
        "DHT22_Humidity, %":data_arduino[2],
        "DS18B20_temperature, °C":data_arduino[4],
        })
    #print (data_dict)
    data_arduino = []

# def change_datalist(curr_str):
#     del_tuple = ('Temperature','Humidity',' ','°C','=','%')
#     for i in del_tuple:
#           curr_str = curr_str.replace(i,'')
#     return curr_str
# s = "Temperature = 22.50 °C"
# s = change_in_str(s)
# print(float(s))

# data = [{'Date': 'Wed Oct 18 13:40:39 2023', 'DHT22_temperature, °C': '22.20', 'DHT22_Humidity, %': '30.60', 'DS18B20_temperature, °C': '-127.00'}, 
# {'Date': 'Wed Oct 18 13:40:44 2023', 'DHT22_temperature, °C': '22.20', 'DHT22_Humidity, %': '30.50', 'DS18B20_temperature, °C': '-127.00'},
# {'Date': 'Wed Oct 18 13:40:49 2023', 'DHT22_temperature, °C': '22.20', 'DHT22_Humidity, %': '30.40', 'DS18B20_temperature, °C': '-127.00'}, 
# {'Date': 'Wed Oct 18 13:40:54 2023', 'DHT22_temperature, °C': '22.20', 'DHT22_Humidity, %': '30.20', 'DS18B20_temperature, °C': '-127.00'}]

# print(data[3])