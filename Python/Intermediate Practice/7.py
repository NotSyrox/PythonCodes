testStr = "A man, a plan, a canal: Panama".replace(" ","")
resultStr = []
for word in testStr:
    for i in word:
        if i.isalnum():
            resultStr.append(i.lower())


if resultStr == resultStr[::-1]:
    print("Yes, This is a Palindrome String.")
else : 
    "No, This is not a Palindrome String."