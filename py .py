import requests
from bs4 import BeautifulSoup
import json
import time
# url = BeautifulSoup(requests.get("https://www.collegedekho.com/mtech-mechanical_engineering-colleges-in-india/").content,"html.parser").find('div',class_="middle-container")
# title = url.find_all("div",class_="title")
# v = []
# for i in title:
#     d = {}
#     d['Name']=(i.a.text).replace("\n","").replace("\n","").replace("\n","").replace("\n","").replace("                    ","").replace("                    ","").replace("                    ","").replace("                    ","")
#     d['link'] = "https://www.collegedekho.com" + (i.a['href'])
#     if i.div != None:
#         d['rating'] = float(i.div.div.span['style'][6:-1])/100 * 5
#     v.append(d)
# k = open('college.json','w')
# json.dump(v,k,indent=4)

f = open("college.json","r").read()
v = json.loads(f)
a = 1
for i in v:
    url = BeautifulSoup(requests.get(i['link']).content,"html.parser")
    if url.find('div',class_="block facilitiesBlock") != None:
        facilites = url.find('div',class_="block facilitiesBlock").find_all('div',class_="title")
    collegeContacts = url.find('div',class_="collegeContacts").find('ul',class_='addressList').find_all('li')
    col = []
    for j in collegeContacts:
        i[(j.find('div',class_="label")).text] =(j.find('div',class_="data").text).replace("\n","").replace("\n","").replace("                              ","")

    fac = []
    for j in facilites:
        if j != None:
            fac.append(j.text)
            i["Facilites"] = fac
    a += 1
    if a%9==0:
        time.sleep(2)
print(v)
jk = open("detail.json","w")
json.dump(v,jk,indent=4)