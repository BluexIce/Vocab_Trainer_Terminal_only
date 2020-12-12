import random

global englishvocab 
global turkishvocab 

#englishlist = []
#turkishlist = []

def add():

    #englishlist = []
    #turkishlist = []

    print("Enter english voc")
    english = input()
    print("now the turkish equivalent:")
    turkish = input()

    #englishlist.append(english)
    #turkishlist.append(turkish)

    #print("Your input: "+english)
    #print("Your input: "+turkish)

    #print("The new english list: "+str(englishlist))
    #print("The new turkish list: "+str(turkishlist))

    with open("vocab_english.txt", "a+") as e:
        e.write(english + "\n")
        
    with open("vocab_turkish.txt", "a+")as t:
        t.write(turkish + "\n")
        


def display():
    with open("vocab_english.txt", "r") as d:
        print("The new english list: " + "\n" + d.read())
        

    with open("vocab_turkish.txt", "r") as e:
        print("The new turkish list: " + "\n" + e.read())
        


def show_content():
    o = open("vocab_english.txt")
    for x in o:
        print(x)
    o.close()
    #shows all content of that file

    o = open("vocab_turkish.txt", "r")
    print("turkish vocab list:")
    for p in o:
        print(p)
    o.close()
    #shows the first entry of that file

def show_last_english_word():
    with open ("vocab_english.txt") as file:
        for last_english_vocab in file:
            pass
        print(last_english_vocab)


def show_last_turkish_word():
    with open ("vocab_turkish.txt") as file2:
        for last_turkish_vocab in file2:
            pass
        print(last_turkish_vocab)
    


#def remove_last_english_word():
    file = open("vocab_english.txt")
    for x in file:
        print(x)
    file.close()
    file = open("vocab_english.txt", "w+")
    for i in file:
        i.writelines([word for word in x[:-1]])
    file.close

    

def vocab_comparison():

    with open("vocab_english.txt", "r") as ve:
        #print("The new english list: " + "\n" + d.read())
        global englishvocab
        englishvocab = ve.readlines()

    with open("vocab_turkish.txt", "r") as vt:
        #print("The new turkish list: " + "\n" + e.read())
        global turkishvocab
        turkishvocab = vt.readlines()

        turkishvocab_readable = []

        for turkish_element in turkishvocab:
            turkishvocab_readable.append(turkish_element.strip())

        englishvocab_readable= []

        for english_element in englishvocab:
            englishvocab_readable.append(english_element.strip())
    
    random_number = random.randint(0,len(englishvocab_readable)-1)
    print(random_number)  # one number
    


    print(englishvocab_readable[random_number])
    print("please write the turkish equivalent: ")
    word = input()
    if word == turkishvocab_readable[random_number]:
        print("thats right!")    
    else:
        print("thats not the right answer!") 
        print(len(turkishvocab_readable[1])) #5
        print(len(word))            #4
        #print(turkishvocab)   #with \n
        #print(turkishvocab_converted) # without \n

    #a = str(englishvocab[random.randint(0,len(englishvocab)-1)])
    #print(a)  #prints word in vocab_english.txt
        
def learn():
    print(englishvocab[1])
    print("please write the turkish equivalent: ")
    word = input()
    if englishvocab[1] == word:
        print("thats right!")
    else:
        print("thats not the right answer!")
        


      


#add()
#display()
#show_content()
#show_last_turkish_word()
#remove_last_english_word()  #does not work properly
vocab_comparison() #writes the file content to an array
#learn()

#print(englishvocab[1])   # shows the content of the array
#print(turkishvocab) #


#print(englishlist)
#print(turkishlist)
