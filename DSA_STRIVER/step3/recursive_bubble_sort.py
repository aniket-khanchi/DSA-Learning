# def bubbleSort(arr, n):
#     # Your code goes here.
#     for i in range(len(arr)-1,1,-1):
#         for j in range(0,i):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
    
#     return arr


def bub_sort_rec(arr,n):

    if n==1:
        return
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]

    bub_sort_rec(arr,n-1)

arr = [41,467,334,500,169]
n = len(arr)
print(arr)
bub_sort_rec(arr,n)
print(arr)