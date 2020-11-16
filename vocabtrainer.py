
def add():

    englishlist = []
    turkishlist = []

    print("Enter english voc")
    english = input()
    print("now the turkish equivalent:")
    turkish = input()

    englishlist.append(english)
    turkishlist.append(turkish)

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





#add()
#display()
show_content()


