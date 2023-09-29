
def proc_theil(data_in ,d1 ,d2 ,year_str):

    from scipy.stats import theilslopes

    # the theil sen slope is very mem intensive
    # and has to be watched,initial running brought
    # the system to its knees with mem @ 32g
    # output -
    # TheilslopesResult(slope=-0.3433476394849728, intercept=21.422918454935427,
    #             low_slope=-0.5690200210748134, high_slope=-0.11784511784511809)

    df_p = data_in
    depth_1 = d1
    depth_2 = d2
    year = year_str
    cond_1 = df_p.Depthm.between(depth_1 ,depth_2)
    cond_2 = df_p.date.str.startswith(year)
    cond_3 = (df_p.Salnty.notnull() & df_p.T_degC.notnull())
    result_full = df_p.loc[cond_1 & cond_2 & cond_3]

    if len(result_full.index) == 0:
        analysis_ts = "empty_string"
    else:
        analysis_ts = theilslopes(result_full['T_degC'], result_full['Salnty'])

    return  analysis_ts


def proc_kendalltau(data_in, d1, d2, year_str):
    from scipy.stats import kendalltau

    df_p = data_in
    depth_1 = d1
    depth_2 = d2
    year = year_str
    cond_1 = df_p.Depthm.between(depth_1, depth_2)
    cond_2 = df_p.date.str.startswith(year)
    cond_3 = (df_p.Salnty.notnull() & df_p.T_degC.notnull())
    result_full = df_p.loc[cond_1 & cond_2 & cond_3]

    analysis_t = kendalltau(result_full['T_degC'], result_full['Salnty'])

    return analysis_t


def proc_spearman(data_in, d1, d2, year_str):
    from scipy.stats import spearmanr

    df_p = data_in
    depth_1 = d1
    depth_2 = d2
    year = year_str
    cond_1 = df_p.Depthm.between(depth_1, depth_2)
    cond_2 = df_p.date.str.startswith(year)
    cond_3 = (df_p.Salnty.notnull() & df_p.T_degC.notnull())
    result_full = df_p.loc[cond_1 & cond_2 & cond_3]

    analysis_s = spearmanr(result_full['T_degC'], result_full['Salnty'])

    return analysis_s


def proc_linregress(data_in, d1, d2, year_str):
    from scipy.stats import  linregress

    df_p = data_in
    depth_1 = d1
    depth_2 = d2
    year = year_str
    cond_1 = df_p.Depthm.between(depth_1, depth_2)
    cond_2 = df_p.date.str.startswith(year)
    cond_3 = (df_p.Salnty.notnull() & df_p.T_degC.notnull())
    result_full = df_p.loc[cond_1 & cond_2 & cond_3]

    analysis_l = linregress(result_full['T_degC'], result_full['Salnty'])

    return analysis_l


