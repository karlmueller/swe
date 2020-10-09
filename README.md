# swe
BME5001 Sway Project Repo

This repo contains a working directory of files and data required for the function of the

As of 10/09/2020
 - The sensor is constructed out of a Raspberry Pi 4B (4GB RAM) and an Adafruit breakout board bno055 inertial measurement unit
 
 
 Several packages are required to use this software as of current:
 - matplotlib #plotting and data interface
 - paramiko #SSH interface library
 - Download of the Adafruit_CircuitPython_BNO055 Sensor libraries (linked here, not copied)
 
 Note on the Adafruit_CircuitPython libraries
  - The adafruit tutorial (https://learn.adafruit.com/bno055-absolute-orientation-sensor-with-raspberry-pi-and-beaglebone-black/overview) references both an old version of the software as well as incorrect information in terms of interfacing with the new software. The rest of the information is still relatively useful
  - One must install CircuitPython here: https://github.com/adafruit/circuitpython and the updated bno055 sensor repo from here: https://github.com/adafruit/Adafruit_CircuitPython_BNO055.git ... IT IS IMPORTANT THAT YOU DO NOT BLINDLY DOWNLOAD THE SOFTWARE SUGGESTED IN THE TUTORIAL
  - The tutorial mentions that the RasPi cannot support I2C but can only support UART... this is false. UART does not function (at least with the Adafruit_CircuitPython version of the BNO055 library... I2C is required... unintuitive, I know.
  - Information on enabling the proper I2C channels on the Raspi can be found here: https://gps-pie.com/pi_i2c_config.htm <-- these are gods amonst men. Note that SDA should be wired into GPIO2, NOT SDA2, and SCL should be wired into GPIO 3, NOT SCL 3.
  
  
  SSH is the current recommended interface with the unit. This can be done over any network but be aware that the ip address of the raspberry pi may change depending on the network that it is on. 
