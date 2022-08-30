from inspect import stack


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        print(self.items)

    # insert a value at bottom of stack using recursion
    def insert_bottom(self,value):
        if self.is_empty():
            self.push(value)
        else:
            pop_val = self.pop()
            self.insert_bottom(value)
            self.push(pop_val)
    #reverse a stack using recursion
    def reverse_stack(self):
        if self.is_empty():
            pass
        else:
            pop_value = self.pop()
            self.reverse_stack()
            self.insert_bottom(pop_value) 

if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(7)

    s.insert_bottom(0)
    s.reverse_stack()
    s.get_stack()
   

