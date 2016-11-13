import congress.models
import urllib2
import sys
import json

def savePerson(person):
    personObject = person.get('person')
    extras = person.get('extra')
    personModel = congress.models.Person()
    personModel.first_name = personObject.get('firstname')
    personModel.last_name = personObject.get('lastname')
    personModel.district = person.get('district')
    personModel.state = person.get('state')
    personModel.contact_page = extras.get('contact_form')
    personModel.person_id = personObject.get('id')
    personModel.title = person.get('title')
    personModel.title_long = person.get('title_long')
    personModel.office_addr = extras.get('address')
    personModel.party = person.get('party')
    personModel.twitter_username = personObject.get('twitterid')
    personModel.save()
    print personModel


result = urllib2.urlopen("https://www.govtrack.us/api/v2/role?current=true&limit=600")
jsonDecodedResult = json.load(result)
basicPersonObjects = jsonDecodedResult.get("objects")
for person in basicPersonObjects:
    savePerson(person)
    #print person

personsBaseURL = "https://www.govtrack.us/api/v2/person/"
allCurrentParams = {"current":"true"}


def getAllPersons():
    result = urllib2.urlopen("https://www.govtrack.us/api/v2/role?current=true&limit=")
    jsonDecodedResult = json.load(result)
    basicPersonObjects = jsonDecodedResult.get("objects")
    print basicPersonObjects
    print '*** HERE ***'
    for person in basicPersonObjects:
        #savePerson(person)
        #print person

def main():
    print "*********MAIN*********"
    getAllPersons()

if __name__ == "__main__":
    main()