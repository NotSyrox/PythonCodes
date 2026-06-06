from collections import Counter

text = "Python Programming".replace(" ", "").lower()
filteredText = text
totalCount = Counter(filteredText)

print(totalCount)