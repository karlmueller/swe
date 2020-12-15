#This is development code -- KWM 2020/11/28
import socket
import time
import busio
import board
import adafruit_bno055






# Define connection parameters b/w the RasPi and the bno055 IMU sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)

################
header_len = 4        #Length of fixed header in bytes -> for imu metadata only
refresh_rate = 100    #Desired refresh rate of imu
################

server_ip = '192.168.0.161'  # IP ADDR of the raspberry pi sensor
port = 35196  # port number, ensure >4 digits and an int

# Initialize a TCP/IP socket. Establishes wireless connection to receive data stream from IMU
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Socket must be 'bound' to a specific IP and port number
s.bind((server_ip, port))
print(f'Server initiated at {server_ip}:{port}')

# 'Listen' for a requesting client connection. The argument indicated number of connection queue positions
s.listen(1)

# This variable is to be true while the IMU is meant to obtain data. Can set to false within the whole loop
# using a keyboard interrupt command when the code is menat to stop running.
maintain = True

while True: #Keep socket alive even when conneciton closes... will re-run the program... no handling for closing the 

    b_time = time.time()  # define time of initialization

    clientsocket, address = s.accept()
    print(f'Connection with {address} accepted!')

    #read data type from the client to send proper data
    data_type = clientsocket.recv(1).decode('utf-8')
    #data_type = 1 #fix this later when allowing for input of any data type

    if data_type == '1':  # Euler angles
        dat_string = 'euler'

    elif data_type == '2':  # Quaternion
        dat_string = 'quaternion'

    elif data_type == '3':  # Total Acceleration
        dat_string = 'acceleration'

    elif data_type == '4':  # Linear acceleration (no gravity)
        dat_string = 'linear_acceleration'

    elif data_type == '5':  # Gravity vector only
        dat_string = 'gravity'

    else:
        print(
            f'Data type code of {data_type} is invalid. Please try again with data type from 1 - 5')


    while maintain == True:
        # read the requested data from sensor
        msg_data = str(getattr(sensor, dat_string))
        # combine length tag and sensor data into string to send to client
        msg_data = f'{len(msg_data):<{header_len}}' + msg_data

        print(f'{msg_data}')

        # send length-flagged data to the client
        clientsocket.send(bytes(msg_data, 'utf-8'))

        time.sleep(1/refresh_rate)


    print(f'Socket connection at {address} disconnected, listening for new connection')