"""
first take int input
use a while loop
    push elemnts in stack
either create a method to combine all 
items in a list or use a loop to add iteratively

"""
from stack_2nd import *
input_int = int(input("enter the number to convert into binary: "))
s = Stack()
while input_int >= 1:
    if input_int == 1:
        bit = input_int%2
        s.push(str(bit))
        break
    else:
        quo = input_int//2
        bit = input_int%2
        s.push(str(bit))
        input_int = quo

s.get_stack()
#two ways to display
#1. convert every bit we push to a str then print it like below code 
print("".join(s.items[::-1]))

#2. reverse stack then using loop to print in a single line
s.reverse_stack()

for i in s.items:
    print(i, end="")

# in a function format & slight different logic
def convert_int_to_bin(dec_num):
    
    if dec_num == 0:
        return 0
    
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(convert_int_to_bin(56))
print(convert_int_to_bin(2))
print(convert_int_to_bin(32))
print(convert_int_to_bin(10))

print(int(convert_int_to_bin(56),2)==56)
        

