from scipy.fft import fft, ifft, fftfreq
import pandas as pd
import scipy.signal as sig
from scipy.signal import butter, lfilter
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as it

##_________________________________
ff = np.genfromtxt('50kfanless_11_23_2020.csv', delimiter=',', dtype=float)  # dataset contains no fan noise

#ff = np.genfromtxt('rate_testing.csv', delimiter=',', dtype=float) #dataset contains fan noise
ff = ff[1:, :]
fx = ff[:, 1]
fy = ff[:, 2]
fz = ff[:, 3]

'''
rfx = np.zeros([len(fx)-4,1])
rfy = np.zeros([len(fx)-4, 1])
rfz = np.zeros([len(fx)-4, 1])
'''

fya = np.average(fy)
fy = fy - fya

fza = np.average(fz)
fz = fz - fza

'''
for ll in range(len(fx)-6):
    rfx[ll+2] = np.average(np.array([fx[ll-2], fx[ll-1], fx[ll], fx[ll+1], fx[ll+2]]))
    rfy[ll+2] = np.average(np.array([fy[ll-2], fy[ll-1],fy[ll], fy[ll+1], fy[ll+2]]))
    rfz[ll+2] = np.average(np.array([fz[ll-2], fz[ll-1], fz[ll], fz[ll+1], fz[ll+2]]))

fx = rfx
fy = rfx
fz = rfz
'''

ff_acc = np.sqrt(np.square(ff[:, 1])+np.square(ff[:, 2])+np.square(ff[:, 3]))

time_vec = ff[:, 0]
N = len(fx)  # number of samples in the dataset

##_________________________________
sample_rate = 100  # sampling frequency in Hz
nyq = sample_rate/2  # effective nyquist frequency, half of sampling rate
T = 1/sample_rate
tt = np.linspace(0, N/sample_rate, N, endpoint=False)

##_________________________________
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5*fs
    low = lowcut/nyq
    high = highcut/nyq
    b, a = butter(order, [low, high], btype='band', analog=False)
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

##_________________________________
#Filter data and replot to view

#### USER DEFINED
low_cutoff = 0.05
hi_cutoff = 35
###==============

'''
fig1 = plt.figure(1)
ax1 = fig1.add_subplot(1, 1, 1)
ax1.plot(tt, ff_acc, c='b')
plt.title('Uniltered Data Output')
plt.xlabel('Time (s)')

fig2 = plt.figure(2)
ax2 = fig2.add_subplot(1, 1, 1)
'''

filt_x = butter_bandpass_filter(
    fx, low_cutoff+.00000001, hi_cutoff-.000000001, sample_rate, 2)

filt_y = butter_bandpass_filter(
    fy, low_cutoff+.00000001, hi_cutoff-.000000001, sample_rate, 2)

filt_z = butter_bandpass_filter(
    fz, low_cutoff+.00000001, hi_cutoff-.000000001, sample_rate, 2)

'''
ax2.plot(tt, yy, c='g')
plt.title('Filtered Data Output')
plt.xlabel('Time (s)')
'''

fig3 = plt.figure(3)
ax3 = fig3.add_subplot(1, 1, 1)
ax3.plot(tt, filt_x, c='b', linewidth=0.15, label='x_filtered')
ax3.plot(tt, filt_y, c='g', linewidth=0.15, label='y_Filtered')
ax3.plot(tt, filt_z, c='r', linewidth=0.15, label='z_Filtered')
plt.legend(loc='upper right')
plt.title('Combination Data')
plt.xlabel('Time (s)')

# fourier transform of the filtered data
fig4 = plt.figure(4)
ax4 = fig4.add_subplot(1, 1, 1)

fxx = fft(filt_x)
fyy = fft(filt_y)
fzz = fft(filt_z)

xf = fftfreq(N, 1/sample_rate)

ax4.plot(xf, np.abs(fxx), c='blue', linewidth=0.15, label='x_fft')
ax4.plot(xf, np.abs(fyy), c='k', linewidth=0.15, label='y_fft')
ax4.plot(xf, np.abs(fzz), c='red', linewidth=0.15, label='z_fft')
plt.legend(loc='upper right')
plt.title('FFT of input data')

#begin testing with the integration functions. How does the data look here? Theoretically, filtered data will be a smoother or more controlled path. In the case of stationary, calibration data, the motion should be negligible
#time_v = ff[:, 0]
time_v = np.linspace(0,500,50000)

x = filt_x
y = filt_y
z = filt_z

vx = []
vy = []
vz = []
sx = []
sy = []
sz = []

sx = it.cumtrapz(it.cumtrapz(x, time_v))
sy = it.cumtrapz(it.cumtrapz(y, time_v))
sz = it.cumtrapz(it.cumtrapz(z, time_v))

fig5 = plt.figure(5)
ax5 = fig5.gca(projection='3d')

xlength = 15
ylength = 15
zlength = 15

ax5.plot3D(sx, sy, sz, c='red', marker="o")
ax5.set_xlabel('X position (m)')
ax5.set_ylabel('Y position (m)')
ax5.set_zlabel('Z position (m)')
ax5.set_xlim3d([-xlength, xlength])
ax5.set_ylim3d([-ylength, ylength])
ax5.set_zlim3d([-zlength, zlength])
ax5.set_autoscale_on(True)

#Histogfram to plot general noise and determine covariance
fig6 = plt.figure(6)
plt.hist(x=fx, color='orange', bins=100, label='fx')
plt.hist(x=fy, color='purple', bins=100, label='fy')
plt.hist(x=fz, color='green', bins=100, label='fz')
plt.legend(loc='upper right')
plt.title('Histogram of Acceleration Measurements')

plt.show()