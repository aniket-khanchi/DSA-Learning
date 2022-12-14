from itertools import count
from multiprocessing import set_forkserver_preload


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
 
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def prepend(self,data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else: 
            new_node = Node(data)
            head = self.head
            cur = self.head
            while cur:
                tail = cur
                cur = cur.next
                if cur == head:
                    break
            tail.next = new_node
            new_node.next = head
            self.head = new_node

    def append(self,data):
        if not self.head :
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head        

    def print_list(self):
        cur = self.head

        while cur:
            print(str(cur.data) + '--' ,end='')
            cur = cur.next
            if cur == self.head:
                break
    
    def remove_node(self,data):
        if self.head.data == data:
            cur = self.head 
            while cur:
                tail = cur
                cur = cur.next
                if cur == self.head:
                    break
            tail.next = self.head.next
            self.head = tail.next
        else:
            cur = self.head
            prev = None
            while cur:
                if cur.data == data:
                    prev.next = cur.next    
                prev = cur
                cur = cur.next
                if cur == self.head:
                    break

    def remove(self, key):
        if self.head:
            if self.head.data == key:
                cur = self.head 
            while cur.next != self.head:
                cur = cur.next 
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = self.head.next
        else:
            cur = self.head 
            prev = None 
            while cur.next != self.head:
                prev = cur 
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next 
                    cur = cur.next
    
    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count
    
    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size ==1:
            return self.head
        
        mid = size//2

        count = 0
        cur = self.head
        head = self.head

        cllist_2 = CircularLinkedList()
        while count < size:
            if count < mid:
                end_1st = cur
            if mid<= count < size:
                cllist_2.append(cur.data)
                # end_2nd = cur
            count+=1
            cur = cur.next
        end_1st.next = head
        return cllist_2.print_list(),print('\n'), self.print_list()

    def split_list(self):
        size = len(self)    

        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size//2
        count = 0

        prev = None
        cur = self.head

        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head 

        split_cllist = CircularLinkedList()
        while cur.next != self.head:
            split_cllist.append(cur.data)
            cur = cur.next
        split_cllist.append(cur.data)

        self.print_list()
        print("\n")
        split_cllist.print_list()

    def remove_node_josephus_problem(self, node):
        if self.head == node:
            cur = self.head 
            while cur.next != self.head:
                cur = cur.next 
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = self.head.next
        else:
            cur = self.head 
            prev = None 
            while cur.next != self.head:
                prev = cur 
                cur = cur.next
                if cur == node:
                    prev.next = cur.next 
                    cur = cur.next

    def josephus_circle(self,step):
        cur = self.head

        length = len(self)
        while length > 1:
            count = 1
            while count != step:
                cur = cur.next
                count +=1 
            print("KILL:" + str(cur.data))
            self.remove_node_josephus_problem(cur)
            cur = cur.next
            length -= 1    
    
        def is_circular_linked_list(self, input_list):
            if input_list.head:
                cur = input_list.head
                while cur.next:
                    cur = cur.next
                    if cur.next == input_list.head:
                        return True
                return False
            else:
                return False
        def is_circular_linked_list(self, input_list):
            if input_list.head:
                cur = input_list.head
                while cur.next:
                    cur = cur.next
                    if cur.next == input_list.head:
                        return True
                return False
            else:
                return False
        

        


cl1 = CircularLinkedList()
cl1.append(3)
cl1.append(5)
cl1.append(9)
cl1.append(2)
cl1.append(7)
cl1.append(4)
cl1.append(10)
cl1.prepend('head')
cl1.josephus_circle(2)
# cl1.split_list()
# cl1.remove_node(4)
# cl1.print_list()
