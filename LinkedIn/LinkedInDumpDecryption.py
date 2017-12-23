#Submission by Akshay Tambe - N19098202 - apt321@nyu.edu
#LinkedIn Password Dump Decryption
#Solution - Dictionary Attack

#Importing Hash Library
import hashlib

#Opening the given LinkedIn Password Dump and the generated Dictionary
linkedindump = open('SHA1.txt', 'r')
dictionary = open('CustomWordList1.txt', 'r')
decryptlist = open('linkedindump_password_list.txt', 'a')

#Initializing Counters
count = 0

#Creating a set for storing given sha1 hashed values
sha1_set = set()
for line in linkedindump:
  sha1_set.add(line.strip()) 

for line in dictionary:
  #Add SHA1 Hash Value to Current Dictionary Item
  hashed_dictionary_item = hashlib.sha1(line.strip()) #Used title(),upper(),lower() for more passwords
  #Check if Dictionary Hash Value present in the provided list
  if hashed_dictionary_item.hexdigest() in sha1_set and count < 1001:
    count = count + 1
    #Print To File
    decryptlist.write(hashed_dictionary_item.hexdigest() + " " + line)
    print str(count) + "\t" + hashed_dictionary_item.hexdigest().ljust(70) + line

if count == 0:
  print 'No Passwords Found'
else: 
  print 'Decryption Completed...' + '\n' + str(count) + " " + 'Passwords Found'