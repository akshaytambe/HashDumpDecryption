# Hash Decryption Algorithms

## Yahoo Dump
The Yahoo database dump was pretty easy to decrypt, as the given file already has passwords with its usernames associated respectively. This is a case of analyzing and understanding the pattern of storage in the file. A python program was written to parse the text file for eliminating the redundant data and splitting the passwords from the original text to form a presentable format.
### Files:
* Decryption Python Program - YahooDumpDecryption.py - Yahoo Dump - yahoo.txt
* Decrypted List - yahoodump_password_list.txt

## LinkedIn Dump
### Identifying the Hash
The LinkedIn Dump was included with the hashes. Now, there are many types of hashes available for encryption of passwords such SHA1, SHA256, MD5 and the list goes on. For this dump, we first need to identify what kind of hashes does the file have. The hash file contains hashes which are 40 characters long. So, the hashing algorithm SHA1 seems to a perfect match for this password dump.
### Thinking of type of attacks
The implementation of reverse SHA1 Decryption is a complex method. Therefore, the focus was turned towards another approach – Brute Force Attack, which is a type of attack of trying all the possible combinations of alphabets, words, and characters. But this approach is too slow to crack down the passwords. Subsequently, Dictionary attack seemed to be a better and faster approach for cracking this dump.
### Developing a Custom Dictionary
For developing a dictionary attack, there was a need for creation of custom dictionary. A dictionary generated with random strings with a string length of 5 to 9 characters was insufficient and time-consuming. According to recent trends, humans store passwords in a readable format which they can remember. Also, some websites have restrictions on the number of characters, special characters, and cases. This paved to create a smart dictionary. Two help-lists: ‘Common First Names’ and ‘Commonly Used English Words’ were used to generate a custom dictionary. A python program which is working on rules by setting a combination between common-words, characters and numbers created a wordlist of around 20 million words for comparing with the SHA1 Hash.
### Working of Decryption Algorithm
The working of decryption program for the LinkedIn dump is based on dictionary attack. The algorithm picks one line in the custom dictionary sequentially, calculate the hash and then searches the computed hash in the original dump file. If the hash is matched, the password is printed in the list with its hash value in a file. The dictionary items are manipulated in the program in a such way that it was generating each hash set of uppercases, lowercases, first capital letters and mixed of cases which helped to reach find around 1000 passwords.
### Files:
* Random Dictionary Program - Generates random set of strings for hash comparison - RandomWordList.py
* Smart Dictionary Program - Generates a custom wordlist based on rules for hash comparison – CustomDictionary.py - Decryption Python Program - Decryption algorithm for SHA1 Hash - LinkedInDumpDecryption.py
* LinkedIn Dump - Provided Dump File - SHA1.txt
* Decrypted List - Cracked Passwords - linkedindump_password_list.txt

## Formspring Dump
The Formspring dump includes the SHA256 Hashes with Salts which are 64 characters long. Salting is appending a random data to the hashes generated. This prevents hashes to be attacked by well-known decryption techniques. E.g. Same passwords have same hashes, but if salted both the hashes are appended with different combinations making them unique.
### Working of Decryption Algorithm using Salts
After performing few cases, appending the salts before hash seems to be a better solution for this dump. The most common mistake while decrypting this type of hash is salting with same numbers by hardcoding which makes decrypting an ineffective process. In this dump, the salts are between 00 to 99. Therefore, a python program is created which appends two random salts before the dictionary item and then computes the hash. The calculated hash is then compared with the list of provided hashes. If a match is found, the passwords are printed with its hash value in the file. The python program uses Dictionary Attack: the same approach as that of LinkedIn Dump for cracking the passwords.
### Files:
* Random Dictionary Program - Generates random set of strings for hash comparison - RandomWordList.py
* Smart Dictionary Program - Generates a custom wordlist based on rules for hash comparison – CustomDictionary.py - Decryption Python Program - Decryption algorithm for SHA256 Hash with Salts - FormSpringDumpDecryption.py
* Formspring Dump - Provided Dump File - formspring.txt
* Decrypted List - Cracked Passwords - formspringdump_password_list.txt

## Comparing the Cracking Techniques
* Decrypting yahoo dump was easy as compared to decrypting the LinkedIn and Formspring dump.
* Dictionary attacks seem to be effective as compared to Brute Force Attack as it performs intelligent guesses.
* SHA256 Hashes with Salts present in Formspring Dump are much more secure than SHA1 Hashes in LinkedIn Dump and therefore, Formspring Dump was difficult to crack as compared to LinkedIn Dump.
* SHA256 Formspring hash decryption algorithm has more complexity than SHA1 LinkedIn hash decryption algorithm.
* The compute time for SHA256 Decryption Algorithm is more than other two decryption algorithms.

