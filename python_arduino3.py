
import serial
import csv
import os
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

fields = ["Date", "DHT22 temperature °C", "DHT22 humidity %", "DS18B20 temperature °C"] # Поля для заполнения таблицы в csv файле
if not os.path.isfile('Data_from_arduino.csv'): #Проверяем наличие файла csv: если его нет, то записываем шапку для таблицы
    with open('Data_from_arduino.csv', 'a', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fields)
            writer.writeheader()

i = 0
while i<288:
    for i in range(6):
        data_arduino.append(change_inlet_str(str(serial_arduino.readline())))
    #data_file = open('Data_from_arduino.txt', 'a')
    t = time.asctime()
    #data_file.write(t +'\n')
    print(t)
    for i in data_arduino:
        print(i)
        #data_file.write(i+'\n')
    #data_file.close()
    #print(data_arduino)
    for i in range(len(data_arduino)):
        data_arduino[i] = change_str_data_arduino(data_arduino[i])
    #print(data_arduino)
    data_dict.append({
        "Date": t, 
        "DHT22 temperature °C": data_arduino[1], 
        "DHT22 humidity %": data_arduino[2],
        "DS18B20 temperature °C": data_arduino[4],
        })
    with open('Data_from_arduino.csv', 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fields)
        writer.writerows(data_dict)
    #print (data_dict)
    data_dict = []
    data_arduino = []
    i += 1

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