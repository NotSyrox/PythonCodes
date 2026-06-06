from itertools import combinations

l = [1, 2, 3]
result = []

for i in range(0,len(l)+1):
	result.append(list(combinations(l,i)))
	
print(result)