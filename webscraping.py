import requests
import pandas
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
#print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
a=soup.find_all('div',class_='_4rR01T')#<div class="_4rR01T">Cellecor X3</div>
b=[]
#print(a)
for i in a[0:10]:
    d=i.get_text()
    b.append(d)
#print(b)

prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')#<div class="_30jeq3 _1_WHN1">₹979</div>
c=[]
#print(prices)
for i in prices[0:10]:
    d=i.get_text()
    c.append(d)
#print(c)


ratings=soup.find_all('div',class_='_3LWZlK')#<div class="_3LWZlK">
e=[ ]
#print(ratings)
for i in ratings[0:10]:
    d=i.get_text()
    e.append(float(d))
#print(e)


features=soup.find_all('ul',class_='_1xgFaf')#<ul class="_1xgFaf">
f=[ ]
#print(features)
for i in features[0:10]:
     d=i.get_text()
     f.append(d)
#print(f)

links=soup.find_all('a',class_='_1fQZEK')
g=[ ]
#print(links)
for i in links[0:10]:
    d= "https://www.flipkart.com/"+i['href']
    g.append(d)
#print(g)

df=pandas.DataFrame()
#print(df)
data={'names':pandas.Series(a),
      'cost':pandas.Series(prices),
      'rattings':pandas.Series(ratings),
      'specifications':pandas.Series(features),
      'quick links':pandas.Series(features)
      }
#print(data)
df = pandas.DataFrame(data)
print(df)
df.to_excel("mobiles_data.xlsx")
