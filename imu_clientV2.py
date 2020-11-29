# client code for inertial measurement unit reading and plotting
# Last mod by Karl Mueller, 11/14/2020 VER 1A

# VER1a Originated 11/14/2020:K_Mueller
#__ End STATE: Can socket into pi and obtain euler angle data. then plots over 50s time to visualize data.

import socket
import sys
import time
import math

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

intt = 75
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
    #byte_string = byte_string.replace('\r', '')
    byte_string = byte_string.split(',')

    tt = time.time()

    try:
        '''
        psi.append(float(byte_string[0]))
        phi.append(float(byte_string[1]))
        theta.append(float(byte_string[2]))
        tc.append(tt)

        if len(phi)>200: #slice data to 200 most current points
            phi = phi[-200:]
            theta = theta[-200:]
            psi = psi[-200:]
            tc = tc[-200:]
        '''

        psi = float(byte_string[0])*np.pi/60
        phi = float(byte_string[1])*np.pi/60
        theta = float(byte_string[2])*np.pi/60

        v0 = np.array([[0, 0, 0],
            [0, 0, 0],
            [0, 0, 1]])
        '''
        with np:
            RR = array([[cos(theta)*cos(psi), sin(phi)*sin(theta)*cos(psi)-cos(phi)*sin(psi), cos(phi)*sin(theta)*cos(psi)+sin(psi)],
                [cos(theta)*sin(psi), sin(phi)*sin(theta)*sin(psi)+cos(phi)*cos(psi), cos(phi)*sin(theta)*sin(psi)-sin(phi)*cos(psi)],
                [-sin(theta), sin(phi)*cos(theta), cos(phi)*cos(theta)]])

        v1 = RR*v0

        print(f'{v1}')

        x = v1[2][0]
        y = v1[2][1]
        z = v1[2][2]
        '''
        ax1.clear()
        ax1.quiver(0, 0, 0, x, y, z, color='r')
        



        '''
        ax1.plot(tc, phi)#, marker='o', color='red')
        ax1.plot(tc, theta)#, marker='o', color='blue')
        ax1.plot(tc, psi)#, marker='o', color='green')
        ax1.set(xlim=(tt-(200*intt/1000), tt), ylim=(-180, 360))
        '''


    except:
        pass

ani = animation.FuncAnimation(fig, animate, interval=intt)

plt.xlabel('Time(s)')
plt.ylabel('Euler Angles (Degrees)')
plt.draw()
plt.show()
