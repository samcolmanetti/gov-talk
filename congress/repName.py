from govtrack.api import GovTrackClient
import urllib

client = GovTrackClient()
#urllib.parse.urlencode("https://www.govtrack.us/developers/api")
person = client.person({'lastname':'Kennedy'})
print person