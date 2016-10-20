from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import time

def sumRVB(rvbTuple):
	return rvbTuple[1]+rvbTuple[2]+rvbTuple[3]

def pressFor(periode, withSnapshot):

	device.touch(350,650,MonkeyDevice.DOWN)
	time.sleep(periode)
	device.touch(350,650,MonkeyDevice.UP)

	if withSnapshot:
		inGameSnapshot = device.takeSnapshot()
		inGameSnapshot.writeToFile('/Users/MacBook/offlineDesktop/python/StickHeroBot/'+str(periode)+'.png','png')

def getTheRedDot(withSnapshot):
	global redDotCord
	#process information to get the correct coordinate
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
			# Even if my numbers are write the device is taking too long to press 
			# so i just subtracted an arbitrary number so this will work
			print redDotCord
			if withSnapshot:
				redDotSnap.writeToFile('/Users/MacBook/offlineDesktop/python/StickHeroBot/redDotSnap#'+str(i)+'.png','png')

def pressTheShareButton():
	inGameSnapshot = device.takeSnapshot()
	pauseButton = inGameSnapshot.getSubImage(shareButtonBox)
	if pauseButton.sameAs(shareImageReference, 0.9):
		device.touch(550,900,MonkeyDevice.DOWN_AND_UP)

def runTheGame():
	#run the game
	device = MonkeyRunner.waitForConnection()
	runComponent = package + '/' + activity
	device.startActivity(component=runComponent)

def tapTheBeginButton():
	#tap to begin the game
	device.touch(350,650,MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(2)

package = 'com.ketchapp.stickhero'
activity = 'com.ketchapp.stickhero.stickhero'
shareImageReferenceUrl = '/Users/MacBook/offlineDesktop/python/StickHeroBot/shareReference.png'
redSquareReferenceUrl = '/Users/MacBook/offlineDesktop/python/StickHeroBot/redSquareReference.png'
playerSubImageBox = (115, 865, 47,50)
shareButtonBox = (270, 690, 171,61)
redLineY = 905
bridgeLineX = 160
redDotSnapBox = (0, 903, 720, 9)

#in game variables
redDotCord = 0
inGameSnapshot = None
#run the game
device = MonkeyRunner.waitForConnection()
runComponent = package + '/' + activity
device.startActivity(component=runComponent)

shareImageReference = MonkeyRunner.loadImageFromFile(shareImageReferenceUrl)
redSquareReference = MonkeyRunner.loadImageFromFile(redSquareReferenceUrl)

MonkeyRunner.sleep(6)

tapTheBeginButton()


for i in range(5):
	time.sleep(5)
	getTheRedDot(False)
	#The 0.0014705 value is calculated by taking two snapshot and comparing value
	#it's fairly easy but is not covered here
	pressFor( redDotCord*0.0014705, False)
	time.sleep(8)
	pressTheShareButton()