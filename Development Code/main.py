from pkgutil import get_data
from client_fx import client_fx
import threading

'''
# Initialize IMU data pipeline thread
imu = client_fx()
imu_thread = threading.Thread(target=imu.run())
imu_thread.daemon = True
imu_thread.start()
'''

imu = client_fx()



