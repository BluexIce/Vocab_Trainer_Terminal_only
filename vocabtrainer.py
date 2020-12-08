

englishlist = []
turkishlist = []

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
        print(last_vocab)


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

    
#def compare():

        


      


#add()
#display()
show_content()
#show_last_turkish_word()
#remove_last_english_word()  #does not work properly



print(englishlist)
print(turkishlist)
