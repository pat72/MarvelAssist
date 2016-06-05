# MarvelAssist
A script to help execute tool assisted sequences. This is considered to be a programmer's tool and lacks a UI and proper error handling. It will be difficult to use if you aren't familiar with programming. It is currently set up for Ultimate Marvel vs Capcom 3 on xbox 360, but could be tweaked for other games/systems. **This tool has inaccuracies due to various reasons so it is best suited for relatively short sequences**.

## Requirements

- Python 3.4 installed. It does not run properly in older versions.
- A titanone/cronus adapter (I use the titanone and have not yet confirmed that it works for the cronus)
- The titanone/cronus API (included with this project) 
 more info: https://www.consoletuner.com/kbase/device_api_print.htm
- The titanone/cronus driver default software/driver installed.
- The titanone/cronus adapter configured to target xbox 360.
- A windows PC (any version of windows your adapter supports probably)

## Notes on the titanone/cronus
-Be careful if you're thinking of buying one of these devices for this. First you need to know that the tool assist is somewhat inaccurate and eventually misses a frame or holds an input for a frame too long. This is due to the game and the tool operating on different time loops which eventually desync. These devices have also been reported to damage usb ports on systems in the past so use them at your own risk. 

## Setup
- Install the software/driver that comes with the device. Make sure your device is set to target xbox 360. After you've done this you can close the device's default software.

- Connect an xbox controller into the adapter and the adapter into the xbox 360. Then connect the adapter to your PC using the side port on the adapter.

- Start up UMVC3, Go to training mode, pick your characters and then the map. By default the script is setup assuming your button config is "Type A" so either change your controls in game or alter the script. Now run the script from within python. By default the program runs a test script which should just dash around.

## Scripting
To write your own scripts, simple create text files and place them in the scripts folder. Then change which file the program loads within the code. The format is as follows:

- Each line begins with a number. This determines how many frames to repeat this action. Due to the inaccuracies, 2 frames is a safe minimum to ensure that input is not skipped entirely.
- After the number you write your inputs separated by spaces which are by default:
```
L M H S up down left right back start A1 A2
```
- You can also repeat a segment by using square brackets like so:
```
2 [
2 L M
2
2 down
]
```
This will press L and M for two frames, do nothing for 2 frames, and then press down for two frames. Then this entire sequence will be done a second time due to the square brackets.

- There is not much checking on the format of your scripts so be sure to write them carefully.
