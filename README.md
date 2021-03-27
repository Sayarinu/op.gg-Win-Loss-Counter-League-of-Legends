# Win, Loss & Amount of Games Counter for League of Legends
## Description:
This code updates your op.gg profile every 60 seconds, scrapes your wins and losses which occured within the recent 9 hours from it (invisibly in background) and afterwards saves it into a file which is created in the same directory called "stats.txt".
A Sample of what "stats.txt" could look like, dependant on your recent 9 hour stats: Games: 8 | W 3 - L 5
This could be usefull to automate, your daily win loss ratio - as seen in twitch streams, where they're still doing it manually.

## Dependencies:

	pip install requests-html

## How To:
1. Download the github repo
2. Open source.py
3. Input your League of Legends Ingame Username in line 64
4. Input your summoner region in line 65 (for example. EUW, NA)
5. Save & Close the file
6. Double click "source.py" to start it
7. Leave it running, while you play your games

Also in line 36 you can higher or lower the time it counts as a day. If you add '8 Hours' for example, it will in return only count games that were played within a span of 7 hours since 8 hours is then a blacklisted term. You can even edit the way it outputs the Win Loss counter in Line 55.

## Adding stats to OBS:
1. Add a 'Text (GDI+)' Source into your current scene
2. Add the created 'stats.txt' file location as source to that text, inside it's properties in OBS.

## Additional Knowledge:
I'm fully aware that there's the Riot Games API that will exactly replicate the functionality of this code, but it required me as a developer to first register an permanent API key through an form for my application, which I don't wanna bother doing. It would've taken too long for me to fill it out and them to accept it, so I've quickly written this instead 😅

If you like it, please star the Repo 👍🏻
