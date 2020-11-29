#Code based on the bno055_simpletest framework by Adafruit
#Modifications initiated by Karl Mueller

'''
Basically, this is the code that uses the sensor API to initialize the sensor via the i2c bus and 
create an output of sensor data. This code itself does not modify the sensor data, merely
formats output and in a convoluted way at that. 

The intent here is to create a function with a parameter that correpsonds to the requried data output
of calling the sensor. We would call for say "euler angles" into the function and
the code would output ONLY these euler angles, not the temperature and the magnetic field and the 
other nonsense outputs that this gives. those aren't useful. 

Note that if made into a function, will need to change how the other code calls this. May actually make it 
easier if running the entirety of the code from the pi though

'''
import time
import board
import busio
import adafruit_bno055
import numpy as np

# Use these lines for I2C
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)

def imu_get_data(baud):

data_out = pd.DataFrame([[]], columns=['gyro','euler','linAcc','grav'])
datapoints = 0

while True:
    '''
    print("Temperature: {} degrees C".format(sensor.temperature))
    print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
    print("Magnetometer (microteslas): {}".format(sensor.magnetic))
    print("Gyroscope (rad/sec): {}".format(sensor.gyro))
    print("Euler angle: {}".format(sensor.euler))
    print("Quaternion: {}".format(sensor.quaternion))
    print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
    print("Gravity (m/s^2): {}".format(sensor.gravity))
    '''
    now = datetime.now().time()
    data_out = pd.DataFrame

    datapoints += 1
    time.sleep(1/baud)
