import ui

def generate():
    i=int(r1.get())
    x=int(r2.get())
    if x < i :
        master.quit()
    else:
        ui.popupmsg("Please input the location where you would like your song ID list to be saved.")
        songlistlocation=ui.getdirectory()
        ui.popupmsg("Creating song ID list at " + songlistlocation)
        songid = open(songlistlocation+"/songs_setid.osm","w+") #create list
        for i in range(x):
            songid.write(i + '\n')
    
    
master = ui.Tk()
master.title('Generate List Time')
ui.Label(master, text="Ok look numbers only or else you'll make a thing that no work").grid(row=0)
ui.Label(master, text="Bottom of Range").grid(row=1)
ui.Label(master, text="Top of Range").grid(row=2)

r1 = ui.Entry(master)
r2 = ui.Entry(master)
r1.insert(10, 1)
r2.insert(10 ,10000)

r1.grid(row=1, column=1)
r2.grid(row=2, column=1)

ui.Button(master, text="Okay let's go", command=generate() )
  
master.mainloop()
