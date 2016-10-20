#Objective

This is a monkeyrunner bot, which mean that it's a python bot executed on android environement.
This bot play the [Stick Hero game](https://play.google.com/store/apps/details?id=com.ketchapp.stickhero) on android.
This is my second python bot, i created it to learn about monkeyrunner and mobile environement. Thus I found that this project can be interesting for anyone that want an introduction to python and/or monkeyrunner tool.
Feel free to update it if you like the project.

#Environement

This bot work perfectly on a Samsung Galaxy Note 2 with [Stick Hero game](https://play.google.com/store/apps/details?id=com.ketchapp.stickhero) already installed.
The script is executed from MacOS Sierra.


#Start

to start you have juste to Donwload the Android SDK if you dont have it and open the Monkeyrunner tool with the script to execute as an argument.
Monkeyrunner tool is located "for me" on "/Users/<UserName>/Library/Android/sdk/tools"
execution example :
cd /Users/<UserName>/Library/Android/sdk/tools
./Monkeyrunner /Users/Path/To/The/Script

This will wait till your phone is connected and then open the game and play it automatically.
Enjoy.

#Issues

Sometime device detection is not working well and i think that it's due to a java something or the process is not finishing correctly. Just closing the terminal and restarting it will fix the problem. If not redo the same process.

The bot is theoretically accurate, but technically not, it's because I am running python above the android layer, which is really slow, the more powerful the phone is the more you have accuracy.