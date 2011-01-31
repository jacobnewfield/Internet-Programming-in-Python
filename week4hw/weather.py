"""
Input a 5 digit zipcode and output corresponding city and current temperature.
Resources pulled from NOAA web API service and USPS website
"""
import sys
import urllib
import urllib2
import re
from time import gmtime, strftime
from BeautifulSoup import BeautifulSoup

#Default zipcode is zipcode for Seattle, WA
zcode = 98119

#Check command line arguments for zipcode else prompt enduser
if len(sys.argv) > 1:
    word = sys.argv[1]
else:
    ziptmp = raw_input('Enter a 5 digit zipcode: ')
    p = re.compile('[0-9]{5,5}')
    if p.match(ziptmp):
        zcode = ziptmp
    else:
        print '\"%s\" is not a valid zipcode. Using %s...\n' % (ziptmp, zcode)

#Get today's and tomorrow's date in time series format
ts = strftime("%Y-%m-%dT%H:%M:%S", gmtime())
ts1 = ts.split('-')
ts2 = ts1[2].split('T')
ts3 = ts1[0] + '-' + ts1[1] + '-' + str(int(ts2[0]) + 1) + 'T' + ts2[1]

ts = urllib.quote(ts)
ts3 = urllib.quote(ts3)

# so we can pretend to be IE 6
headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)'}

#Create request/response for zipcode to city
zurl = 'http://zip4.usps.com/zip4/zcl_3_results.jsp'
data = urllib.urlencode({'zip5':zcode})
zreq = urllib2.Request(zurl, data, headers=headers)
response = urllib2.urlopen(zreq)
zhtml = response.read()
response.close()

#Create request/response for today's temperature
wparams = 'whichClient=NDFDgenMultiZipCode&lat=&lon=&listLatLon=&lat1=&lon1=&lat2=&lon2=&resolutionSub=&listLat1=&listLon1=&listLat2=&listLon2=&resolutionList=&endPoint1Lat=&endPoint1Lon=&endPoint2Lat=&endPoint2Lon=&listEndPoint1Lat=&listEndPoint1Lon=&listEndPoint2Lat=&listEndPoint2Lon=&zipCodeList=%s&listZipCodeList=&centerPointLat=&centerPointLon=&distanceLat=&distanceLon=&resolutionSquare=&listCenterPointLat=&listCenterPointLon=&listDistanceLat=&listDistanceLon=&listResolutionSquare=&citiesLevel=&listCitiesLevel=&sector=&gmlListLatLon=&featureType=&requestedTime=&startTime=&endTime=&compType=&propertyName=&product=time-series&begin=%s&end=%s&maxt=maxt&mint=mint&Submit=Submit' % (zcode, ts, ts3)
wurl = 'http://www.weather.gov/forecasts/xml/SOAP_server/ndfdXMLclient.php?' + wparams
wreq = urllib2.Request(wurl, headers=headers)
response = urllib2.urlopen(wreq)
whtml = response.read()
response.close()

#soup for zipcode to city
zsoup = BeautifulSoup(zhtml)
#print zsoup.prettify()

#soup for weather/temperature
wsoup = BeautifulSoup(whtml)
#print wsoup.prettify()

#For printing format
degree_symbol = unichr(176).encode("latin-1")

#Get city from zipcode
def zip_funct(text):
    text = text.lower()
    if 'actual city name in' in text:
        return True
zip_text = zsoup.find(text=zip_funct)
if zip_text:
    zdiv = zip_text.findNext(name='b')
    cityorzip = zdiv.getText()
else:
    cityorzip = zcode

print 'Today\'s temperature for %s:' % cityorzip

#Get today's high temperature of city/zip
def max_tmp(text):
    if 'Daily Maximum Temperature' in text:
        return True
maximum_temp = wsoup.find(text=max_tmp)
if maximum_temp:
    maxdiv = maximum_temp.parent.findNextSibling(name='value')
    print '\tHighs: %s %sF' % (str(maxdiv.getText()), degree_symbol)
else:
    print 'Today\'s high temperature not found'

#Get today's low temperature of city/zip
def min_tmp(text):
    if 'Daily Minimum Temperature' in text:
        return True
minimum_temp = wsoup.find(text=min_tmp)
if minimum_temp:
    mindiv = minimum_temp.parent.findNextSibling(name='value')
    print '\tLows:  %s %sF' % (str(mindiv.getText()), degree_symbol)
else:
    print 'Today\'s low temperature not found'
    


