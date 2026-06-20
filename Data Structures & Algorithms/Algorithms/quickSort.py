from random import randint


def quickSort(arr, low, high):
    if low >= high:
        return
    splitPoint  = partition(arr, low, high)
    quickSort(arr, low, splitPoint-1)
    quickSort(arr, splitPoint+1, high)
    return arr

def partition(arr, low, high):
    pivot = randint(low, high)
    arr[pivot], arr[high] = arr[high], arr[pivot]
    i = low-1
    for j in range(low, high):
        if arr[j] < arr[high]:
            i+=1
            arr[i],arr[j] = arr[j], arr[i]
    arr[high],arr[i+1] = arr[i+1],arr[high]

    return i+1

if __name__ == "__main__":
    print(quickSort([1,4,6,2,8,3,7,9,0], 0, 8))