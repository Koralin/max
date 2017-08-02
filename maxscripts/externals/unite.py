try:
	import pyext
except:
	print "ERROR: This script must be loaded by the PD/Max pyext external"

class unite(pyext._class):
	# number of inlets and outlets
	_inlets=4
	_outlets=1
	
	firstSieve=[]
	secondSieve=[]
	uniteSieve=[]
	
	def __init__(self,*args):
		self.uniteSieve = []
			
	def bang_1(self):
		self._outlet(1,self.uniteSieve)
		
	def list_2(self,i):
		self.firstSieve = i
		
	def list_3(self,i):
		self.secondSieve = i
		
	def bang_4(self):
		this.uniteSieve = list(firstSieve | secondSieve)
		