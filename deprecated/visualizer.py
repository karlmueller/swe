from tf.transformations import euler_from_quaternion as efq
from datetime import datetime as DT
import numpy as np
import matplotlib.pyplot as plt



def plotter(time, data_list):

    for i  in data_list:
        