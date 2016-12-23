# Objective

This is a monkeyrunner bot, which mean that it's a python bot executed on android environement.
This bot play the [Stick Hero game](https://play.google.com/store/apps/details?id=com.ketchapp.stickhero) on android.
This is my second python bot, i created it to learn about monkeyrunner and mobile environement. Thus I found that this project can be interesting for anyone that want an introduction to python and/or monkeyrunner tool.
Feel free to update it if you like the project.

After update this bot use google's machine learning tool "TensorFlow" to maximize it's score.

# Environement

This bot work perfectly on a Samsung Galaxy Note 2 with [Stick Hero game](https://play.google.com/store/apps/details?id=com.ketchapp.stickhero) already installed.
The script is executed from MacOS Sierra

# Getting Started

- First download [Android SDK](https://developer.android.com/studio/index.html), you dont need the full Android Studi + SDK, get just the command line tools.

- Next you have to add the monkeyrunner to your path variable for [Mac/Linux](http://www.troubleshooters.com/linux/prepostpath.htm) and this is for [Windows](http://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/)

- Then using [HarambeRunner](https://github.com/Boussama/HarambeRunner) you can get the coordinates of the buttons that are specifique to your device and replace them in the StickHeroBot.py file at line 83, it's commented so it's pretty easy.

# Start

- machineLearningRoutine.py is an independant file that givin two array of X's and Y's will calculate the best fit for the equation Y = AX + B

- StickHeroBot.py is the main file that pilote the device, you can use it to farm exeperience to use later or juste give it correct value to play the game. The value farmed and the correct variable are related to machine learning capability

- This is why to facilitate all the process you can juste use the trainer.sh file to farm values, calculate the best fit and play the game.

- Example of the execution "./trainer.sh 50 80" where 50 is the number of value to get which then will be calculated and 80 will be the number of repetition after the bot get experienced.

[![The bot execution in action](http://img.youtube.com/vi/gxfLE0se99c/0.jpg)](https://www.youtube.com/watch?v=gxfLE0se99c)
# Issues

Sometime device detection is not working well and it's due to a monkeyrunner bug, Just closing the terminal and restarting it will fix the problem. If not redo the same process.
This bug is not fixed untill now 23 December 2016.

look to the fixConnection.sh if you dont want this manual methode but it's for advanced linux user.