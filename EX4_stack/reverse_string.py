from stack_2nd import *
# reverse string using list slicing
# input_str = "Educative"
# print(input_str[::-1])

# reverse string using a stck data structure
input_str = str(input("Enter the string to be reversed: "))
s = Stack()
output_str = ''
for i in range(0,len(input_str)):
    s.push(input_str[i])

for i in range(0,len(s.get_stack())):
    output_str = output_str + s.pop()

print(output_str)

#Educative
def reverse_string(stack, input_str):
  for i in range(len(input_str)):
    stack.push(input_str[i])
  rev_str = ""
  while not stack.is_empty():
    rev_str += stack.pop()

  return rev_str

stack = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))
