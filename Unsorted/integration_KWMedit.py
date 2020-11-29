import socket
import sys
import time
import math

import matplotlib.pyplot as plt
from scipy import integrate as it
from matplotlib import style
import matplotlib.animation as animation 
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
import numpy as np

x = []
y = []
z = []
velocity_x = [0]
velocity_y = [0]
velocity_z = [0]
location_x = [0]
location_y = [0]
location_z = [0]
tt = []
tc = []
style.use('fivethirtyeight')

fig1 = plt.figure()
fig2 = plt.figure()
#fig3,[ax5,ax6,ax7] = plt.subplots(3,1,sharex=True,sharey=True)
ax1 = fig1.gca(projection='3d')
ax2 = fig2.add_subplot(1, 3, 1)
ax3 = fig2.add_subplot(1, 3, 2)
ax4 = fig2.add_subplot(1, 3, 3)

x.append(float(byte_string[0]))
y.append(float(byte_string[1]))
z.append(float(byte_string[2]))
tc.append(tt)
vx = it.trapz(x[-2:],tc[-2:])
velocity_x.append(vx)
lx = it.trapz(velocity_x[-2:],tc[-2:])
lx = location_x[-1]+lx
location_x.append(lx)
vy = it.trapz(y[-2:],tc[-2:])
velocity_y.append(vy)
ly = it.trapz(velocity_y[-2:],tc[-2:])
ly = location_y[-1]+ly
location_y.append(ly)
vz = it.trapz(z[-2:],tc[-2:])
velocity_z.append(vz)
lz = it.trapz(velocity_z[-2:],tc[-2:])
lz = location_z[-1]+lz
location_z.append(lz)



ax1.clear()
ax1.plot3D(location_x,location_y,location_z,c='red',marker="o")
ax1.set_xlabel('X position (m)')
ax1.set_ylabel('Y position (m)')
ax1.set_zlabel('Z position (m)')
ax1.set_xlim3d([-2, 2])
ax1.set_ylim3d([-2, 2])
ax1.set_zlim3d([-2, 2])
ax1.set_autoscale_on(False)

ax2.plot(tc,location_x,c='blue',marker='o')
ax2.set_xlabel('Time (sec)')
ax2.set_ylabel('X Position (m)')
ax2.set(xlim=(tt-(50*intt/1000), tt), ylim=(-2, 2))

ax3.plot(tc,location_y,c='green',marker='o')
ax3.set_xlabel('Time (sec)')
ax3.set_ylabel('Y Position (m)')
ax3.set(xlim=(tt-(50*intt/1000), tt), ylim=(-2, 2))

ax4.plot(tc,location_z,c='orange',marker='o')
ax4.set_xlabel('Time (sec)')
ax4.set_ylabel('Z Position (m)')
ax4.set(xlim=(tt-(50*intt/1000), tt), ylim=(-2, 2))
