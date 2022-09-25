#adding


from hashlib import new


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur


    def prepend(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node


    def print_list(self):
        cur = self.head
        while cur:
            print(str(cur.data) + ' <----> ',end='')
            cur = cur.next
    
    def add_node_before(self,index,data):
        cur = self.head
        previous = None
        #next = None
        node_index = 0
        while cur:
            if node_index == index:
               new_data = Node(data)
               previous.next = new_data
               new_data.prev = previous
               new_data.next = cur
               cur.prev = new_data 
            previous = cur
            cur = cur.next
            
            node_index += 1

    #add node before by using data point

    def add_node_before_via_key(self,key,data):
        cur = self.head
        previous = None
        while cur:
            if cur.data == key:
               new_data = Node(data)
               previous.next = new_data
               new_data.prev = previous
               new_data.next = cur
               cur.prev = new_data 
            previous = cur
            cur = cur.next
    
    def add_node_after(self,index,data):
        cur = self.head
        #previous = None
        next_node = cur.next
        node_index = 0
        while cur:
            if node_index == index:
                if next_node == None:
                    new_data = Node(data)
                    cur.next = new_data
                    new_data.prev = cur
                    break                  
                else:
                    new_data = Node(data)
                    next_node.prev = new_data
                    new_data.prev = cur
                    new_data.next = next_node
                    cur.next = new_data
                    break
                
            next_node = next_node.next 
            cur = cur.next
            
            node_index += 1


    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next 
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur 
                nxt.prev = new_node
                return
            cur = cur.next
    
    def add_before_node(self, key, data):
        cur = self.head 
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
                return 
            cur = cur.next

    #delete a Node

    def del_node(self,data):
        cur = self.head
        while cur:
            if cur.data == data:
                # deleting the only node present
                if not cur.next and cur ==self.head:
                    cur = None
                    self.head = None
                    return
                # deleting the head node
                elif cur.data == self.head.data:
                    self.head = cur.next
                    cur = None
                    return
                #Deleting node other than head where cur.next is None
                elif cur.next == None:
                    prv =cur.prev
                    prv.next = None
                    cur = None
                    return
                #Deleting node other than head where cur.next is not None
                else:
                    nxt = cur.next
                    prv = cur.prev
                    prv.next = nxt
                    nxt.prev = prv      
            cur = cur.next    
            
            
                
                


dll1 = DoublyLinkedList()
dll1.append(2)
dll1.append(4)
dll1.append(5)
dll1.append(7)
dll1.append(8)
dll1.prepend(0)
# dll1.add_node_after(5,50)
dll1.del_node(8)
dll1.print_list()


