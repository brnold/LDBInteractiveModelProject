#Composed by Benjamin R. Nold
#

import time, soundFunctions

roomList = []

timeLimitAfterPlay  = 5;

# def updateRoomList(electroidList):
# 	global roomList
# 	for idx in range(0, len(electroidList)):
# 		new_list = [x for x in myList if x.age == 30] #check and see if we allready have the object.
# 		if(len(new_list)==0) #k, add the object
# 			roomList.append(electroidList[idx])

def updateRoomList(electroidList):
	global roomList
	#search roomlist and see if the element is in the list
	for idx in range(0, len(electroidList)):
		if electroidList[idx] not in roomList:
			roomList.append(room(electroidList[idx]))

#takes away the last element, why?
def removeNonTouchedRooms(electroidList):
	global roomList
	for rooms in roomList:
		for elect in electroidList:
			if elect == rooms.getName(): #if the element is there, break
				break
	roomList.remove(rooms)	#remove the element


def removeExpiredRooms():
	global roomList
	for i in range(0, len(roomList)):
		if roomList[i].getTimeSincePlayed() > timeLimitAfterPlay:
			roomList.remove(roomList[i]) # take away the expired room and make it availible to be played

def getNumberUnplayedRooms():
	global roomList
	countUnplayed = 0
	for rooms in roomList:
		if rooms.getPlayedStatus() == False:
			countUnplayed=countUnplayed+1;
	return countUnplayed

def playFirstUnplayedRoom():
	global roomList
	for rooms in roomList:
		if rooms.getPlayedStatus == False:
			soundFunctions.playSoundFromElectrode(rooms.getName())
			rooms.setPlayedStatus()
			break

def printRoomList():
	global roomList
	for rooms in roomList:
		print rooms.getName()
	print "-------------------"

class room:

    def __init__(self, electrode):
        self.electrode = electrode    # instance variable unique to each instance
        self.timeInit = time.time()
        self.playedStatus = False

    def __contains__(self, x):
        if x == self.electrode:
        	return True
        else:
        	return False

    def playSound(self):
    	soundFunctions.playSoundFromElectrode(self.electrode)
    	self.playedStatus = True

    def getTimeSincePlayed(self):
    	return (time.time() - self.timeInit)

    def getName(self):
	return self.electrode

    def getPlayedStatus(self):
    	return self.playedStatus

    def setPlayedStatus(self):
    	self.status = True