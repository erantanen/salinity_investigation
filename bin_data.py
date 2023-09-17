import os
import pandas as pd
import csv
import pre_proc_depth_id as pre


#
# csv structure
# csv_header = ['date', 'lat', 'long', 'Depthm', 'T_degC', 'Salnty']


def date_bin(proc_file):
    from datetime import datetime
    # pre-set a date for testing
    date_old = '1900-01'
    #

    data_list = []
    # data = pre.data_to_proc(proc_file, proc_fields)
    # this is the consolidated csv just read each line
    data_b = os.path.join(os.getcwd(), "input", proc_file)
    data_main = pd.read_csv(data_b)

    for i, row in data_main.head(2000).iterrows():
        date_new = row['date']
        dt_obj1 = datetime.strptime(date_old, "%Y-%m")
        dt_obj2 = datetime.strptime(date_new, "%Y-%m")

        # shifts date from old to new
        if dt_obj1 < dt_obj2:
            date_old = date_new
            date_csv = os.path.join(os.getcwd(), "output", date_new + '.csv')
            print(date_csv)
            writer, fh = pre.cvs_builder(date_csv)

    fh.close()


def salinity_bin():
    print("blah")


#fields = ['date', 'lat', 'long', 'Depthm', 'T_degC', 'Salnty']
date_bin("data_everything.csv")
