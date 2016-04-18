#Composed by Benjamin R. Nold
#

import time, soundFunctions

class room:

    def __init__(self, electrode):
        self.electrode = electrode    # instance variable unique to each instance
        self.timeInit = time.time()
        self.playedStatus = false

    def playSound():
    	soundFunctions.playSoundFromElectrode(self.electrode)
    	self.playedStatus = true

    def getTimeSincePlayed():
    	return (time.time() - self.timeInit)

     def getName():
	return self.electrode