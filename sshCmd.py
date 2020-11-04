import paramiko
import sys
import time
import matplotlib.pyplot as plt
import numpy as np

'''
Paramiko allows for communication via SSH connection within Python. This allows for the
calling of required IMU driver functions as well as pulling information from the RasPi device
via the command line output and put into graphs within linux.

Ensure that username, IP addressm, passowrd, etc are properly input if errors occur
'''

def sshCommand(hostname, port=22, username = 'pi', password = 'karl', comm =''):
	client = paramiko.SSHClient() #initialize with creation of SSH client

	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.load_system_host_keys()#required to auth via password or private key, check with server host key

	client.connect(hostname, port, username, password)
	print('connection initialized')
	stdin, stdout, stderr = client.exec_command(comm, get_pty=True) #does this run in parallel with the following processes??? I thought so, this may be the problem or this needs more time to gather information
	stdout.flush()
	save_data = ['roll','pitch','yaw']

	time_begin = time.time()
	'''
	fig = plt.figure()
	ax1 = fig.add_subplot(1,1,1)
	'''

	#fig = plt.gcf()
	#fig.show()
	#fig.canvas.draw()

	#plt.axis([time_begin-10, time_begin, -360, 360])
	#plt.ylabel('Euler Angle(s) [Degrees]')
	#plt.xlabel('Time History (s)')

	time_series = []
	euler_series = []

	while True:
		c_time = time.time()
		#print(stdout.readline(100))
		out_data =  stdout.readline(35)
		parse_dat = out_data.strip('(')
		#parse_dat = parse_dat.strip(')')
		parse_dat = parse_dat.replace(' ','')
		parse_dat = parse_dat.replace(')\r\n','')
		parse_dat = parse_dat.split(',')
		form_dat = []

		form_dat.append(float(c_time))

		for ii in range(len(parse_dat)):
			form_dat.append(round(float(parse_dat[ii]), 6))
		print(f'{form_dat}')
		'''
		xs.append(form_dat[1:])
		ys.append(form_dat[1])
		ax1.plot(xs,ys,['ro','bo','go'])
		'''
		'''
		time_series.append(form_dat[0])
		euler_series.append(form_dat[1])
		
		if len(time_series)>30:
			time_series = time_series[-30:]
			euler_series = euler_series[-30:]
		'''
		#print(len(time_series))

		#plt.plot(time_series, euler_series,'ro')
		#plt.axis([c_time-1.5, c_time, -360, 360])
		#ani = anim.FuncAnimation(fig, interval = 100)
		#fig.canvas.draw()
		#save_data.append(form_dat)
		stdout.flush()
		time.sleep(.05)
		

