from english_words import get_english_words_set

wordListOG = get_english_words_set(['gcide'], lower=True)

wordListNew = []

for word in wordListOG:
    wordListNew.append(word)
wordListNew.sort()

count = 0
v2cList = []
lowList = []
lowListWord = []
count2 = 0
lowListWordVal = []

for word in wordListNew:
    word = word.lower()
    charList = list(word)

    vowels = ["a", "e", "i", "o", "u"]

    v = 0
    c = 0

    for letter in charList:
        if letter in vowels:
            v += 1
        else:
            c += 1

    if v == 0:
        v = 10000
        c = 1
    elif c == 0:
        v = 1
        c = 1

    v2c = v / c
    v2cList.append(v2c)

highVal = 0

for val in v2cList:
    val = v2cList[count]
    if val > highVal:
        highVal = val
        if highVal == v2cList[len(v2cList) - 1]:
            highVal = v2cList[len(v2cList) - 1]
    count += 1
combLists = zip(wordListNew, v2cList)
combFinalList = list(combLists)

for val in combFinalList:
    if val[1] == highVal:
        lowList.append(val)

for word in lowList:
    lowListWord.append(word[0].replace(" ", ""))

for word in lowListWord:
    lowListWordVal.append(len(word))

newComb = zip(lowListWord, lowListWordVal)

newCombList = list(newComb)

newCombList.sort()

highVal2 = 0

for val in newCombList:
    if val[1] > highVal2:
        highVal2 = val[1]


for val in newCombList:
    if val[1] == highVal2:
        print(val[0])


print("Exit by pressing the enter key")
input()