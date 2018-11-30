# Usage: python3 getLatestSalt.py
# Latest Salt value will be in latestSalt.txt (filename_latestSalt)

import os

filename_counter = 'counters.txt' 
filename_salts = 'salts.txt'
filename_latestSalt = 'latestSalt.txt'

def readCounters():
	fp = open(filename_counter,'r')
	raw = fp.readlines()
	fp.close()

	counters = []
	for line in raw:
		counters.append(int(line.strip()))

	currentCounter = counters[0]
	usedCounter = counters[1]

	return currentCounter, usedCounter


def getLatestSalt():
	current, used = readCounters()

	#if no more available salts, make some
	if current == used:
		os.system("python3 salter.py 1")
		current += 1

	#now get the salt[used]
	fp = open(filename_salts, 'r')
	lines = [salt.strip('\n') for salt in fp.readlines()]
	fp.close()

	fp = open(filename_latestSalt, 'w')
	fp.write(str(lines[used]))
	used += 1
	fp.close()

	#update counters
	fp = open(filename_counter,'w')
	fp.write(str(current) + '\n' + str(used))
	fp.close()

getLatestSalt()





