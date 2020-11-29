# client code for inertial measurement unit reading and plotting
# Last mod by Karl Mueller, 11/17/2020 VER 2a

# VER1a Originated 11/14/2020:K_Mueller
#__ End STATE: Can socket into pi and obtain euler angle data. then plots over 50s time to visualize data.
# VER2a: Created on 11/17/2020: K_Mueller
# Integrated a more flexible method of requesitng specific data type from the server, more robust.
# There is 0 data loss in this version and it saves to csv for analysis

import socket
import sys
import time
import math
import csv
import numpy as np

header_len = 4
refresh_rate = 50 #ignore until server changes are made, this changes nothing currently

b_time = time.time()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #predefine client socket

server_ip = '192.168.0.161' #IP ADDR of the raspberry pi sensor
port = 35196 #port number, ensure >4 digits and an int

# Connect to the bound server socket to read data
try:
    s.connect((server_ip, port))
    print(f'Connection with sensor at {server_ip}:{port} established')
except:
    sys.exit('Connection not established. Check power, port number, and IP ADDR and try again')

#send server proper type of data requested 1)euler, 2)quat, 3)acc, 4)lin_acc, 5)grav
data_type = 4
s.send(bytes(str(data_type),'utf-8')) #send data to server

#predefine state variable x to allow for state data storage
if data_type == 2:
    x = np.array([0, 0, 0, 0, 0])
else:
    x = np.array([0, 0, 0, 0])

c_time = []

line_iterator = 0
#while True:
for loop_iteration in range(50000):
    line_iterator += 1
    dat_length = int(s.recv(header_len).decode('utf-8'))
    byte_string = s.recv(dat_length).decode('utf-8')

    #Parse incoming string data, will automatically form  
    byte_string = byte_string.strip('(')
    byte_string = byte_string.strip(')')
    byte_string = byte_string.replace(' ', '')
    byte_string = byte_string.split(',')

    #print(f'{byte_string}')

    data_ray = np.array([time.time()])
    byte_ray = np.array(byte_string, dtype=float)

    data_ray = np.hstack((data_ray, byte_ray))
    x = np.vstack((x, data_ray))

    #don't add a wait/sleep statement here, this will run as soon as ready
    #added wait statement will cause additional, stacking lag on data stream

np.savetxt('50kfanless_11_23_2020.csv', x, delimiter=',', fmt='%15f')