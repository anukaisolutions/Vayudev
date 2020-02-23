
def getData(year,month,form1,to,statio):
    url = "http://weather.uwyo.edu/cgi-bin/sounding?region=seasia&TYPE=TEXT%3ARAW&YEAR="+year+"&MONTH="+month+"&FROM="+from1+"&TO="+to+"&STNM="+station
    import requests
    response = requests.get(url)
    response = str(response.content)
    # print(response.content)
    name = "wyomingData/"+station+".txt"
    file = open(name,'w') 
    for i in response[3:-1]:
        if(i == '\\'):
            file.write("\n")
        elif(i == 'n'):
            continue
        else:
            file.write(i)

    file.close() 


year = "2019"
month = "3"
from1 = "2700"
to = "2700"
stationCodes = ['42707','42101','42182','42339','42361','42379','42299','42314']
for station in stationCodes:
    getData(year,month,from1,to,station)
