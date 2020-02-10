from bs4 import BeautifulSoup
import requests

import matplotlib.pyplot as cizim
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

daysize = int(input("Please enter the day count you want to access"))


adanacimento = 'http://finans.mynet.com/borsa/hisseler/adana-adana-cimento-a/tarihselveriler/'
site = requests.get(adanacimento)
soup = BeautifulSoup(site.text, 'html.parser')
table =soup.find_all('tbody',id="fnTarihselListe")

data = {
    'days':[],
    'last' : [],
    'size' : []
}

for row in table:
    trclass = row.find_all('tr',class_="")


for rows in trclass[:daysize]:
    values = rows.find_all('td',class_="")
    dayvalues = rows.find_all('td',class_="ndt-leftText")
    data['days'].append(dayvalues[0].get_text())
    data['last'].append(values[0].get_text())
    data['size'].append(values[3].get_text())
    
    
    
print("--------------------------------------")
print("Days List:")
print(data['days'])
print("Value Per Stock List")
print(data['last'])
print("Size of Company List")
print(data['size'])

print("               --------------------------------------")
print("               Line Chart:Per Share Value x Days")
cizim.plot(data['days'],data['last'])
cizim.xlabel('Days')
cizim.ylabel('Per Share Value')
cizim.show()


print("               --------------------------------------")
print("               Bar Chart:Total Size x Days")
barchart=[]
for x in range(daysize):
    barchart.append(data['size'][x])

objects = (data['days'])
y_pos = np.arange(len(objects))
performance = (barchart)
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Market Size')
plt.title( 'Size History')
 
plt.show()



