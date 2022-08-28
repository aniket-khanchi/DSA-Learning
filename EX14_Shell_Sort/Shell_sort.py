def shell_sort(arr):
    size = len(arr)
    gap = size//2

    while gap > 0:
        for i in range(gap,size):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap]>anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2

def foo(arr):
    size = len(arr)
    gap = size // 2
    gap = 3
    for i in range(gap, size):
        anchor = arr[i]
        j = i
        while j>=gap and arr[j-gap]>anchor:
            arr[j] = arr[j-gap]
            j -= gap
        arr[j] = anchor

if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [5]
    ]
    # elements = [89,78,61,53,23,21,17,12,9,7,6,2,1]
    elements =[2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    #for elements in tests:
    shell_sort(elements)
    print(elements)
x = elements
i = 0
while i < (len(x) - 1):
    if x[i] == x[i+1]:
        del x[i]
    i+=1

print(x)   