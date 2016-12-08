from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import time
import sys

def sumRVB(rvbTuple):
	return rvbTuple[1]+rvbTuple[2]+rvbTuple[3]

def pressFor(periode, training):

	global trainingMaterial
	global trainingPoints

	device.touch(350,650,MonkeyDevice.DOWN)
	time.sleep(periode)
	device.touch(350,650,MonkeyDevice.UP)

	if training:
		inGameSnapshot = device.takeSnapshot()
		stickLength = 0
		for i in range(stickSourceY):
			if inGameSnapshot.getRawPixelInt(stickSourceX,stickSourceY-i) == blackIntValue:
				stickLength = i
			else:
				break
		trainingMaterial.append(stickLength)
		trainingPoints.append(periode)


def getTheRedDot():
	# process information to get the correct coordinate of the red square

	global redDotCord
	inGameSnapshot = device.takeSnapshot()
	i=160
	notSame = True

	while notSame and i<707 :
		i = i+1

		redDotSnap = inGameSnapshot.getSubImage((i,redLineY,12,10))

		if redDotSnap.sameAs(redSquareReference, 0.5):
			notSame = False
			redDotCord = (i-120)
			if redDotCord < 0:
				redDotCord = 0

def pressTheShareButton():
	inGameSnapshot = device.takeSnapshot()
	pauseButton = inGameSnapshot.getSubImage(shareButtonBox)
	if pauseButton.sameAs(shareImageReference, 0.9):
		device.touch(550,900,MonkeyDevice.DOWN_AND_UP)

def runTheGame():
	global device
	runComponent = package + '/' + activity
	device.startActivity(component=runComponent)
	MonkeyRunner.sleep(6)
	device.touch(350,650,MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(2)


package = 'com.ketchapp.stickhero'
activity = 'com.ketchapp.stickhero.stickhero'

#please replace this by the absolute path to the directory
currentDirectory = '/Users/MacBook/offlineDesktop/python/StickHeroBot/'

shareImageReferenceUrl = currentDirectory+'shareReference.png'
redSquareReferenceUrl = currentDirectory+'redSquareReference.png'
playerSubImageBox = (115, 865, 47,50)
shareButtonBox = (270, 690, 171,61)
redLineY = 905
bridgeLineX = 160
stickSourceX = 162
stickSourceY = 905
blackIntValue = -16777216
redDotSnapBox = (0, 903, 720, 9)
trainingMode = False
openAutomatically = False
trainingRepetition = 1
trainingMaterial = []
trainingPoints = []

#these are preprocessed value but you can make your own
b = 0.8300544 #5.69149542 #14.53295326
a = 684.39886475 #670.55163574 #640.38397217

# in game variables
redDotCord = 0
inGameSnapshot = None

# the argument have limitation which depend from the os. For example in the MacOs it's limited to 4 argument
if len(sys.argv) > 1:
	if "-t" in sys.argv:
		trainingMode = True
		trainingRepetition = int(sys.argv[sys.argv.index("-t") + 1])
	if "-o" in sys.argv:
		openAutomatically = True
	if "-x" in sys.argv:
		a = float(sys.argv[sys.argv.index("-x") + 1])
		b = float(sys.argv[sys.argv.index("-x") + 2])
		trainingRepetition = int(sys.argv[sys.argv.index("-x") + 3])


shareImageReference = MonkeyRunner.loadImageFromFile(shareImageReferenceUrl)
redSquareReference = MonkeyRunner.loadImageFromFile(redSquareReferenceUrl)

device = MonkeyRunner.waitForConnection()

if openAutomatically:
	runTheGame()


# how many time do I have to train ?
# I choose 10 as a minimum so i cant get 0.01*10=0.1 which is the least we can press
# Same for 85 as a maximum else we have a stick that step outside the border
if trainingMode:
	rangeToDo = range(10,86, int((85-10)/(trainingRepetition-1)))
else:
	rangeToDo = range(trainingRepetition)

for i in rangeToDo:

	time.sleep(5)
	getTheRedDot()

	#due to the slow process of the monkeyrunner the difference between to stick value will not give an accurate value
	#and this's why I have to make some machine learning to be as accurate as possible

	# y=ax+b
	# y is the stick height wich have to be equal to the red square distance
	# x is the time to press the screen
	# a & b are variable computed with machine learning

	if trainingMode:
		pressFor(float(i * 0.01), trainingMode)
	else:
		pressFor( (float(redDotCord) - b)/a , trainingMode)

	time.sleep(6)
	pressTheShareButton()

if trainingMode:
	dataToProcess = str(trainingPoints).replace(" ","")
	dataToProcess += " "+ str(trainingMaterial).replace(" ","")
	print(dataToProcess)