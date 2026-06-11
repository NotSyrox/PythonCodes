dict_a = {'a': 10, 'b': 20} 

dict_b = {'b': 5, 'c': 15}


def mergingDict(dict1,dict2):
    merged = {}

    for key in dict1:
        merged[key] = dict1[key]

    for key in dict2:
        merged[key] = merged.get(key, 0) + dict2[key]
    return merged

print(mergingDict(dict_a,dict_b))