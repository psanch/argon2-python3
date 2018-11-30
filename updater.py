import sys

if(len(sys.argv) < 2) or (len(sys.argv) > 2):
		print('Incorrect argument count')

fp = open('counters.txt','r')
raw = fp.readlines()
fp.close()

counters = []
for line in raw:
	counters.append(int(line.strip()))

currentCounter = counters[0]
usedCounter = sys.argv[1]

fp = open('counters.txt','w')
fp.write(str(currentCounter) + '\n' + str(usedCounter))
fp.close

