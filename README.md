# Win, Loss & Amount of Games Counter within Recent 9 Hours - for League of Legends
![GitHub Banner](https://i.imgur.com/B3mCK4N.png)
## Description
This code updates your op.gg profile every 60 seconds, scrapes it - all in the background - and afterwards saves it into a file which is then created in the same directory called "stats.txt".
A Sample of what "stats.txt" could look like, dependant on your recent 9 hour stats:    Games: 8 | W3 - L4
This could be usefull to automate, your daily win loss ratio - as seen in twitch streams, where they're still doing it manually.

## How To:
1. Download the github repo
2. Open source.py
3. Input your League of Legends Ingame Username in line 64
4. Input your summoner region in line 65 (for example. EUW, NA)
5. Save & Close the file
6. Double click "source.py" to start it

## Adding Recent 9 Hour stats to OBS:
1. Add a 'Text (GDI+)' Source into your current scene
2. Add the created 'stats.txt' file location as source to that text, inside it's properties in OBS.
