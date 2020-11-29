import socket
import sys
import time



imu_socket, data_type)
s_data(imu_socket)



def socketing(server_ip, port, metric=0):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((f'{server_ip}', port))
        print(f'Connection with sensor at {server_ip}:{port} established!')
    except:
        sys.exit('Connection failed to establish. Check power, port, and IP ADDR and try again')

    if metric == 0:
        print('Please enter corresponding number for desired data type:')
        print('1) Euler Angles')
        print('2) Quaternion')
        print('3) Total Acceleration ')
        print('4) Linear Acceleration (no grav)')
        print('5) Gravity Vector')
        data_type = input('>> :')
    else:
        data_type = metric
    return [s, data_type]


def s_data(socket_object, size=128):

    current_time = time.time()
    imu_data = socket_object.recv(size).decode('utf-8')
    imu_data = imu_data.strip('(')
    imu_data = imu_data.strip(')')
    imu_data = imu_data.replace(' ', '')
    imu_data = imu_data.split(',')

    return [current_time, imu_data]