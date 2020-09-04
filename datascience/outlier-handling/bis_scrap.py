#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:11:16 2020

@author: nicholassandomeno
"""

import requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup, NavigableString, Tag


# (1) - bis denied person's list
url = "https://www.bis.doc.gov/dpl/public/dpl.php"
#hdr = {'User-Agent': 'Mozilla/5.0'}
#req = Request(url, headers=hdr)
#res = urlopen(req)
#rawpage = res.read().decode("utf-8")
#page = rawpage.replace('<!-->', '')
#soup = BeautifulSoup(res.text, "html.parser")
#table = soup.find("table")
#print(table)
source = url
bis_dict = {}


response = requests.get(url)
response
print(type(response.text))
soup = BeautifulSoup(response.text, "html.parser")
table = soup.findAll('table')
print(table)

table_rows = soup.findAll('tr')

for tr in table_rows:
    iter = 0 
    td = tr.findAll('td')
    for entry in td:
     br_tag = entry.findAll("br")
     
     if len(br_tag) > 0:
        name = entry.find("br").previousSibling
        name = str(name)
        address = entry.find("br").nextSibling
        address = str(address)
        #row = [i.text for i in td]
        print("NAME: ", name)
        print("ADDRESS: ", address)
        bis_dict[name] = address
        iter = iter + 1
# ---------------------------------------------------------









