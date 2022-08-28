#searching algorithm
# Input : arr[] = {10, 20, 80, 30, 60, 50, 
#                      110, 100, 130, 170}
#           x = 110;
# Output : 6
# Element x is present at index 6
# Input : arr[] = {10, 20, 80, 30, 60, 50, 
#                      110, 100, 130, 170}
#            x = 175;
# Output : -1
# Element x is not present in arr[].

import numpy as np
def fin_el(arr, n ):
    """find the element at a given position"""
    if n in arr:
        return 1
    return -1    

x = np.array([10, 20, 80, 30, 60, 50, 110, 100, 130, 170])    
y= len(x)
print(y)
f = 110
print(fin_el(x,f))


x1 = np.array([10, 20, 80, 30, 60, 50, 110, 100, 130, 170])    
f = 175
print(fin_el(x1,f))

z = 25 
print(25)