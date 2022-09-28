"""
Is it possible to advance from the start of the array to the last element 
given that the maximum you can advance from a position is based on the 
value of the array at the index you are currently present on?
"""

# def array_advance(A):
#     furthest_reached = 0
#     last_idx = len(A) - 1
#     i = 0
#     while i <= furthest_reached and furthest_reached < last_idx:
#         furthest_reached = max(furthest_reached, A[i] + i)
#         i += 1
#     return furthest_reached >= last_idx

def array_advance(A):
    idx = 0
    val = None
    while idx < len(A) - 1 and val != 0:
        val = A[idx]
        idx = idx + val
    if idx == len(A) -1:
        print('success')
    else:
        print('Failure!')
   





# x = [1,3,1,0,2,0,1]
x =[3, 2, 0, 0, 2, 0, 1]
array_advance(x)


