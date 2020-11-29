import time
import board
import busio
import adafruit_bno055
import numpy as np
#import pandas as pd

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)

baud_rate = 20

while True:
    #output of the sensor data... this does not store data and is to be deprecated when visualization code created
    print(f'{sensor.euler}')

    #Data storage and formatting on the fly
    #out_data = str(sensor.euler)
    #parse_dat = out_data.strip('(')
    #parse_dat = parse_dat.strip(')')
    #parse_dat = parse_dat.replace(' ','')
    #parse_dat = parse_dat.split(',')

    #form_dat = []
    #for i in range(len(parse_dat)):
    #form_dat.append(round(float(parse_dat[i]),6))

    #print(f'{form_dat}')

    # Sleep with time 1/baud rate. Some studies point to 25Hz being useful though this is TBD
    time.sleep(1/baud_rate)
