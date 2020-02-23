import csv
def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


while(1):
    i=0
    ifile  = open('loc1.csv', "r")
    reader = csv.reader(ifile)
    rownum = 0
    for row in reader:
            
            if(row[4]!='Altitude'):
                    # tempalt = str(row[4])
                    tempalt = 0
                    temppos=str(row[3])
                    temploc = temppos.split(',')
                    templat = float(temploc[0])
                    templon = float(temploc[1])
                    templat = truncate(templat,3)
                    templon = truncate(templon,3)
                    print(templat)
                    print(templon)
                    print(tempalt)
                    print(i)
                    i=i+1
        