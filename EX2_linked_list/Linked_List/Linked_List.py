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
    
    def del_value(self,val):
        if val == self.head.data:
            self.head = self.head.next
        else:
            itr = self.head
            while itr.data:
                if str(itr.next.data) == val:
                    prev_itr =  itr
                    prev_itr.next = itr.next.next
                    break
                itr = itr.next

    def delete_node(self, key):   #Another method to delete the node
  
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next 
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next 

        if cur_node is None:
            return 
        
        prev.next = cur_node.next
        cur_node = None
    
    def index(self,index):
        itr = self.head
        if index >= 0:
            for i in range(index):
                itr = itr.next 
            if itr == None:
                print('Index out of Range')
            else:
                return itr.data
        else:
            print('Not defined for negative index')

    def del_at_index(self,index):
        curr_node = self.head
        index_element = self.index(index)
        if index == 0:
               self.head = curr_node.next 
        else:
            for i in range(index):
                if curr_node.next.data == index_element:
                    prev_index_element = curr_node
                    break
                curr_node = curr_node.next
            prev_index_element.next = prev_index_element.next.next 
            # index_element.next = None

    def delete_node_at_pos(self, pos):   #Another method to Delete node at a index
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node 
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return 

            prev.next = cur_node.next
            cur_node = None

    


# if "__name__" == "__main__":
llist = LinkedList()
llist.append("3")
llist.append("4")
llist.append("5")
llist.append("6")
llist.insert_after(2,9)
llist.del_at_index(4)
# llist.del_value("6")
# llist.index(-4)
llist.printl()


