import socket
import sys
import time
import threading

class imu():

    def __init__(self):
        self.header_len = 4
        self.refresh = 50
        
        self.ip = '192.168.0.161'
        self.port = 35196

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.connect((self.ip, self.port))
            print(f'Connection with sensor at {self.ip}:{self.port}')
        except:
            sys.exit('Connection not established. Check power, port number, and IP ADDR and try again')

    def imu_call(self):

            print("11")
            time.sleep(0.5)

    def imu_call2(self):

            print("22222")
            time.sleep(0.1)


imu_thread = threading.Thread(target=imu().imu_call(), arges=(1,))
imu_thread2 = threading.Thread(target=imu().imu_call2(), arges=(1,))


imu_thread.start()
imu_thread2.start()

