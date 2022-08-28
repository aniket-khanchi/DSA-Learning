#using list as a stack
# s = []

# s.append('https://www.cnn.com/')
# s.append('https://www.cnn.com/world')
# s.append('https://www.cnn.com/india')
# s.append('https://www.cnn.com/china')



# s.pop()

# print(s)

from collections import deque
stack = deque()

dir(stack) # to know the mtds of stacks

stack.append("https://www.cnn.com/")     # to push the element
stack.append("https://www.cnn.com/world")
stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")

# print(stack)


stack.pop()  # to pull the last element

class stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

    def look(self):
        return self.container    


s = stack()

s.push(5)
s.push(9)
s.push(34)
s.push(78)
s.push(12)

print(s.look())
# print(s)
print(s.is_empty())




