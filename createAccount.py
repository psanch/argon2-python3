#Usage: python3 createAccount.py <username> <salt> <H(s+pw)>

import sys
import os

filename_logins = 'logins.txt'
filename_row = 'row.txt'

def createAccountRecord(args):
	username = args[0]
	salt = args[1]
	hashed = args[2]
	print(username,salt,hashed)
	contents = str(username) + ' ' + str(salt) + ' ' + str(hashed) + '\n'

	fp = open(filename_logins, 'a')
	fp.write(contents)
	fp.close()

def usernameIsUnique(username):
	msg = "python3 getRowFromUsername.py " + str(username)
	os.system(msg)

	fp = open(filename_row,'r')
	results = [(login.strip('\n')).split() for login in fp.readlines()]
	fp.close()

	if results[0][0] != "-1":
		return False
	return True


def main(argv):
	if(len(argv) != 4):
		print('Incorrect argument count',len(argv))
		print(argv)
		return

	if(usernameIsUnique(argv[1]) == False):
		print('username already in use')
		return

	print("input: ",argv[1:])

	createAccountRecord(argv[1:])
