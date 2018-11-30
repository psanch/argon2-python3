# Provides Salter class for secure password storage
# Generates N unique salts and appends them to salts.txt
# usage: "python3 salter.py N" 

import sys
from Crypto.Hash import SHA256

filename_counter = 'counters.txt' #[how many salts we've generated \n how many salts we've used]
filename_salts = 'salts.txt' #

class salter():

	def __init__(self):
		#initialize the counter variables
		self.currentCounter, self.usedCounter = self.readCounters()

		#initialize hashing functionality
		self.hasher = SHA256.new()

	def readCounters(self):
		fp = open(filename_counter,'r')
		raw = fp.readlines()
		fp.close()

		counters = []
		for line in raw:
			counters.append(int(line.strip()))

		currentCounter = counters[0]
		usedCounter = counters[1]

		return currentCounter, usedCounter

	def getHash(self,msg):
		x = bytearray(int(msg))
		self.hasher.update(x)
		return self.hasher.hexdigest()

	def writeSalts(self,numSalts):

		newCounter = self.currentCounter + numSalts

		newSalts = ''
		if self.currentCounter != 0:
			newSalts = '\n'

		for i in range(self.currentCounter, self.currentCounter+numSalts):
			newSalts+= (str(self.getHash(i))[:32] + '\n')
		newSalts = newSalts[:-1]

		fp = open(filename_salts,'a')
		fp.write(str(newSalts))
		fp.close()

		fp = open(filename_counter,'w')
		fp.write(str(newCounter) + '\n' + str(self.usedCounter))
		fp.close()

		self.currentCounter = newCounter


def main(argv):
	if(len(argv) < 2) or (len(argv) > 2):
		print('Incorrect argument count')

	x = salter()
	x.writeSalts(int(argv[1]))

main(sys.argv)

