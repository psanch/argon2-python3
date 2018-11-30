#Usage: python3 getRowFromUsername <username>
#Results in the row (username, salt, h(pw+s) ) in the file row.txt 
#If not found, "-1 -1 -1" >> row.txt


import sys


filename_logins = 'logins.txt'
filename_row = 'row.txt'

def search(username):
	fp = open(filename_logins, 'r')
	logins = [(login.strip('\n')).split() for login in fp.readlines()]
	fp.close()

	#logins = List[List]
	#logins[i] = [username, salt, H(s+pw)]

	i=0
	contents = '-1 -1 -1'

	while i in range(len(logins)):
		if logins[i][0] == username:
			contents = str(logins[i][0]) + ' ' + str(logins[i][1]) + ' ' + str(logins[i][2])
			break
		i+=1

	fp = open(filename_row, 'w')
	fp.write(contents)
	fp.close()


def main(argv):
	if(len(argv) != 2):
		print('Incorrect argument count')

	search(argv[1])


main(sys.argv)

