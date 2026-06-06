string = "Python is awesome".split(" ")
n = -1
reversedWords = []
for word in string:
    reversedWords.append(word[::-1])
resultedWords = " ".join(reversedWords)

print(resultedWords)