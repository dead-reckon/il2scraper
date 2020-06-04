
The syntax and process for running the tool is pretty much like it was for the old tool - this is how I do it at any rate

1. create a new temp folder with a short/easy name (for example, c:\gtptemp)
2. copy unGTP-IL2.exe into that temp folder
3. copy the game's .gtp file(s) you want to extract into that temp folder (for example, the skins.gtp file)
4. open a command window (run cmd from the start menu)
5. in the command window, navigate (using cd\ commands etc.) so that you are in that temp folder (probably not strictly necessary but makes the typing of the next step much simpler)
6. type the following: unGTP-IL2 <name of .gtp file you want to extract> <name of folder into which you want the extracted files to be placed>

In my example above, assuming you want to extract the skins.gtp file, you would type the following (without the quotes, of course):  "unGTP-IL2 skins.gtp skins"

and then hit enter - when you do, it will create a new folder ("skins") in your gtptemp folder and extract all the contents of skins.gtp into that new skins folder

I always just name the new folders the same as the name of the .gtp file I'm extracting - easier to keep things straight that way.  And by navigating into the gtptemp folder first in the command window, I save the trouble of having to type all the pathing info for the files and folders.

[EDIT] to find the game's .gtp files, just open a Windows Explorer window and search for ".gtp" in your main game folder.


BTW the plane data can be found in Swf.gtp
swf/il2/worldobjects/planes/