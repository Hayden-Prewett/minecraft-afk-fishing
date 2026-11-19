# AFK Fishing Script for Minecraft
A python script that detects when a fish is caught in Minecraft and reels it in. The process repeats, allowing you to AFK farm fishing.

## Instructions
1. Download the executable or python script
2. Open your world in full screen
3. Turn on closed captions / subtitles
4. Get a fishing rod. For maximum results, use these enchantments:
- Mending (Otherwise your rod will break)
- Unbreaking III
- Luck of the Sea III (ideal for faster results)
- Lure III
5. Equip your fishing rod. Do not cast it.
6. Start the python script or executable and switch to the full screen minecraft within 10 seconds.

If this does not work, please create an issue in the GitHub repository and state your setup (OS, minecraft version, etc)

## How it works
The python script captures the screen and reads the captions. It looks for "fishing bobber splashes" and right clicks to reel in. Then it right clicks again to cast. This loops until the application is closed.
