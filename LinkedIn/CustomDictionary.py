#Submission by Akshay Tambe - N19098202 - apt321@nyu.edu
#Custom Dictionary

#Importing Libraries
import random
  
#Initialising Variables  
r = random.SystemRandom()
password = open('CustomWordlist.txt','w+')

#Combinations
#W - WORDS    C - CHARACTERS    N - NUMBERS    FC - FIRST CAPS    ALL - ALL CAPS    LOWER - ALL LOWER    UPPER - ALL UPPER

#1W 1C 2N FC
def generate_password1(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    commonwords = r.sample(words[:top], k)
    
    numlist1 = []
    numlist2 = []
    charlist = []
    
    if numbers:
        numlist1.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist2.insert(r.randint(1,9), r.choice(numbers))
    if characters:
        charlist.insert(r.randint(1,9), r.choice(characters))

    return ''.join(commonwords+charlist+numlist1+numlist2).title()
 
#2W 1C 1N FC
def generate_password2(words, top=60000, k=2, numbers=None, characters=None, first_upper=True):
    commonwords = r.sample(words[:top], k)
    
    numlist1 = []
    charlist = []
    
    if numbers:
        numlist1.insert(r.randint(1,9), r.choice(numbers))
    if characters:
        charlist.insert(r.randint(1,9), r.choice(characters))

    return ''.join(commonwords+charlist+numlist1).title()

#1W 1C 3N FC
def generate_password3(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    commonwords = r.sample(words[:top], k)
    
    numlist1 = []
    numlist2 = []
    numlist3 = []
    charlist = []
    
    if numbers:
        numlist1.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist2.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist3.insert(r.randint(1,9), r.choice(numbers))
    if characters:
        charlist.insert(r.randint(1,9), r.choice(characters))

    return ''.join(commonwords+charlist+numlist1+numlist2+numlist3).title()
 
#1W 1C 2N ALL
def generate_password4(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    commonwords = r.sample(words[:top], k)
    
    numlist1 = []
    numlist2 = []
    charlist = []
    
    if numbers:
        numlist1.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist2.insert(r.randint(1,9), r.choice(numbers))
    if characters:
        charlist.insert(r.randint(1,9), r.choice(characters))

    return ''.join(commonwords+charlist+numlist1+numlist2).upper()
 
#1W 0C 0N ALL
def generate_password5(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    commonwords = r.sample(words[:top], k)
    
    return ''.join(commonwords).upper()

#1W 0C 3N ALL
def generate_password6(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    commonwords = r.sample(words[:top], k)
    
    numlist1 = []
    numlist2 = []
    numlist3 = []
    
    if numbers:
        numlist1.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist2.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist3.insert(r.randint(1,9), r.choice(numbers))

    return ''.join(commonwords+numlist1+numlist2+numlist3).upper()

#3N 1W 3N LOWER
def generate_password7(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    commonwords = r.sample(words[:top], k)
    
    numlist1 = []
    numlist2 = []
    numlist3 = []
    numlist4 = []
    numlist5 = []
    numlist6 = []
    
    if numbers:
        numlist1.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist2.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist3.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist4.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist5.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist6.insert(r.randint(1,9), r.choice(numbers))

    return ''.join(numlist1+numlist2+numlist3+commonwords+numlist4+numlist5+numlist6).lower()

#3N 1W LOWER
def generate_password8(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    commonwords = r.sample(words[:top], k)
    
    numlist1 = []
    numlist2 = []
    numlist3 = []
    
    if numbers:
        numlist1.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist2.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist3.insert(r.randint(1,9), r.choice(numbers))

    return ''.join(numlist1+numlist2+numlist3+commonwords).lower()

#1W 4N LOWER
def generate_password9(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    commonwords = r.sample(words[:top], k)
    
    numlist1 = []
    numlist2 = []
    numlist3 = []
    numlist4 = []
    
    if numbers:
        numlist1.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist2.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist3.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist4.insert(r.randint(1,9), r.choice(numbers))

    return ''.join(commonwords+numlist1+numlist2+numlist3+numlist4).lower()

#2W 2N 1C LOWER
def generate_password10(words, top=60000, k=2, numbers=None, characters=None, first_upper=True):
    elements = r.sample(words[:top], k)
  
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))    
    if characters:
            elements.insert(r.randint(1, len(elements)), r.choice(characters))

    return ''.join(elements).lower()

#1W 2N 1C LOWER
def generate_password11(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    elements = r.sample(words[:top], k)
  
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))    
    if characters:
            elements.insert(r.randint(1, len(elements)), r.choice(characters))

    return ''.join(elements).lower()

#2W 1N 1C LOWER
def generate_password12(words, top=60000, k=2, numbers=None, characters=None, first_upper=True):
    elements = r.sample(words[:top], k)

    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))    
    if characters:
            elements.insert(r.randint(1, len(elements)), r.choice(characters))

    return ''.join(elements).lower()

#1W 1N 0C FIRST CAPS
def generate_password13(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    elements = r.sample(words[:top], k)
  
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))

    return ''.join(elements).title()

#1W 1N LOWER
def generate_password14(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    elements = r.sample(words[:top], k)
  
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))

    return ''.join(elements).lower()

#2W 2N 0C LOWER
def generate_password15(words, top=60000, k=2, numbers=None, characters=None, first_upper=True):
    elements = r.sample(words[:top], k)
  
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))
    if numbers:        
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))    

    return ''.join(elements).lower()

#1W 1N 1C LOWER
def generate_password16(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    elements = r.sample(words[:top], k)
  
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))
    if characters:
            elements.insert(r.randint(1, len(elements)), r.choice(characters))

    return ''.join(elements).lower()

#1W 3N 1C LOWER
def generate_password17(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    elements = r.sample(words[:top], k)
  
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))            
    if characters:
            elements.insert(r.randint(1, len(elements)), r.choice(characters))

    return ''.join(elements).lower()


#2W 1N 0C LOWER
def generate_password18(words, top=60000, k=2, numbers=None, characters=None, first_upper=True):
    elements = r.sample(words[:top], k)
  
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))           

    return ''.join(elements).lower()

#1W UPPER
def generate_password19(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    elements = r.sample(words[:top], k)
  
    return ''.join(elements).upper()

#1W 3N LOWER
def generate_password20(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    elements = r.sample(words[:top], k)
  
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))           
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))           
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))           

    return ''.join(elements).lower()

#1W 3N UPPER
def generate_password21(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    elements = r.sample(words[:top], k)
  
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))           
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))           
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))           

    return ''.join(elements).upper()

#1W 1N 1C FIRST CAPS
def generate_password22(words, top=60000, k=1, numbers=None, characters=None, first_upper=True):
    elements = r.sample(words[:top], k)
  
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))           
    if characters:
            elements.insert(r.randint(1, len(elements)), r.choice(characters))

    return ''.join(elements).title()

#2W 2N 1C FIRST CAPS
def generate_password23(words, top=60000, k=2, numbers=None, characters=None, first_upper=True):
    elements = r.sample(words[:top], k)
  
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))           
    if numbers:
            elements.insert(r.randint(1, len(elements)), r.choice(numbers))           
    if characters:
            elements.insert(r.randint(1, len(elements)), r.choice(characters))

    return ''.join(elements).title()

#10N
def generate_password24(words, top=60000, k=0, numbers=None, characters=None, first_upper=True):    
    numlist1 = []
    numlist2 = []
    numlist3 = []
    numlist4 = []
    numlist5 = []
    numlist6 = []
    numlist7 = []
    numlist8 = []
    numlist9 = []
    numlist10 = []
    
    if numbers:
        numlist1.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist2.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist3.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist4.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist5.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist6.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist7.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist8.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist9.insert(r.randint(1,9), r.choice(numbers))
    if numbers:
        numlist10.insert(r.randint(1,9), r.choice(numbers))

    return ''.join(numlist1+numlist2+numlist3+numlist4+numlist5+numlist6+numlist7+numlist8+numlist9+numlist10)

#Main Function
if __name__ == '__main__':
    with open('names.txt') as f:
        words = [w.strip() for w in f]
    count= 0
    #Generating Passwords    
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password1(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password2(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password3(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password4(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password5(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password6(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password7(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password8(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password9(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password10(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password11(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password12(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password13(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password14(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password15(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password16(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password17(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password18(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password19(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password20(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password21(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password22(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password23(words, numbers='0123456789', characters='!@#$%')+"\n")
    for i in range(1,1000000):
        count = count + 1
        print count
        password.write(generate_password24(words, numbers='0123456789', characters='!@#$%')+"\n")
        
    password.close()