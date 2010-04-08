from sickbeard.tvclasses import TVEpisode
from sickbeard.tvapi import store
from sickbeard.tvapi.tvapi import getTVShow
from sickbeard.tvapi.tvapi_classes import TVEpisodeData

# use case: parsing a random scene name, generating temp objects for it, and throwing them away
#           for example, when parsing the RSS names and finding an episode we already have
# we take The.Office.US.S01E02E03.Blah.avi and found:
#
# series name: The Office US
# season: 1
# episodes: (2,3)
#
# we then look up the tvdb id (internet or local DB) and determine that the show is one we want
# tvdb_id: 73244

# the use case starts here
# use the tvdb id to make the show data
myShow = getTVShow(73244) # really I'd just look it up in sickbeard.showList

# in real life this line wouldn't be necessary since the metadata database would always have the latest required info
myShow.update()
store.add(myShow)
for x in myShow.show_data.seasons:
    print myShow.show_data[x]

print "1. %s (%r)" % (myShow.show_data.name, myShow.tvdb_id)

epObj = TVEpisode(myShow)

epObj.addEp(1,2)
print "2. %s" % ", ".join(["%dx%d - %s" % (x.season, x.episode, x.name) for x in epObj.episodes_data])
epObj.addEp(1,3)
print "3. %s" % ", ".join(["%dx%d - %s" % (x.season, x.episode, x.name) for x in epObj.episodes_data])
store.commit()
for x in myShow.nextEpisodes():
    print x.season, x.episode, x.aired

print "4. status:", epObj.status
epObj.status = 55
print "5. status:", epObj.status

epObj = TVEpisode(myShow)
print "6. status:", epObj.status
epObj.addEp(6,21)
print "7. status:", epObj.status
epObj.status = 66
print "8. status:", epObj.status
