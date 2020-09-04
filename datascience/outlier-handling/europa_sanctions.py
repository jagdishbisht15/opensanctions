#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 13:39:54 2020

@author: nicholassandomeno
"""

import requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup, NavigableString, Tag
import pandas as pd
from bs2json import bs2json

# (2) EU and UN Consolidated Sanctions List
base_url = "https://webgate.ec.europa.eu/europeaid/fsd/fsf/public/files/csvFullSanctionsList/content?token=dG9rZW4tMjAxNw"
response = requests.get(base_url)
df = pd.read_csv(response.text)

#print(type(response.text))
#converter = bs2json()
# Conver to CSV
#res_df = pd.toD
soup = BeautifulSoup(response.text, "html.parser")
#soup_df = pd.
#print(type(soup))
json = converter.convertAll(soup)