numlist = [1, 2, 2, 3, 1, 4, 2]

seen = set()

result = []

for num in numlist:
    if num not in seen:
        seen.add(num)
        result.append(num)
    
print(result)