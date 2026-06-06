
def twoSum(arr,target):
    hashmap = {}
    for i,n in enumerate(arr):
        if target-n in hashmap:
            return [i,hashmap[target-n]]
        hashmap[n] = i
print(twoSum([6,1,2,4,3,8],9))