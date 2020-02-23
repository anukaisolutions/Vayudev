import requests
import lxml.html as lh
import pandas as pd
import csv
import datetime

url = "http://ddgmui.imd.gov.in/ual/DisplayTempMessageLive.php?option=0"

#Create a handle, page, to handle the contents of the website
page = requests.get(url)
#Store the contents of the website under doc
doc = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')
tr_elements = doc.xpath('//tr')
def func(index):
    #Create empty list
    col=[]
    #For each row, store each first element (header) and an empty list
    for time in tr_elements[0]:
        time = str(time.text_content())
    c=[]
    
    for t in tr_elements[index]:
        data=str(t.text_content())
        c.append(data)
         # print(c[1])
    c[2] = c[2].replace("\r\n"," ")
    # print(c[0]) 
    # print(c[1])
    # print(c[2])
    name = "ddgmuiData/TTAA/"
    name += c[0]
    name += ".csv"
    with open(name, 'a') as csvFile:
            writer = csv.writer(csvFile)
            now = datetime.datetime.now()
            row = [time,c[0],c[1],c[2]]
            writer.writerow(row)
    c[2] = []
    
for index in range(3,30):
    func(index)
print("done")