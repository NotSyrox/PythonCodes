list1 = [101, 102, 103] 
list2 = [103, 104, 105]

def IsSymmetric(l1,l2):
    result = []
    for n in l1:
        if n not in l2:
            result.append(n)
    for n in l2:
        if n not in l1:
            result.append(n)
    return result

print(IsSymmetric(list1,list2))

# def get_exclusive_ids(ids1, ids2):
#     set1 = set(ids1)
#     set2 = set(ids2)
    
#     # Symmetric difference
#     return set1 ^ set2

# # Usage
# january_visitors = [10, 20, 30, 40]
# february_visitors = [30, 40, 50, 60]

# exclusive = get_exclusive_ids(january_visitors, february_visitors)
# print(f"Visitors exclusive to one month: {exclusive}")