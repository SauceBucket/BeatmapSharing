import os
import ui

ui.init()
#select osu! song path directory
ui.popupmsg("Please select your osu! song path directiory.")
songpath=ui.getdirectory()
ui.popupmsg("You have selected your song directory path as: " + songpath)
#select location in which list will be created
ui.popupmsg("Please input the location where you would like your song ID list to be saved.")
songlistlocation=ui.getdirectory()
ui.popupmsg("Creating song ID list at " + songlistlocation)

songid = open(songlistlocation+"/songs_setid.osm","w+") #create list
#for each folder in the song directory, chop off the id number in the beginning of the name and write it to the list
for entry in os.listdir(songpath):
    x = entry.split(' ')[0].split('+')[0]
    songid.write(x + '\n')

#close file and quit
ui.popupmsg("Success! Your .osm containing your map IDs has been created at " + songlistlocation + "/songs_setid.osm")
songid.close()
quit()