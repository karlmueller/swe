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

	sin,sout,serr = client.exec_command(comm)
	for l in line_buffered(sout):
		print(f'{l}')



def line_buffered(f):
	line_buf = ""
	while not f.channel.exit_status_ready():
		line_buf += f.read(1)
		if line_buf.endswith('\n'):
			yield line_buf
			line_buf = ''


'''
stdin, stdout, stderr = client.exec_command(comm)
for line in stdout.read():
	print(f'{line}')
'''