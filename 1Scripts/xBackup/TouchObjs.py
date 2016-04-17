import TouchCtrl
# Touch Objects.
# Touch objects configuration.
# Touch objects status read.
# 4 touch objects in a sub-network by 8 sub-networks.
# 32 touch objects.
Status = 0
TOs =	[
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(),		# net 0
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(),		# net 1
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(),		# net 2
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(),		# net 3
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(),		# net 4
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(),		# net 5
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(),		# net 6
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj()		# net 7
		]

StatusOfTOs =	[
					Status, Status, Status, Status,		# net 0
					Status, Status, Status, Status,		# net 1
					Status, Status, Status, Status,		# net 2
					Status, Status, Status, Status,		# net 3
					Status, Status, Status, Status,		# net 4
					Status, Status, Status, Status,		# net 5
					Status, Status, Status, Status,		# net 6
					Status, Status, Status, Status		# net 7
		]
def ConFigController():
	idx = 0
	for idx in range (0,32):						# idx will range from 0 to 31
		TOs[idx].ConFigController()

def GetStatus():
	idx = 0
	for idx in range (0,32):						# idx will range from 0 to 31
		StatusOfTOs[idx] = TOs[idx].displayStatus()
#	print StatusOfTOs
	return StatusOfTOs
