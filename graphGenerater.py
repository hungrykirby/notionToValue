import matplotlib.pyplot as plt
import numpy as np
from os.path import join, dirname
import os

class GraphGenerator:
  label_x = "x"
  label_y = "y"
  fig = None
  title = None
  file_name = None

  area = {
    'max': {
      'x': 500, 'y': 500
    },
    'min':{
      'x': 100, 'y': 100
    }
  }

  def __init__(self, title, file_name):
    self.title = title
    self.file_name = file_name

  def set_max_min(self, max_x, max_y, min_x, min_y):
    self.area = {
      'max': {
        'x': max_x, 'y': max_y
      },
      'min':{
        'x': min_x, 'y': min_y
      }
    }

  def set_labels(self, label_x, label_y):
    self.label_x = label_x
    self.label_y = label_y

  def create_motion_graph(self, x, y, save_flag = False):
    plt.title(self.title)
    plt.xlabel(self.label_x)
    plt.ylabel(self.label_y)
    plt.ylim(self.area['min']['y'], self.area['max']['y'])
    plt.plot(x, y)
    if save_flag:
      rootdir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
      plt.savefig(join(os.getcwd(), 'imgs', 'saved.png'))
    else:
      plt.show()
