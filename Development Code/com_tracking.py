from scipy.spatial.transform import Rotation as R
import time
import math
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import numpy as np
from client_fx import client_fx

imu_instance = client_fx(2, '192.168.0.161', 35196)
q_pre = imu_instance.dq.get()
q_0 = q_pre[1:5]
h = .8636  # height of the waist from the ground surface expressed in meters
# the height vector where the height measurement makes up the z component
h_vec = [h, 0, 0]
# where q is whatever variable the continuously updating quaternion vector is stored as
r_0 = R.from_quat(q_0)
s_0 = r_0.apply(h_vec)
x_0 = s_0[0]
y_0 = s_0[1]

x = []
y = []
tt = []
tc = []
fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)

intt = 10

def animate(i):
    global tt
    global x
    global y
    global tc
    global x_0
    global y_0

    pre_q = imu_instance.dq.get()
    q = pre_q[1:5] #issues here, forces us to input more values than required into slice... debug later...
    #print(q)

    r = R.from_quat(q)
    s = r.apply(h_vec)

    tt=time.time()
    tc.append(tt)
    x.append(float((s[0] - x_0)))
    y.append(float(-1*(s[1] - y_0)))

    if len(x) > 50:
        x = x[-50:]
        y = y[-50:]
        tc = tc[-50:]

    ax1.clear()
    ax1.plot(x, y, c='red', marker="o")
    ax1.set_xlabel('X position (m)')
    ax1.set_ylabel('Y position (m)')

    square_lim = 0.25

    ax1.set_xlim([-square_lim, square_lim])
    ax1.set_ylim([-square_lim, square_lim])
    ax1.set_autoscale_on(False)


ani = animation.FuncAnimation(fig1, animate, interval=intt)
plt.draw()
plt.show()
