SetA = {1, 2, 3}
SetB = {1, 2, 3, 4, 5}


if SetA.isdisjoint(SetB):
    print("Set A is disjoint of Set B")
elif SetA.issubset(SetB):
    print("Set A is subset of Set B")
elif SetA.issuperset(SetB):
    print("Set A is superset of Set B")

# def validate_relationships(list1, list2):
#     a = set(list1)
#     b = set(list2)
    
#     if a.issubset(b):
#         print("Set A is a subset of Set B.")
#     elif a.issuperset(b):
#         print("Set A is a superset of Set B.")
    
#     if a.isdisjoint(b):
#         print("The sets are disjoint (they share no elements).")
#     else:
#         print(f"The sets share these elements: {a & b}")

# # Usage
# validate_relationships([1, 2], [1, 2, 3, 4])