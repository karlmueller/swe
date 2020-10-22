import paramiko

'''
Paramiko allows for communication via SSH connection within Python. This allows for the
calling of required IMU driver functions as well as pulling information from the RasPi device
via the command line output and put into graphs within linux.

Ensure that username, IP addressm, passowrd, etc are properly input

'''

def sshCommand(hostname, port=22, username = 'pi', password = 'karl', comm =''):
	client = paramiko.SSHClient() #initialize with creation of SSH client

	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.load_system_host_keys()#required to auth via password or private key, check with server host key

	client.connect(hostname, port, username, password)

	stdin, stdout, stderr = client.exec_command(comm)
	print('command executed')

	stdout_r = stdout.readlines()
	for l in stdout_r:
		print(l)

'''
	for l in line_buffered(stdout):
		print(l)

def line_buffered(f):
	print("entered buffer sequence")
	line_buf = ""
	while True: #not f.channel.exit_status_ready():
		line_buf += f.read(1)
		print("completed line")
		if line_buf.endswith('\n'):
			yield line_buf
			line_buf = ""
			break

'''



'''
	for line in stdout.read():
		print(f'{line}')
#Theoretically, this is a way of obtaining continous output. Needs work to function, however
	sin,sout,serr = client.exec_command(comm)
	for l in line_buffered(sout):
		print(f'{l}')

'''


