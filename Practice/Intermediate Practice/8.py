l = ["apple", "education", "ice", "ocean", "python", "umbrella"]

resultedS = []
for word in l:
    if word[0].lower() in 'aeiou' and len(word) >5:
        resultedS.append(word)
        
print(resultedS)