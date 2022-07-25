#!/usr/bin/python3
import pandas as pd

#YYYY-MM-DD
#start_date = '2020-02-01'
#end_date = '2020-02-03'
#range_date = pd.date_range(start=start_date, end=end_date)

#print(range_date)
#stn = 'CP'
#uri = 'https://embracedata.inpe.br/imager/'

#for day in range_date:
 # print(uri + day.strftime(f'{stn}/%Y/{stn}_%Y_%m%d/'))


def returnRangeOfDates(start_date, end_date):
  range_date = pd.date_range(start=start_date, end=end_date, freq='MS')
  full_uri = range_date.strftime('%Y%m%b')
  return full_uri.str.lower()

start_date = '2020-02'
end_date = '2020-10'
#stn = 'CP'
range_date = returnRangeOfDates(start_date, end_date)
for month in range_date:
  print(month)