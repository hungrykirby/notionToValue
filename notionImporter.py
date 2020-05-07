import csv
import datetime

class NotionCsvImporter:
  csv_file_name = None  
  def __init__(self, csv_file_name):
    self.csv_file_name = csv_file_name

  def convert_csv_to_list(self):
    readed = self.__csv_reader()
    if readed == False:
      return False
    return self.__date_sort(readed)

  def __date_sort(self, results):
    # return [[title => str, d => datetime, mothin => str], [], ... ]
    results_sorted = sorted(results, key=lambda r: r[1])
    return results_sorted

  def __csv_reader(self):
    results = []
    if self.csv_file_name == None:
      return False
    with open('./notionData/' + self.csv_file_name, encoding="utf-8") as f:
      # CSVの形式
      # title, day(date and month), year, ???, mothon
      lines = f.readlines()
      for i, line in enumerate(lines):
        if i == 1: # headerっぽい
          continue
        splitted_line = line.split(',')
        if len(splitted_line) <= 5:
          continue
        title = splitted_line[0]
        day = splitted_line[1].replace("\"", '')
        year = splitted_line[2].replace("\"", '').replace("\t", '').replace(" ", "")
        motion = splitted_line[5].replace("\n", '')
        date_and_month = self.__day_to_date_and_month(day)
        if date_and_month == False:
          continue
        d = year + '/' + str(date_and_month['month']) + '/' + str(date_and_month['date'])
        results.append([title, datetime.datetime.strptime(d, '%Y/%m/%d'), self.__convert_motion_to_value(motion)])
    return results

  def __day_to_date_and_month(self, raw_day):
    raw_day_list = raw_day.split(" ")
    dic_str_month = {
      "Apr": 4,
      "May": 5,
      "Mar": 3,
      "Feb": 2,
      "Jan": 1,
      "Dec": 12,
      "Nov": 11,
      "Oct": 10,
      "Sep": 9,
      "Aug": 8,
      "Jul": 7
    }
    if len(raw_day_list) <= 1:
      return False
    if raw_day_list[0] in dic_str_month:
      month = dic_str_month[raw_day_list[0]]
      return {'month': month, 'date': int(raw_day_list[1])}
    else:
      return False

  def __convert_motion_to_value(self, motion):
    dic_str_motion = {
      '良い': 5, 'そこそこ良い': 4, '普通': 3,
      'そこそこ悪い': 2, '悪い': 1
    }
    if motion in dic_str_motion:
      return dic_str_motion[motion]
    else:
      return -1