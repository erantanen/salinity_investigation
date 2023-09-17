import os
import pandas as pd
import csv
import pre_proc_depth_id as pre


# binning by brute force
# csv structure
# csv_header = ['date', 'lat', 'long', 'Depthm', 'T_degC', 'Salnty']

def open_csv(proc_file):
    # data = pre.data_to_proc(proc_file, proc_fields)
    # this is the consolidated csv just read each line
    data_b = os.path.join(os.getcwd(), "input", proc_file)
    return pd.read_csv(data_b)


def date_bin(data_main):
    # builds files based on year

    # pre-set a date for testing
    date_old = '1900'

    for i, row in data_main.iterrows():
        date_new = row['date']
        date_string = date_new.split("-")

        # shifts date from old to new
        # 1900 < 1949
        if date_old < date_string[0]:
            date_old = date_string[0]
            date_csv = os.path.join(os.getcwd(), "output", date_string[0] + '.csv')
            writer, fh = pre.cvs_builder(date_csv)

        data_list = [row['date'], row['lat'], row['long'], row['Depthm'], row['T_degC'], row['Salnty']]
        writer.writerow(data_list)

    fh.close()




# fields = ['date', 'lat', 'long', 'Depthm', 'T_degC', 'Salnty']
csv_data_new = open_csv("data_everything.csv")
date_bin(csv_data_new)
