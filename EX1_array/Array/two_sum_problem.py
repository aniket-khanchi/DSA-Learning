"""
Given an array of integers, return True or False if the array 
has two numbers that add up to a specific target.
You may assume that each input would have exactly one solution.
"""







# def two_sum_brute_force(A,target):
#     for i in range(len(A)-1):
#         for j in range(i+1,len(A)):
#             if A[i] + A[j] == target:
#                 print(A[i],A[j])
#                 return True
#     return False
# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]
    return False

# Time Complexity: O(n)
# Space Complexity: O(1)
def two_sum(A, target):
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif i < j:
            i += 1
        else:
            j -= 1
    return False




A = [-2, 1, 4, 2, 7, 11]
target = 13
print(two_sum(A,target))
# print(two_sum_hash_table(A,target))

