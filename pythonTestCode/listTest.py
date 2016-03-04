#Baseline configuration settings
ucBaseLine = [0x2b,  # Data block starting address
                                              0x01,   # MHDR
                                              0x01,   # NHDR
                                              0x0e,   # NCLR
                                              0x00,   # FDLR
                                              0x01,   # MHDF
                                              0x05,   # NHDF
                                              0x01,   # NCLF
                                              0x09,   # FDLF
                                              0x00,   # NHDT
                                              0x00,   # NCLT
                                              0x00]  # FDLT



#This function takes a list of 
def  listHextToInt(theList):
	for hexNum in theList:
		theList.append( int(hexNum))
	return intList                                      



#listOfInt = listHextToInt(ucBaseLine)

print listOfInt[1]