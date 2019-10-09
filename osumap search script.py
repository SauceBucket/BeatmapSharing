import os

songpath = r'C:\Users\Pizza\AppData\Local\osu!\Songs'

songid = open("songs_setid","w+")

for entry in os.listdir(songpath):
    if os.path.isdir(os.path.join(songpath,entry)):
        x = entry.split(' ')[0]
        songid.write(x.split('+')[0]) #//some maps are seperated by + too
        songid.write('\n')

songid.close()


