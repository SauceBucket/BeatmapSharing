import webbrowser
import time
import ui

ui.init()

ui.popupmsg("Select the .osm file you want to import maps from.")
osm=ui.getfilename()
if osm[len(osm)-4:]==".osm": #making sure selected file is of correct filetype
    ui.popupmsg("retrieving files from: " + osm)
    with open(osm) as f:
            for line in f:
                    webbrowser.open("https://osu.ppy.sh/beatmapsets/"+line+"/download")
                    time.sleep(20)
else: #print incorrect filetype error message
    ui.popupmsg("Error! File selected not of type .osm! Please make sure your ID list has the correct filetype and try again.")
ui.popupmsg("Success!")
f.close()
quit()