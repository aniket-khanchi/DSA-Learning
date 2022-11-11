# 1. Write a Python program to calculate the sum of a list of numbers.
# x = [1,3,4,5,6]

# def sum_list(ls,idx):
#     if idx == len(ls):
#         return 0  
#     sum = ls[idx]
#     return sum + sum_list(ls,idx+1)

# print(sum_list(x,0))


# 2. Write a Python program to converting an Integer to a string in any base.

def to_string(n,base):
   conver_tString = "0123456789ABCDEF"
   if n < base:
      return conver_tString[n]
   else:
      return to_string(n//base,base) + conver_tString[n % base]

print(to_string(2835,16))

#