from matplotlib.pyplot import figtext
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fftfreq
import statistics as st
import scipy.stats as stats
import scipy

#read in 
no_fan = np.genfromtxt('testing_imu_output_NOFAN.csv', delimiter=',', dtype=float)
fan = np.genfromtxt('testing_imu_output.csv',
                    delimiter=',', dtype=float)

ff = np.genfromtxt('fanless_filter_test.csv', delimiter=',', dtype=float)

no_fan = no_fan[1:,:]
fan = fan[1:,:]

ff = ff[1:,:]

#1000 data points at 10Hz
sample_rate = 20 #Hz
T = 1/sample_rate #Sampling period
N = 2000 #Sample number

#fig, ax1 = plt.subplots(nrows=3, ncols=1)

# Transform 3 axis data into non-directional total acceleration


ff_acc = np.sqrt(np.square(ff[:, 1])+np.square(ff[:, 2])+np.square(ff[:, 3]))

mn = np.mean(ff_acc)

var = np.var(ff_acc)
stdev = np.sqrt(var)
x_norm = np.linspace(mn-3*stdev, mn+3*stdev, 100)


plt.figure(1)
plt.subplot(2,1,1)
plt.plot(ff[:, 0], ff_acc, 'ro')
plt.title('Acceleration Magnitude time points')


yf = fft(ff_acc)
#xf = np.linspace(0.0,1.0/(2.0*T), N//2)
xf = fftfreq(N, 1/sample_rate)

plt.subplot(2,1,2)
#plt.plot(xf, 2.0/N*np.abs(yf[0:N//2]))
plt.plot(xf, np.abs(yf))
plt.title('FFT of input data')
#plt.xlim([0, 3])

plt.figure(2)
plt.subplot(1,1,1)
plt.plot(x_norm, stats.norm.pdf(x_norm, mn, stdev))











plt.grid()
plt.show()


