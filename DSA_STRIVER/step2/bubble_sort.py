def bubbleSort(arr, n):
    # Your code goes here.
    for i in range(n):
        for j in range(1,n):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                continue
        print(i)

    return arr


def bubbleSort(arr, n):
    # Your code goes here.
    for i in range(len(arr)-1,1,-1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    
    return arr

arr = [41,467,334,500,169,724,478,358,962,464]
n = 10

print(bubbleSort(arr,n))



