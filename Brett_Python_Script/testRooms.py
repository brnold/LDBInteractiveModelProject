import room

electroidList = [200, 201, 202, 203, 204]

room.updateRoomList(electroidList)
room.printRoomList()
room.removeExpiredRooms() # get rid of all the old unplayed rooms
room.printRoomList()
room.removeNonTouchedRooms(electroidList)
room.printRoomList()
numUnplayedRooms = room.getNumberUnplayedRooms()

room.printRoomList()

print "Number of the unplayed rooms" 
print numUnplayedRooms

if numUnplayedRooms == 1: #best case
	#naiave way of doing this
	room.playFirstUnplayedRoom()