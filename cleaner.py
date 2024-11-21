import pandas as pd

# covnert rastr and decstr to floats
def daysToSeconds(time):
    TIME_MAP = [('d', 86400), ('h', 3600), ('m', 60), ('s', 1)]
    res = 0.0
    isNegative = True if time[0] == "-" else False

    cur = time if not isNegative else time[1:]
    for (chr, multiplier) in TIME_MAP:
        cur_split = cur.split(chr)
        if(len(cur_split) > 1):
            res += (float(cur_split[0]) * multiplier)
            cur = cur_split[1]
    if isNegative:
        res *= -1
    return res

df = pd.read_csv('./data/exoplanets.csv')

df['rastr'] = df['rastr'].apply(daysToSeconds)
df['decstr'] = df['decstr'].apply(daysToSeconds)

# Change sy_pynum to be 1 or more True if 1, False if more than 1
df['sy_pnum'] = df['sy_pnum'].apply(lambda x: x == 1)
df = df.drop(columns=["pl_name","hostname"])
df = df.rename(columns={'sy_snum': "num_stars", 'sy_pnum': 'single_planet_exosystem'})

cleaned_csv = open('./data/exoplanets-clean.csv', 'w')
df.to_csv(cleaned_csv, index=False, lineterminator='\n')