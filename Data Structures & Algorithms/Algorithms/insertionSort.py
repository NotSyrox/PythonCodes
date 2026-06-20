def insertionSort(arr:list[int]) -> list:
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j-1] and j > 0:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
    return arr
if __name__ == "__main__":
    print(insertionSort([5,2,7,9,4,6,1,8,3]))