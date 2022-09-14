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
                if cur.next == head:
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
                cur = cur.next
                prev = cur
                if cur == self.head:
                    break 
                



cl1 = CicularLinkedList()
cl1.append(3)
cl1.append(5)
cl1.append(9)
cl1.append(2)
cl1.append(7)
cl1.append(4)
cl1.prepend('head')
cl1.remove_node(2)
cl1.print_list()
