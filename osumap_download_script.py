import time
import ui
import urllib3

def download():
       ui.init()
       http = urllib3.PoolManager()
       ui.popupmsg("Select the .osm file you want to import maps from.")
       osm=ui.getfilename()
       if osm[len(osm)-4:]==".osm": #making sure selected file is of correct filetype
               ui.popupmsg("Downloading maps listed in: " + osm)
               with open(osm) as f:
                       for line in f:
                              mapdownload = http.request('GET',"https://bloodcat.com/osu/s/"+line)
                              with open("./dldest/"+line+".osz","wb") as osumap:
                                       osumap.write(mapdownload.data)
                                       mapdownload.release_conn()
                                       time.sleep(10)
       else:
              ui.popupmsg("Error! File selected not of type .osm! Please make sure your ID list has the correct filetype and try again.")
       ui.popupmsg("Success!")
       f.close()
       quit()
