try:
	import pyext
except:
	print "ERROR: This script must be loaded by the PD/Max pyext external"

class residual(pyext._class):
	# number of inlets and outlets
	_inlets=6
	_outlets=1
	
	modulus=0
	offset=0
	
	start=0
	end=0
	
	sieve=[]
	
	def __init__(self,*args):
		self.sieve=[]
		if len(args)>= 4:
			modulus=args[1]
			offset=args[2]
			start=args[3]
			end=args[4]
			populateSieve(this.modulus, this.offset, this.start, this.end)
			
	def bang_1(self):
		self._outlet(1,self.sieve)
		
	def int_2(self,i):
		self.modulus = i
		
	def int_3(self,i):
		self.offset = i
		
	def int_4(self,i):
		self.start = i

	def int_5(self,i):
		self.end = i
		
	def bang_6(self):
		populateSieve(this.modulus, this.offset, this.start, this.end)
		
	def populateSieve(m,o,s,e):
		self.sieve = []
		entry = s
		index = 0
		while (entry + o < e):
			if entry % m == 0:
				self.sieve.append(index, entry + o)
				index += 1
				entry += m 
			else:
				entry += 1
			
		