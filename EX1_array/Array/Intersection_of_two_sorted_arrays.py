"""
Given two sorted arrays, A and B, determine their intersection. What elements are common to A and B?
"""

from datetime import datetime
 
# record current timestamp

from numpy import append

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]


# print(set(A).intersection(B))

def intersection_array(A,B):  #the time complexity is worst O(n^2) in operator take O(n) & inside for loop for full program it become O(n^2)
    intersection = []
    for i in set(A):
        if i in B:
            intersection.append(i)
            

    return intersection

print(intersection_array(A,B))


start = datetime.now()


def intersect_sorted_array(A, B):
    i = 0
    j = 0
    intersection = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]: #this condn A[i] != A[i - 1] takes care of duplicate items in list
                intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection

print(intersect_sorted_array(A,B))
end = datetime.now()
td = (end - start).total_seconds() * 10**3
print(f"The time of execution of above program is : {td:.03f}ms")
