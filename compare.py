import csv
import notionImporter
import graphGenerater
import pressureImporter
import datetime
import time
import pandas as pd
import numpy as np


def main():
  pcsv = pressureImporter.PressureCsvImporter()
  notion = notionImporter.NotionCsvImporter('Untitled.csv')
  motion_list = notion.convert_csv_to_list()
  categories = ['firstLast', 'lastFirst', 'firstLastAbs', 'lastFirstAbs', 'downSum', 'upSum', 'downMax', 'upMax', 'ave', 'MaxMinusMin']
  pressure_vals_list = {}
  for category in categories:
    pressure_vals_list[category] = []
  compare_list = {
    'motions': [],
    'pressures': pressure_vals_list
  }
  for i in range(len(motion_list)):
    motion_recorded_date = motion_list[i][1]
    pressure_recorded = pcsv.fetch_one_day(motion_recorded_date - datetime.timedelta(days=1), False)
    if pressure_recorded == False:
      continue
    compare_list['motions'].append(motion_list[i][2])
    for category in categories:
      compare_list['pressures'][category].append(pressure_recorded[category])
  s1 = pd.Series(compare_list['motions'])
  for category in categories:
    print(category)
    s2 = pd.Series(compare_list['pressures'][category])
    res = s1.corr(s2)
    print(res)
  print('---fin---')

if __name__ == "__main__":
    main()