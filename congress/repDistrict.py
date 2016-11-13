import urllib2
import re

googleApiKey = "AIzaSyAzgMVEQQjTbh7CnXyAfEYG_CPvWL8GYvk"

pattern = "ocd-division/country:us/state:\w\w/cd:[0-9]+"

def getRepDistrict(address):
    requestURL = "https://www.googleapis.com/civicinfo/v2/representatives?address=" + address.replace(" ", "+") + "&includeOffices=false&key=" + googleApiKey
    response = urllib2.urlopen(requestURL).read()
    match = re.search(pattern, response, flags=0)
    
    if match:
        obj = match.group(0)
        removeState = obj.replace("ocd-division/country:us/state:", "")
        removeCd = removeState.replace("/cd:", " ")
        return removeCd
    else:
        return "Not found"