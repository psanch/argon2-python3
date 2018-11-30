from argon2 import PasswordHasher
import argon2
import os
import sys

ph = PasswordHasher()

###############################################################################################################
### Utility Functions
###############################################################################################################


filename_logins = 'logins.txt'
filename_row = 'row.txt'

def createAccountRecord(args):
	username = args[0]
	salt = args[1]
	hashed = args[2]
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


def attemptAccountCreation(argv):
	if(len(argv) != 3):
		print('****\nIncorrect argument count',len(argv))
		return

	if(usernameIsUnique(argv[0]) == False):
		print('****\nError: Username already in use')
		return

	createAccountRecord(argv)
	print('****\nSuccess: Account created!')

def readLatestSalt():
	filename_latestSalt = 'latestSalt.txt'

	os.system("python3 getLatestSalt.py")

	fp = open(filename_latestSalt,'r')
	lines = [salt.strip('\n') for salt in fp.readlines()]
	fp.close()

	return lines[0]

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

	return contents

###############################################################################################################
### Password-Hashing Functions
###############################################################################################################

def register(username, pw):

	salt = readLatestSalt()

	hashed = argon2.low_level.hash_secret(bytes(pw.encode('utf-8')), bytes(salt.encode('utf-8')), time_cost=1, memory_cost=8, parallelism=1, hash_len=64, type=argon2.low_level.Type.I, version=19)
	formatted = (str(hashed)[2:-1])

	#python3 createAccount.py <username> <salt> <H(s+pw)>
	msg_string = username + " " + salt + " " + str(formatted)
	attemptAccountCreation(msg_string.split(' '))

	return

def login(username, pw):

	returned = search(username)
	if returned == '-1 -1 -1':
		print("****\nError: User does not exist.")
		return
	stored = (returned.split(' ')[2])

	#argon2.low_level.verify_secret(hash, secret, type)
	z = argon2.low_level.verify_secret(bytes(stored.encode('utf-8')), bytes(pw.encode('utf-8')), type=argon2.low_level.Type.I)
	
	if z == True:
		print("****\nSuccess: User Authenticated")
	else:
		print("****\nError: Failed to authenticate user.")


###############################################################################################################
### High-level User Interaction Functions
###############################################################################################################

def main():

	while(1):
		print("****\nOptions:")
		print("\tRegister")
		print("\tLogin")
		print("\tExit")
		control = input("Choose an option.\n\n")

		if control.upper() == "REGISTER":
			username = input("Please enter your username:\n")
			password = input("Please enter your password:\n")
			register(username, password)

		elif control.upper() == "LOGIN":
			username = input("Please enter your username:\n")
			password = input("Please enter your password:\n")
			login(username, password)

		else:
			print("Thanks for using the system.")
			return

main()






