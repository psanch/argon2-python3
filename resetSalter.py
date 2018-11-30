# Usage: python3 resetSalter.py

filename_counter = 'counters.txt' 
filename_salts = 'salts.txt' 
filename_latestSalt = 'latestSalt.txt'
filename_logins = 'logins.txt'
filename_row = 'row.txt'

#reset counters to 0,0
fp = open(filename_counter, 'w')
fp.write('0\n0')
fp.close()

#flush all salts
fp = open(filename_salts, 'w')
fp.write('')
fp.close()

#flush latestSalter
fp = open(filename_latestSalt, 'w')
fp.write('')
fp.close()

#flush logins
fp = open(filename_logins, 'w')
fp.write('')
fp.close()

#flush requested rows
fp = open(filename_row, 'w')
fp.write('')
fp.close()