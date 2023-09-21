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


def panda_bin_gen(data_frame, depth_1, depth_2, inspect_date):
    # hard-coding nulls quick and dirty

    cond_1 = data_frame.Depthm.between(depth_1, depth_2)
    cond_2 = data_frame.date.str.startswith(inspect_date)
    cond_3 = (data_frame.Salnty.notnull() & data_frame.T_degC.notnull())
    result = data_frame.loc[cond_1 & cond_2 & cond_3]

    return result


def mean_total_year(data_main, target, d1, d2):

    # builds a dictionary of lists - year

    # data cleaning of incoming dataframe
    df_group = data_main
    # depth banding
    depth_1 = d1
    depth_2 = d2
    cond_1 = df_group.Depthm.between(depth_1, depth_2)
    cond_3 = (df_group.Salnty.notnull() & df_group.T_degC.notnull())
    result_inside = df_group.loc[cond_1 & cond_3]

    # pre-set a date for testing
    date_old = '1900'
    new_dic = dict()
    new_list = []

    # for i, row in result_inside.iterrows():
    for i, row in result_inside.head(1000).iterrows():

        date_new = row['date']
        date_string = date_new.split("-")

        # shifts date from old to new
        # 1900 < 1949
        # sets new dictionary key
        if date_old < date_string[0]:
            date_old = date_string[0]
            new_list.append(row[target])
            new_dic["lst_" + str(date_old)] = new_list
        else:
            new_list.append(row[target])
            new_dic["lst_" + str(date_old)] = new_list

    return new_dic

# fields = ['date', 'lat', 'long', 'Depthm', 'T_degC', 'Salnty']
#csv_data_new = open_csv("data_everything.csv")
# date_bin(csv_data_new)
