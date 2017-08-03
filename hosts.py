#coding:utf-8
import os
import requests



resp = requests.get("https://raw.githubusercontent.com/racaljk/hosts/master/hosts")
html = resp.text

fp = open("../../../private/etc/hosts","w")
fp.write(html)
