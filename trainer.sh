#!/usr/bin/env bash

output="$(monkeyrunner StickHeroBot.py -t $1)"
IFS=' ' read -r -a array <<< "$output"
learningVariable="$(python machineLearningRoutine.py "${array[0]}" "${array[1]}")"
IFS=' ' read -r -a learningArray <<< "$learningVariable"
monkeyrunner StickHeroBot.py -x "${learningArray[0]}" "${learningArray[1]}" $2