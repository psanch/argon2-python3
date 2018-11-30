README

salter.py
	"python3 salter.py <N>"
	N is number of new unique salts to be generated

getLatestSalt.py
	"python3 getLatestSalt.py"
	Latest salt will appear in latestSalt.txt, guaranteed
	Even if no unused salts, it will create a new salt.

getRowFromUsername.py
	"python3 getRowFromUsername.py <username>"
	Writes the requested row (username, salt, h(pw+s) ) in the file row.txt
	If username not found, "-1 -1 -1" goes into row.txt
	Can be used to check if a user already exists (account creation) or to get the data required to authenticate a user (login)

resetSalter.py
	"python3 resetSalter.py"
	Resets all relevant files

createAccount.py
	"python3 createAccount.py <username> <salt> <H(s+pw)>"
	Can be used to create an account once (s+pw) has been run through hash algorithm
	Will not write new account if account with the same username already exists.