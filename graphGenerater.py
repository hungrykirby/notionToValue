import matplotlib.pyplot as plt
import numpy as np
from os.path import join, dirname
import os

class GraphGenerator:
  label_x = "x"
  label_y = "y"
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

  def fill_gap(self, x, y, interval = 1):
    len_list = len(x)
    x_min = x[0]
    x_max = x[len_list - 1]
    i = x_min
    xs = []
    ys = []
    while i < x_max:
      target_x = i
      tmp = np.asarray(x) - target_x
      tmp2 = np.where(tmp <= 0)
      idx = np.abs(tmp2).argmax()
      i = i + interval
      if idx > len_list - 1:
        continue
      x1 = x[idx]
      x2 = x[idx + 1]
      y1 = y[idx]
      y2 = y[idx + 1]
      # print(x_min, i, x_max)
      target_y = (y2 - y1)*(target_x - x1)/(x2 - x1) + y1
      xs.append(target_x)
      ys.append(target_y)
    return {'x': xs, 'y': ys}

  def create_motion_graph(self, x, y, save_str = False):
    plt.title(self.title)
    plt.xlabel(self.label_x)
    plt.ylabel(self.label_y)
    plt.ylim(self.area['min']['y'], self.area['max']['y'])
    plt.plot(x, y)
    if save_str:
      rootdir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
      plt.savefig(join(os.getcwd(), 'imgs', 'saved' + save_str + '.png'))
      plt.close()
    else:
      plt.show()
