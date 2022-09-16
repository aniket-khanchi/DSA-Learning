from itertools import count
from multiprocessing import set_forkserver_preload


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
 
class CicularLinkedList:
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

        cllist_2 = CicularLinkedList()
        while cur.next != self.head:
            if count < mid:
                end_1st = cur
            if mid<= count < size:
                cllist_2.append(cur.data)
                # end_2nd = cur
            count+=1
            cur = cur.next
        end_1st.next = head
        return cllist_2.print_list()


        

        


        
    
        
            

            




                



cl1 = CicularLinkedList()
cl1.append(3)
cl1.append(5)
cl1.append(9)
cl1.append(2)
cl1.append(7)
cl1.append(4)
cl1.prepend('head')
cl1.split_list()
# cl1.remove_node(4)
cl1.print_list()
