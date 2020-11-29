import paramiko
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import matplotlib.animation as animation

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

	baud_rate = 5

	time_series = []
	euler_series = []

	




# reading and theoretically plotting perpetual while loop
	while True:
		stdout.flush()
		c_time = time.time()

		out_data =  stdout.readline(45)
		parse_dat = out_data.strip('(')

		parse_dat = parse_dat.replace(' ','')
		parse_dat = parse_dat.replace(')\r\n','')
		parse_dat = parse_dat.split(',')
		form_dat = []

		form_dat.append(float(c_time))

		for ii in range(len(parse_dat)):
			form_dat.append(round(float(parse_dat[ii]), 6))
		#print(f'{form_dat}')

		time.sleep(1/baud_rate)
