# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:07:54 2023

@author: Asus
"""

import requests
from pprint import pprint as print

sura = input("Sura raqamini kiriting: ")
oyat = input("Oyat raqamini kiriting: ")
tafsir = "uzb-muhammadsodikmu"

url_sura = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}.json"
url_oyat = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json"

r1 = requests.get(url_oyat)
print(r.status_code)
res1 = r1.json()['text']
print(res)


if sura=True:
    print(res1)