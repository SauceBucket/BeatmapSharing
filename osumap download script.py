import webbrowser
import os
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()
osm=askopenfilename()
print("\nretrieving files from: " + osm)
with open(osm) as f:
        for line in f:
                webbrowser.open("https://osu.ppy.sh/beatmapsets/"+line+"/download")
                time.sleep(20)
f.close()
