import os
drive = 'C'
print("please input the letter of which drive your osu! folder is on.")
drive=input()

rootDir = '/'
for dirName, subdirList, fileList in os.walk(rootDir):
    if dirName.endswith('osu!\Songs'):
        print(dirName)
        songpath = drive + ':' + dirName
print(songpath)
songid = open("songs_setid.txt","w+")

for entry in os.listdir(songpath):
    if os.path.isdir(os.path.join(songpath,entry)):
        x = entry.split(' ')[0]
        songid.write(x.split('+')[0]) #//some maps are seperated by + too
        songid.write('\n')

songid.close()



 

        
    
