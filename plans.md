# BeatmapSync
A attempt at pulling maps en masse from osu beatmap mirror websites

first goal is to pull the id codes from beatmap folders in osu!/songs/ and place the numbers into a .txt file seperated by <br>

second goal is to request those numbers from the appropriate beatmap mirror server

these two should be seperate scripts so you can theoretically take any text file and use that for the request not just use the one thatthe program made on your machine but instead borrow another user's beatmap collection and do the function:

updated folder = old beatmaps ⋃ new beatmaps pulled from mirror server


next step is profit??



notes:

the number used to sort/order beatmaps is the SET NUMBER. search by set number on mirror websites to find the correct map.



 issue if song directories that do not have set ids yet (i.e. your maps you made but not uploaded) mucking up the process.


make a tool to compare two text files and remove duplicate song ids from the list so you dont download songs twice 
(using ppys resources and your own more than necessary)
 
make a option to create osm files with custom ranges of beatmap id #s
