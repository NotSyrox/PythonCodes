def removeExtraParens(string):
    trackOfParens = []
    idx = 0
    newStr = []
    for char in string:
        if char == "(":
            trackOfParens.append(idx)
            newStr.append(char)
        elif char == ")":
            if trackOfParens:
                trackOfParens.pop()
                newStr.append(char)
            else:
                newStr.append('')
        else:
            newStr.append(char)
        idx += 1
    for i in trackOfParens:
        newStr[i] = ""
    return ''.join(newStr)

print(removeExtraParens(input("Enter a string that includes '(' or ')': ")))