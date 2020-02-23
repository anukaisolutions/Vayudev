import math 
import csv
import xlwt 
from xlwt import Workbook 
  
# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

# pr    int(math.cos(60*0.0174533))
# coordinates of chitkara rajpura
lat1 = 30.518986
lat2 = 30.512601

lon1 = 76.655164
lon2 = 76.663573

# converting in from to format
if(lat1>lat2):
    lat1,lat2 = lat2,lat1

if(lon1>lon2):
    lon1,lon2 = lon2,lon1

# distance in metres
# dist = 300

# total = 60
# number = 0
# for i in range (1,int(total/2)):
#     if(i*i >= total):
#         number = i-1
#         break
# # horizontal and vertical cuts 
# horizontal = int(number/2)
# vertical = number-horizontal

# currlat = lat1
# currlon = lon1

# while(currlat<lat2):
#     currlat = dist/(110.574*1000)
#     while(currlon < lon2):
#         currlon = dist/(111.32*1000*math.acos(currlat*0.0174533))
#         print(str(currlat)+","+str(currlon))
#         break
#     break
# # latitude


# # longitude
total = 10
number = 0
for i in range (1,int(total/2)):
    if(i*i >= total):
        number = i-1
        break
# lat1 = 30.518986
# lat2 = 30.512601

# lon1 = 76.655164
# lon2 = 76.663573
alts = [7000,14000,21000,28000,35000]
print("number: "+str(number))
horizontal = int(number)
vertical = int(number)
difflat = (lat2-lat1)/horizontal
difflon = (lon2-lon1)/vertical
print("difflat: "+str(difflat))
currlat =  lat1
currlon = lon1
print("intiiallt: "+str(currlat)+","+str(currlon))
print("lat2: "+str(lat2))
i=0
sheet1.write(i,0,str(i))
sheet1.write(i,1,"Latitude")
sheet1.write(i,2,"Longitude")
i=i+1
while (currlat<=lat2):
    while (currlon<=lon2):
        for alt in alts:
                print(str(currlat)+","+str(currlon))
                sheet1.write(i,0,str(i))
                sheet1.write(i,1,str(currlat))
                sheet1.write(i,2,str(currlon))
                sheet1.write(i,3,str(alt))
                i=i+1

        currlon = currlon + difflon
    currlon = lon1
    currlat = currlat+difflat

wb.save('chitkara3d.xls') 