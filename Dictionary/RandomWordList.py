#Submission by Akshay Tambe - N19098202 - apt321@nyu.edu
#Random Dictionary

#Importing Libraries
import string, random

#Open File
FILE = open("RandomWordList.txt","w+")

#Inputs5
min_charlength = input('Minimum Characters of Password: ')
max_charlength = input('Maximum Characters of Password: ')
quantity = input('Number of Passwords to be generated: ')

#Initialising Varaiables
alphabet = string.letters[0:52] + string.digits #+ string.punctuation
string=''

#Generating Password
for count in xrange(0,quantity):
  #Appending Random String to File
  for x in random.sample(alphabet,random.randint(min_charlength,max_charlength)):
      string += x
  print str(count) + "\t" + string +'\n'
  FILE.write(string +'\n')
  string=''
FILE.close()
print 'Passwords are generated successfully!'