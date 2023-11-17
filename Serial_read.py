from itertools import count
from sys import intern
import serial
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import pyexcel as px
import datetime
import random

temper_min, temper_max = -5, 5



serialport = serial.Serial('/dev/cu.usbserial-0001', 115200, timeout=1)

class DongPlot():
  def __init__(self):
    self.time_vals = [0]
    self.temper_vals = [0]
    self.index = count()
    self.cur_index = 0
  
  def animate(self, i):
    serial_line = str(serialport.readline())[2:-5]
    # print("just test one time")     # <- gonna delete
    if serial_line == '':
      pass
    else:
      print('serial_line : ', serial_line)
      self.time_vals.append(next(self.index)/1)      # need to be calibrated
      if str(serial_line) == "":
        self.temper_vals.append(0)
        pass
      else:
        self.temper_vals.append(float(serial_line))
        plt.cla()
        plt.ylim(temper_min, temper_max)
        plt.plot(self.time_vals, self.temper_vals)
        plt.title("BioBME")
        plt.xlabel('time [s]')
        plt.ylabel("Temperature ['C]")
        plt.tight_layout()  
      self.cur_index += 1         # Mystery
        

if __name__ == "__main__":
  dongplot = DongPlot()
  ani = FuncAnimation(plt.gcf(), dongplot.animate, interval=20, frames=200)
  plt.show()
  print("Finish")