#Submission by Akshay Tambe - N19098202 - apt321@nyu.edu
#Yahoo Password Dump Decryption
#Solution - Parse By Splitting

#Opening the given Yahoo Password Dump
yahoodump = open('yahoo.txt', 'r')
decryptlist = open('yahoodump_password_list.txt', 'w+')

#Adding Parsing Constraints
startparse = "1:ac1@associatedcontent.com:@fl!pm0de@"
endparse = "739853:smoker23@gmx.de:asdf1234"

#Initialising Variables
parse_flag = 0
count = 1
database_array = []

#Parsing the File
for line in yahoodump:
    #Ignore Redundant Strings --> Skip to 3. email:pass dump (450k users) in file
    if line.strip() == startparse:
        parse_flag = 1
        count = 1
        print 'Ignoring Redundant Strings from Dump File...'
    #Retrieving First 1000 Passwords
    if count < 1001 and parse_flag == 1:
        count = count + 1
        line = line.strip()
        #Split the Database File with Colon
        database_array = line.split(":")
        #Writing the file
        print str(count-1) + "\t" + line.strip().ljust(80) + " " + database_array[2] + "\n" 
        decryptlist.write(line.strip() + " " + database_array[2] + "\n")
    #Ignore Redundant Strings below last line of Database file
    if line.strip() == endparse:
        parse_flag = 0
        print 'Decryption Complete for 1K Passwords'