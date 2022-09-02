class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):   
        new_node = Node(data)
        #empty linked list case
        if self.head == None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  #self.head is a node which will have a pointer to the next element 
            last_node = last_node.next
        last_node.next = new_node
    
    def printl(self):
        itr = self.head
        while itr:
            print(str(itr.data) + '-+-', end=' ')
            itr = itr.next
        

    def prepend(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_after(self,index,value):
        itr = self.head
        for i in range(index):
            itr_bi = itr
            itr = itr.next
        new_node = Node(value)
        new_node.next = itr
        itr_bi.next = new_node 

# if "__name__" == "__main__":
llist = LinkedList()
llist.append("3")
llist.append("4")
llist.append("5")
llist.append("6")
llist.insert_after(2,9)
llist.printl()


