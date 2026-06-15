word1 = "listen"
word2 = "silent"

def anagramCheck(w1,w2):
    
    sortedW1 = sorted(w1.lower().replace(" ", ""))

    sortedW2 = sorted(w2.lower().replace(" ", ""))

    return sortedW1 == sortedW2

print(anagramCheck(word1,word2))