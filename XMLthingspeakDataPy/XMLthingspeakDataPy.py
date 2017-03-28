import urllib
import xml.etree.ElementTree as ET

input=urllib.urlopen('https://thingspeak.com/channels/245802/field/1.xml').read()
stuff=ET.fromstring(input);
lst=stuff.findall('feeds/feed')
print "total Heart Rate values: ",len(lst)
for item in lst:
    print item.find('field1').text
