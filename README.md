# Downloading files from Space Weather Repository
[![](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/)
[![](https://img.shields.io/badge/Version-1.0-yellow.svg)](https://github.com/embrace-inpe/download_embracedata)
[![](https://img.shields.io/badge/INPE-EMBRACE-orange.svg)](http://www2.inpe.br/climaespacial/portal/pt/)

Need Python >= 3.6.10 to work

Clone repository in https....

Install packeges
```bash
pip3 install -r requirements.txt
```

Change input data in get_data.py and unconment instrument to download data.
Folder will be created in te base dir of project with tree bellow:
data/instrument/year/stn/ etc


input format / stations / filters:

1. ### CALLISTO:
```text
only date with format bellow:
YYYY-MM-DD
```

2. ### IMAGER:
```text
date and station/filter with format bellow:
YYYY-MM-DD
all available stations: ['BJL', 'BV', 'CA', 'CP', 'SMS']
all available filters: ['O6', 'OH', 'O6-DARK', 'OH-DARK']
```

3. ### IONOSONDE:
```text
date and station/extension with format bellow:
YYYY-DOY
all available stations: ['BLJ03', 'BVJ03', 'CAJ2M', 'CGK21', 'FZA0M', 'SAA0K', 'SMK29']
all available extensions: ['.RSF', '.SAO', '.PNG', '.DFT', '.DVL', '.SKY' 'SAO.XML' 'MMM']
```

4. ### LIDAR:
```text
date and element with this format:
YYYY-MM-DD
all available elements: ['Potassium', 'Sodium']
```

5. ### MAGNETOMETER:
```text
date and station whit format bellow:
YYYY-MM-DD
all available stations: ['ALF', 'ARA', 'CBA', 'CHI', 'CXP', 'EUS', 'JAT', 'MAN','MED',
                        'PAL', 'PVE', 'RGA', 'SJC', 'SLZ', 'SMS', 'STM', 'TCM', 'VSS']
```


6. ### SCINTILLATION:
date and stations with format bellow:
YYYY-DOY
```text
all available stations: ['afl', 'alt', 'apu', 'bht', 'bhz', 'boa', 'bov', 'bsa', 'bsb',
                         'cba', 'chp', 'cpa', 'cub', 'dou', 'imp', 'ios', 'nta', 'pbr',
                         'pln', 'ppt', 'pvh', 'sjc', 'sjk', 'slz', 'sta', 'tfe']
```
