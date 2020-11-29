# client code for inertial measurement unit reading and plotting
# Last mod by Karl Mueller, 11/14/2020 VER 1A

# VER1a Originated 11/14/2020:K_Mueller
#__ End STATE: Can socket into pi and obtain euler angle data. then plots over 50s time to visualize data.

import socket
import sys
import time
import math
import csv

import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation 
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
import numpy as np

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

#Read data from the socket and call the embedded command

#KARL< README... Initial version simple for either euler or quaternion. Make later versions tell the sensor or tell the code here what to outputr or accept resectively

phi = []
theta = []
psi = []

x = []
y = []
z = []
tt = []
tc = []
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

intt = 125
def animate(i):
    # byte_string.flush() ... is this format possible or even necessary
    global tt
    global phi
    global theta
    global psi
    global tc

    byte_string = s.recv(56).decode('utf-8')

    byte_string = byte_string.strip('(')
    byte_string = byte_string.strip(')')
    byte_string = byte_string.replace(' ', '')
    byte_string = byte_string.split(',')

    tt = time.time()

    try:
        phi.append(float(byte_string[0]))
        theta.append(float(byte_string[1]))
        psi.append(float(byte_string[2]))
        tc.append(tt)

        if len(phi)>200:
            phi = phi[-200:]
            theta = theta[-200:]
            psi = psi[-200:]
            tc = tc[-200:]
        #x = 
        #y = 
        #z = 
        #ax1.quiver(0, 0, 0, x, y, z, color='r')
        ax1.clear()
        ax1.plot(tc, phi)#, marker='o', color='red')
        ax1.plot(tc, theta)#, marker='o', color='blue')
        ax1.plot(tc, psi)#, marker='o', color='green')
        ax1.set(xlim=(tt-(200*intt/1000), tt), ylim=(-20, 20))
        plt.xlabel('Time(s)')
        plt.ylabel('Euler Angles (Degrees)')

    except:
        pass

ani = animation.FuncAnimation(fig, animate, interval=intt)

plt.draw()
plt.show()

with open('dat_out.csv','w',newline=' ') as csvfile:
    


