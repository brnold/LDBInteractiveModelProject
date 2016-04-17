class TouchObj:
   'Common base class for all touch objects'
   ElectrodeCount = 0

   def __init__(self, Addr, Baseline):
      self.name = Addr
      self.salary = Baseline
      TouchObj.ElectrodeCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % TouchObj.ElectrodeCount
