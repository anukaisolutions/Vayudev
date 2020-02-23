import requests
import lxml.html as lh
import pandas as pd
url = "http://ddgmui.imd.gov.in/ual/DisplayTempMessageLive.php?option=0"

#Create a handle, page, to handle the contents of the website
page = requests.get(url)
#Store the contents of the website under doc
doc = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')
tr_elements = doc.xpath('//tr')
#Create empty list
col=[]
#For each row, store each first element (header) and an empty list
for time in tr_elements[0]:
    n = str(time.text_content())
name = "ddgmuiData/"
name += n
name += ".txt"
file = open(name,'w')     
for k in range(3,31):
    for t in tr_elements[k]:
        name=t.text_content()
        # print ('%d:"%s"'%(i,name))
        col.append((name,))
    col.append("\n")
for i in col:
    for j in i:
        file.write(j)
        file.write(" ")
    # file.write("\n")
    # col = []
file.close()