def countWords():
    filename=input("enter the filename")

    numWords=0
    file=open(filename,'r')
    for line in file:
        Words=line.split()
        numWords=numWords+len(Words)
    print("no of words")
    print(numWords)

countWords()