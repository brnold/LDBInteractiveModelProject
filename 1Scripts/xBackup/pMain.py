import time, os, sys
import TouchCtrl, TouchObjs
#TouchStatus = TouchObjs.StatusOfTOs					# This is a single touch object
print "Kennel Model Running!"
TouchObjs.ConFigController()
time.sleep(0.05)
try:
	while 1==1:
		TouchStatus = TouchObjs.GetStatus()
		for idx in range (0, 32):
			if TouchStatus[idx] > 0:
				print TouchStatus[idx]
		time.sleep(0.5)
except KeyboardInterrupt:
	print ""
	print "Kennel Model Stopped!"

