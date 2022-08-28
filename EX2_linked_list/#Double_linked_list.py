# Implement doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well.
# That way you can iterate in forward and backward direction. Your node class will look this this,
# class Node:
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
# Add following new methods,

# def print_forward(self):
# This method prints list in forward direction. Use node.next

# def print_backward(self):
#     # Print linked list in reverse direction. Use node.prev for this.
# Implement all other methods in regular linked list class 
# and make necessary changes for doubly linked list (you need to populate node.prev in all those methods)


class Node:
    def __init__(self, data=None, next=None, prev=None ):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_Linked_list:
    def __init__(self):
        self.head = None

    def inser_at_beg(self,data):
        node = Node(data, self.head, None)    # if we have to insert at beg then the next element should be the head of the node 
        # self.head.prev = node               # Which is already present in Double_linked_list 
        self.head = node
        # self.prev = None

    def inser_at_end(self,data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            return 

        itr  = self.head        

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def print_forward(self):
        if self.head is None:
           print("linekd_list is empty")
           return

        itr = self.head
        llstr = " "
        while itr:
            llstr += str(itr.data) + '-->' 
            itr = itr.next      # itr is updated to the next element of the linked_list 
        print(llstr)    

    def get_last_node(self):
        itr = self.head 
        while itr.next:
            # print(str(itr.data))
            itr = itr.next

        return itr   


    def print_backward(self):                          # when we add individual elemnet using inser_at_beg mtd it will ony print th last element sort this out
        if self.head is None:
            print("linekd_list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = " "
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.prev
        print(llstr)   


    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.inser_at_beg(data)
            return

        count = 0 
        itr = self.head
        while itr :
            if count == index -1:
                node = Node(data,itr.next,itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

     def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)    









if __name__ == "__main__" :

    ll = Doubly_Linked_list()
    ll.inser_at_end(10)
    ll.inser_at_end(12)
    # ll.inser_at_end(18)
    ll.print_forward()
    ll.print_backward()
    # print(ll.get_last_node())