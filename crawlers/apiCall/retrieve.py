import csv
def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


ifile  = open('loc1.csv', "r")
reader = csv.reader(ifile)
rownum = 0
for row in reader:
    pos=""
    alt=""
    lat=""
    lon=""
    if(row[4]!='Altitude'):
        alt = str(row[4])
        pos=str(row[3])
        loc = pos.split(',')
        # print(loc)
        lat = float(loc[0])
        lon = float(loc[1])
        lat = truncate(lat,3)
        lon = truncate(lon,3)
        print(str(lat))
        print(str(lon))
        print(str(alt))
ifile.close()