fh = open("Headlines", 'r')
Word = input("Type your Word Here:")
S = " "
count = 1

while S:
    S = fh.readline()
    L = S.split()
    if Word in L:
        print("Line Number:", count, ":", S)
        count += 1

