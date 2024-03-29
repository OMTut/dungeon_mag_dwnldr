# Dungeon Magazine Downloader

I put together this script to download Dungeon Magazine from archive.org. I couldn't find a list so it iterates a range up to 221. I noticed two formats for the download url so this tries one variation, then the other before trying to download.

I also put a 30sec delay between requests. I havern't done anything like this before. I checked the robots.txt file and I believe it's ok to use a script to download, but I put the 30sec delay on there be nice and not get blocked.

## Trouble
If there is something that interrupts the download, it doesn't cycle back and recheck them. This is simply a loop iterator. Some magazines might get missed.

## Dependencies
requests
the rest is from the standard library I believe (I'm new to python)