import embracedata_download


CALLISTO = { 
  'start_date': '2022-01-31',
  'end_date': '2022-01-31'
}

IMAGER = {
  'start_date': '2022-01-01',
  'end_date': '2022-01-02',
  'stations': ['CA', 'CP'],
  'filters': ['O6-DARK', 'OH-DARK']
}

IONOSONDE = {
  'start_date': '2020-036',
  'end_date': '2020-036',
  'stations': ['BLJ03'],
  'extensions': ['.SAO']
}

MAGNETOMETER = {
  'start_date': '2022-01-01',
  'end_date': '2022-01-02',
  'stations': ['ALF', 'ARA']
}

def download_Files():
  get_data = embracedata_download.Embrace_Data()
  get_data.Callisto(**CALLISTO)
  get_data.Imager(**IMAGER)
  get_data.Ionosonde(**IONOSONDE)
  get_data.Magnetometer(**MAGNETOMETER)

if __name__ == '__main__':
  download_Files()
