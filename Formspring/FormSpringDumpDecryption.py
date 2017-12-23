#Submission by Akshay Tambe - N19098202 - apt321@nyu.edu
#Formspring Password Dump Decryption
#Solution - Dictionary Attack

#Importing Librarires
import hashlib

#Opening the given Formspring Password Dump
formspringdump = open('formspring.txt', 'r')
dictionary = open('CustomWordlist1.txt', 'r')
decryptlist = open('formspringdump_password_list.txt', 'a')

#Initialising Variables
count = 0
salt1 = 0x30
salt2 = 0x30

#Creating a set for storing given sha1 hashed values
sha256_set = set()
for line in formspringdump:
  sha256_set.add(line.strip()) 

count = 0
while (salt2 <= 99):
    while (salt1 <= 99):
        for line in dictionary:
            #Appending Salt to Dictionary Item and Hashing to SHA256
            hashed_dictionary_item = hashlib.sha256(chr(salt1) + chr(salt2) + line.strip()) #Used title(), upper(), lower() for more passwords
            #Comapring the Dictionary Item Hash with the Formspring Dump
            if hashed_dictionary_item.hexdigest() in sha256_set:
                count = count + 1
                if count < 1001:
                    #Match Found
                    #Print To File
                    decryptlist.write(hashed_dictionary_item.hexdigest()+ " " + line.strip() + "\n")
                    print str(count) + "\t" + hashed_dictionary_item.hexdigest()+ "\t" + line.strip().ljust(100) + "\n"
                else:
                    #Counter Exceed 1K Passwords --> Exit
                    print 'Decryption Completed...' + '\n' + str(count) + 'Passwords Found'
                    exit()
        dictionary.seek(0,0)
        salt1 = salt1 + 1
    salt2 = salt2 + 1
    
if count == 0:
    print 'Decryption Completed...' + '\n' + 'No Passwords Found'
else:
    print 'Decryption Completed...' + '\n' + str(count) + 'Passwords Found'
    salt1 = 0x30