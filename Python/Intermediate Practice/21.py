numbers = [1, 2, 3, 2, 4, 5, 1, 6]
duplicates_found = set()
nums_checked = set()

def isDuplicate(num_list):
    for num in num_list:
        if num in nums_checked:
            duplicates_found.add(num)
        else:
            nums_checked.add(num)
    return duplicates_found

print(f"Duplicates are: {isDuplicate(numbers)}")