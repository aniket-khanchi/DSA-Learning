#linked_list
#Node class
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class linked_list:
#     def __init__(self):
#         self.head = None

#     def printlist(self):
#         temp = self.head
#         while(temp):
#             print(temp.data)
#             temp = temp.next 


# if __name__ == '__main__':

#     list1 = linked_list()
#     list1.head = Node(1)
#     second = Node(2)
#     third = Node(3)


#     list1.head.next = second
#     second.next = third
    
#     list1.printlist()


#______________________________________________________________________________________________________
class Node:
    def __init__(self,data= None,next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None

    def inser_at_beg(self,data):
        node = Node(data,self.head)
        self.head = node  

    def printlist(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = " "
        while itr:
            llstr += str(itr.data)+ '-->'
            itr = itr.next    
        print(llstr)    

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None) 

    def insert_values(self, data_list):
        # self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count    
    
    def remove_at(self, index):
        if index<0 or index>= self.get_length():
            raise Exception('invalid index')
        
        if index ==0:
            self.head = self.head.next
            return

        count = 0 
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
    
            itr = itr.next
            count +=1

    def insert_at(self, index, data):
        if index<0 or index> self.get_length():
            raise Exception('invalid index')        
        
        if index ==0:
            self.inser_at_beg(data)
            return
        
        count = 0
        itr = self.head 
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1    



 

if __name__ == '__main__':
    ll = linked_list()
    # ll.inser_at_beg(5)
    # ll.inser_at_beg(89)
    # ll.insert_at_end(79)
    # ll.insert_at_end(7)
    ll.insert_values(['sky','cloud','sun','rain'])
    # ll.printlist()
    # print(ll.get_length())    
    # ll.remove_at(2)
    ll.insert_at(3,'kim')
    ll.printlist() 
    # print(ll.get_length())   