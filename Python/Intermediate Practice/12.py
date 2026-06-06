dic = {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}

def Inverted_Dic(d):
    result = {}

    for key in d:
        for value in d[key]:
            result[value]= key

    return result


print(Inverted_Dic(dic))