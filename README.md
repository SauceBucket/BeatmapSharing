# Beatmap Sharing

A attempt at pulling maps en masse from server

Firsty, this was made for windows, have 0 idea if it will work for mac/linux but I see no reason why it shouldn't other than file manip garbage

Using this script shouldnt be too difficult. If you want to package up your beatmap folder then use the search script.

If you want to take a packaged up beatmap set and download all the maps, then use the donloading script. 

Both scripts have prompts for input with little input checking so dont input something dumb or it no work.

let me know @ saucy#7035 or saucy on osu if you have issues or wanna talk to me about this project.

also the time in between beatmap downloads is by defualt 20 seconds, it should work with less if your internet speed is god tier, but if you need to change the speed slower because downloads are stacking on top of each other, then open the download script in notepad++ and change the number in the time.sleep(20) to a larger number. (its measured in seconds)
