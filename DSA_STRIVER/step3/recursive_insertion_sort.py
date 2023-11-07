def ins_sort(arr,n,i):
    if i ==n :
        return
    while i > 0 and arr[i-1] > arr[i]:
        arr[i],arr[i-1]=arr[i-1],arr[i]
        i-=1
    i+=1
    ins_sort(arr,n,i)

arr = [41,467,334,500,169]
n = len(arr)
print(arr)
ins_sort(arr,n,0)
print(arr)
