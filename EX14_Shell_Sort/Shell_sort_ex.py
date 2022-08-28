# x = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
# # i = 0
# # while i < (len(x) - 1):
# #     if x[i] == x[i+1]:
# #         del x[i]
# #     i+=1

# # # print(x)    
# # for i in x:
# #     print(str(i)+"i")
    

# # for j in x:
# #     print(str(x[j]) + "j")    
# i = 0
# j = 0
# while i < len(x) :    
#     if i == j:
#         j+=1
#         i-=1
#     if i < j and i > j:   
#         j = 0 
#         while j < len(x):
#             if x[i] == x[j]:
#                 del x[j]
                
            
#             j+=1
#     i+=1

# print(x)  


def shell_sort(arr):
    n = len(arr)
    div = 2
    gap = n//div
    while gap > 0:
        index_to_delete = []
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >= temp:
                if arr[j-gap] == temp:
                    index_to_delete.append(j)
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        index_to_delete=list(set(index_to_delete))
        index_to_delete.sort()
        if index_to_delete:
            for i in index_to_delete[-1::-1]:
                del arr[i]
        div *= 2
        n = len(arr)
        gap = n//div


if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9,  5, 8, 3]

    print(f'Given unsorted list: {elements}')
    shell_sort(elements)
    print(f'List after Sorting : {elements}')