import random as r

def binary_search(arr:list[int], target:int):
    start = 0
    end = len(arr) - 1
    attempts = 0
    while start <= end:
        middle = start + (end - start) // 2
        if arr[middle] < target:
            start = middle + 1
            attempts += 1
        elif arr[middle] > target:
            end = middle - 1
            attempts += 1
        else:
            attempts += 1
            return f"{middle}, took {attempts} attempts."
    return None

ran = r.randint(1,100000000)

seq = list(range(1, 100000001))

print(binary_search(seq, ran))
