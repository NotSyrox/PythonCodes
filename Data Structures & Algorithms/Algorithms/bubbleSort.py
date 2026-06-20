def bubbleSort(arr):

    for i in range(len(arr)-1,0,-1):

        for j in range(i):

            if arr[j] > arr[j+1]:

                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

if __name__ == "__main__":
    print(bubbleSort([12,634,2,6,4,78,9,1]))