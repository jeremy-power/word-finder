import itertools
letters = ['l','y','u','g','i']

finalword = ""
keywords = list(itertools.product(letters, repeat = 3))
testlist = []
for i in range(len(keywords)):
    testlist.append([])
    for j in range(len(keywords[i])):
        testlist[i].append(keywords[i][j])
wordlist = []
for i in range(len(testlist)):
    testlist[i].append('t')
    wordlist.append(''.join(testlist[i]))
for i in range(len(wordlist)):
    print(wordlist[i] + "\n")