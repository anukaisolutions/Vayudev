
import csv
import requests
import datetime


def getData(year,month,from1,to,statio):
    url = "http://weather.uwyo.edu/cgi-bin/sounding?region=seasia&TYPE=TEXT%3ARAW&YEAR="+year+"&MONTH="+month+"&FROM="+from1+"&TO="+to+"&STNM="+statio
    response = requests.get(url)
    response = str(response.content)
    response = response[3:]
    TTAA = "null"
    TTBB = "null"
    TTCC = "null"
    TTDD = "null"
    PPBB = "null"
    listt = []
    listt = response.split("\\n ")
    for el in listt:
        # print(el)
        if(el[0] == 'T' and el[1] == 'T' and el[2] == 'A' and el[3] == 'A'):
                TTAA = el
        elif(el[0] == 'T' and el[1] == 'T' and el[2] == 'B' and el[3] == 'B'):
                TTBB = el
        elif(el[0] == 'T' and el[1] == 'T' and el[2] == 'C' and el[3] == 'C'):
                TTCC = el
        elif(el[0] == 'T' and el[1] == 'T' and el[2] == 'D' and el[3] == 'D'):
                TTDD = el
        elif(el[0] == 'P' and el[1] == 'P' and el[2] == 'B' and el[3] == 'B'):
                PPBB = el
    name = "wyomingData/"
    name += statio+".csv"
    with open(name, 'a') as csvFile:
        writer = csv.writer(csvFile)
        now = datetime.datetime.now()
        row = [TTAA, TTBB, TTCC,TTDD,PPBB,now]
        writer.writerow(row)
        print("inserted in row")
    
   
#     TTCC = second[1]
#     TTBB = second[0]
#     TTAA = first[0]
#     TTAA = TTAA.replace('\\n'," ")
#     TTAA = TTAA.replace("TTAA","")
#     TTBB = TTBB.replace("\\n"," ")
#     TTCC = TTCC.replace("\\n"," ")
#     lines = []
#     name = "wyomingData/"
#     name += statio+".csv"
#     with open(name, 'a') as csvFile:
#         writer = csv.writer(csvFile)
#         now = datetime.datetime.now()
#         row = [TTAA, TTBB, TTCC,now]
#         writer.writerow(row)

year = "2019"
month = "3"
from1 = "2900"
to = "2900"
stationCodes = ['42101','43192','43185','43150','42299','43346','42874']
# stationCodes = ['42101']
for station in stationCodes:
    getData(year,month,from1,to,station)
    print(station)
