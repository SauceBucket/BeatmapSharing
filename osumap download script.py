import webbrowser
import os
import time
print("please select a text file from displayed. \nIf not displayed, please make sure that it is in the same folder as this script.")
i=0
x= [0,0,0,0,0,0,0,0,0,0]
for file in os.listdir("."):
    if file.endswith(".osm"):
        print("option " + str(i+1) + " " + os.path.join(os.getcwd(),file) )
        x[i]=str(os.path.join(os.getcwd(),file))
        i=i+1
print("input a single integer option from the list")
option=int(input())
while option >= i+1 :
        print("please choose from the options listed")
        option=int(input())
osm=str(x[option-1])
print("you chose option " + str(option) +"\n" + "whose path is "+ osm +"\nretrieving files...")
with open(osm) as f:
        for line in f:
                webbrowser.open("https://osu.ppy.sh/beatmapsets/"+line+"/download")
                time.sleep(20)
f.close()         
