
def swap(arr, x, y):
    arr[x],arr[y] = arr[y],arr[x]
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        lowest_index = i
        for j in range(i,len(arr)):
            if arr[j] < arr[lowest_index]:
                lowest_index = j
        swap(arr,lowest_index,i)
    return arr

array = [5,4,3,2,1]

print(selection_sort(array))