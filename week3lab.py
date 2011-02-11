import sys
import urllib2
from BeautifulSoup import BeautifulSoup

search_url = 'http://briandorsey.info/uwpython/Internet_Programming_in_Python.html'
months = ['Jan ', 'Feb ', 'Mar ']
datelist = []

# so we can pretend to be IE 6
headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)'}

req = urllib2.Request(search_url, headers=headers)
response = urllib2.urlopen(req)
html = response.read()

soup = BeautifulSoup(html)

def create_date_list(text):
    for month in months:
        if month in text:
            datelist.append(text)

soup.find(text=create_date_list)
for date in datelist:
    print date

