nested = [1, [2, 3], [4, [5, 6]], 7]

def GetFlattened(lis: list):
    flattened = []
    for i in lis:
        if isinstance(i, list):
            flattened.extend(GetFlattened(i))
        else: flattened.append(i)
    return flattened

print(GetFlattened(nested))