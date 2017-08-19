try:
	import pyext
except:
	print "ERROR: This script must be loaded by the PD/Max pyext external"

class xenOp(pyext._class):
	# number of inlets and outlets
	_inlets=4
	_outlets=2
	
	leftSieve=[]
	rightSieve=[]
	
	union=[]
	intersection=[]
			
	def bang_1(self):
		self._outlet(1,self.union)
		self._outlet(2,self.intersection)
		
	def list_2(self,i):
		self.leftSieve = i
		
	def list_3(self,i):
		self.rightSieve = i
		
	def bang_4(self):
		populateSieves(this.leftSieve, this.rightSieve)
		
	def populateSieves(l, r):
		union = list(set(l) | set(r))
		intersection = list(set(l) & set(r))
			
		