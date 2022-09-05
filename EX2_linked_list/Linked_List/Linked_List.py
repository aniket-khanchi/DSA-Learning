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
    
    def length(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count+=1
            curr_node = curr_node.next
        return count

    def len_recursive(self, node): #recursive method to find length of linked list
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def node_swap(self,n1,n2):
        prev_node = None
        curr_node = self.head
        while curr_node:
            if curr_node.data == n1:
                n1_curr_node = curr_node
                n1_prev_node = prev_node
            if curr_node.data == n2:
                n2_curr_node = curr_node
                n2_prev_node = prev_node
                break
            prev_node = curr_node
            curr_node = curr_node.next
        n1_prev_node.next.data,n2_prev_node.next.data =  n2_curr_node.data,n1_curr_node.data
        # n2_prev_node.next = n1_curr_node
    
    def swap_nodes(self, key_1, key_2): # Another way to Swap Nodes

        if key_1 == key_2:
            return 

        prev_1 = None 
        curr_1 = self.head 
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1 
            curr_1 = curr_1.next

        prev_2 = None 
        curr_2 = self.head 
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2 
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return 

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next
    
    def reverse_iterative(self):
        prev = None 
        cur = self.head
        while cur:
            nxt = cur.next   #storing the next element
            cur.next = prev  #reversing the pointer --making curr next element previous one
            prev = cur       #moving the prev to curret node
            cur = nxt        #moving the curr node to next
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None) 

    #Merge Two Sorted Linked Lists
    def merge(self,ll1,ll2):
        p = ll1.self.head
        s = None
        q = ll2.self.head
        while p or q :
            if p.data > q.data:
                s = q
                q = q.next
                
            elif p.data< q.data:
                s = p
                p = p.next
            else:
                pass
        

        

        


# if "__name__" == "__main__":
llist = LinkedList()
llist.append("3")
llist.append("4")
llist.append("5")
llist.append("6")
llist.insert_after(2,9)
# llist.node_swap("4","5")
# llist.swap_nodes("4","5")
# llist.del_at_index(4)
# print(llist.len_recursive(llist.head))
# llist.del_value("6")
# llist.index(-4)
llist.reverse_recursive()
llist.printl() # orignal llist 3 4 9 5 6


