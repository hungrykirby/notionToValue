import csv
import datetime
import glob

class PressureCsvImporter:
  pressure_list = None

  def __init__(self):
    self.pressure_list = self.convert_csv_to_list()

  def test(self):
    self.__csv_reader()
  
  def fetch_one_day(self, oneday, fetch_type):
    results = [p[1] for p in self.pressure_list if p[0].date() == oneday.date() ]
    print(results)
    l = len(results)
    if l != 24:
      return False
    vals = {
      'firstLast': results[0] - results[l - 1], # 0時 - 23時
      'lastFirst': results[l - 1] - results[0], # 23 - 0
      'firstLastAbs': abs(results[0] - results[l - 1]),
      'lastFirstAbs': abs(results[l - 1] - results[0]),
      'downSum': 0, # 一日の下がり合計
      'upSum': 0,
      'downMax': 0,
      'upMax': 0,
      'gap': 0,
      'ave': sum(results) / l,
      'MaxMinusMin': max(results) - min(results)
    }
    downs = []
    ups = []
    for i in range(len(results)):
      if i == l - 1:
        continue
      if results[i] > results[i + 1]:
        vals['downSum'] += (results[i] - results[i + 1])
        downs.append(results[i] - results[i + 1])
      else:
        vals['upSum'] += (results[i + 1] - results[i])
        ups.append(results[i + 1] - results[i])
    if len(downs) > 0:
      vals['downMax'] = min(downs)
    if len(ups) > 0:
      vals['upMax'] = max(ups)
    vals['gap'] = max([vals['upMax'], abs(vals['downMax'])])
      
    return vals


  def convert_csv_to_list(self):
    return self.__time_sort(self.__csv_reader())

  def __time_sort(self, results):
    return sorted(results, key=lambda r: r[0])

  def __csv_reader(self):
    results = []
    all_csv_files = glob.glob('./pressureData/*.csv')
    for f1 in all_csv_files:
      with open(f1, encoding="utf-8") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
          splitted_line = line.split(',')
          y = int(splitted_line[1])
          m = int(splitted_line[2])
          d = int(splitted_line[3])
          h = int(splitted_line[4])
          p = float(splitted_line[5])
          time_str = str(y) + '/' + str(m) + '/' + str(d)
          time_str += ' '
          if h == 24: # 24時は翌日の0時
            time_str += '0'
            dtime = datetime.datetime.strptime(time_str, '%Y/%m/%d %H') + datetime.timedelta(days=1)
          else:
            time_str += str(h)
            dtime = datetime.datetime.strptime(time_str, '%Y/%m/%d %H')
          results.append([dtime, p])
    return results