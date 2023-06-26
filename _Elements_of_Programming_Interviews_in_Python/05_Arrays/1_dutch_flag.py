x =[1,4,7,3,6,9,2,8,5]


def even_odd(x):
    even_arr = []
    odd_arr = []
    for i in x:
        if i%2==0:
            even_arr.append(i)
        else:
            odd_arr.append(i)

    return even_arr+ odd_arr

# print(even_odd(x))

def even_odd_mod(A):
    even_idx = 0
    odd_idx = len(A)-1
    while even_idx < odd_idx:
        if A[even_idx]%2 ==0:
            even_idx+=1
        else:
            A[even_idx], A[odd_idx] = A[odd_idx], A[even_idx]
            odd_idx -=1
    return A




print(even_odd_mod(x))