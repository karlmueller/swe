import paramiko as pk
import os
import time

from sshCmd import sshCommand


user = 'pi'
pswd = 'karl' 
port = 22
addr = '192.168.0.161' 

#ensure that the proper command is entered here. Should point to a symbolically-linked python script within the root directory of the pi

sshCommand(addr, port, user, pswd, 'python bno055_simpletest.py')