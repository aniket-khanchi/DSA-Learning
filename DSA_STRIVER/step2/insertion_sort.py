#without Recursion

def insertionSort(arr,n):
    for i in range(0,n):
        j=i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
    return arr  

arr = [9,3,6,2,0]
n = len(arr)

print(insertionSort(arr,n))