# client code for inertial measurement unit reading and plotting
# Last mod by Karl Mueller, 11/17/2020 VER 2a

# VER1a Originated 11/14/2020:K_Mueller
#__ End STATE: Can socket into pi and obtain euler angle data. then plots over 50s time to visualize data.
# VER2a: Created on 11/17/2020: K_Mueller
# Integrated a more flexible method of requesitng specific data type from the server, more robust.
# There is 0 data loss in this version and it saves to csv for analysis
# VER3a: Created on 12/12/2020: K_Mueller
#Code altered into the form of a function, now called clinet_fx.py. this is intended for use in the
#GUI-centric format and a code-block form to allow for better insertion of cuntions into a main script

import socket
import sys
import time
import numpy as np
import threading
import queue

class client_fx(object):
    def __init__(self, server_ip, port, **kwargs):

        self.header_len = 4
        self.refresh_rate = 50  # not yet handled for
        self.b_time = time.time()
        # predefine client socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server_ip = server_ip  # IP ADDR of the raspberry pi sensor
        self.port = port  # port number, ensure > 4 digits and an int

        try:  # Connect to the bound server socket to read data
            self.s.connect((self.server_ip, self.port))
            print(f'Connection with sensor at {self.server_ip}:{self.port} established')
        except:
            sys.exit(
                'Connection not established. Check power, port number, and IP ADDR and try again')

        #send server proper type of data requested 1)euler, 2)quat, 3)acc, 4)lin_acc, 5)grav
        self.data_type = 2
        self.s.send(bytes(str(self.data_type), 'utf-8'))  # send data to server

        self.dq = queue.LifoQueue(1)
        imu_thread = threading.Thread(target=self.run)
        imu_thread.start()

        #print_imu_dat = threading.Thread(target=self.ticker)
        #print_imu_dat.start()


    def run(self):
        while True:
            self.c_time = []

            self.dat_length = int(self.s.recv(self.header_len).decode('utf-8'))
            self.byte_string = self.s.recv(self.dat_length).decode('utf-8')

            self.byte_string = self.byte_string.strip('(')
            self.byte_string = self.byte_string.strip(')')
            self.byte_string = self.byte_string.replace(' ', '')
            self.byte_string = self.byte_string.split(',')
            self.data_ray = np.array([time.time()])
            self.byte_ray = np.array(self.byte_string, dtype=float)
            self.data_ray = np.hstack((self.data_ray, self.byte_ray))
            
            self.dq.put(self.data_ray) #assign current value to stream

    def ticker(self):
        while True:
            print(self.dq.get())
