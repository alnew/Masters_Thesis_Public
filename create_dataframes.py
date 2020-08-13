#--Create app_usage dataframe--
#--Source: https://stackoverflow.com/questions/41857659/python-pandas-add-filename-column-csv
import pandas as pd
import glob
import os

globbed_files = glob.glob("Data/weekly_data/*.xlsx") #create a list of all csv files

data = []
for file in globbed_files:
    try:
        frame = pd.read_excel(file, sheet_name='Top applications by usage')
        frame['filename'] = os.path.basename(file)
        data.append(frame)
    except:
        frame['Application'] = 0
        frame['Usage (kB)'] = 0
        frame['% Usage'] = 0
        frame['filename'] = os.path.basename(file)
        print(os.path.basename(file))
        data.append(frame)


app_usage = pd.concat(data, ignore_index=True)
