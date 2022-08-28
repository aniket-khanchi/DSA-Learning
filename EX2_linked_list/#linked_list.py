# linked_list

# Node is sub class of linked_list class
class Node:
    def __init__(self,data= None,next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None    #A linked list is represented by a pointer to the first node of the linked list.
                            #The first node is called the head. If the linked list is empty, then the value of the head is NULL.

    def inser_at_beg(self,data):
        node = Node(data,self.head)    # if we have to insert at beg then the next element should be the head of the node 
        self.head = node               #then assign the node as head since its at beginning

    def printlist(self):
        if self.head is None:             
            print("Linked list is empty")
            return

        itr = self.head        #itr is head of a linked_list
        llstr = " "
        while itr:
            llstr += str(itr.data) + '-->' 
            itr = itr.next      # itr is updated to the next element of the linked_list
        print(llstr)    

    def insert_at_end(self, data):      
        if self.head is None:           # if head of a linked_list is empty
            self.head = Node(data, None)  #then last element will become head of the linked_list
            return
        
        itr = self.head
        while itr.next:      # we will iterate uptill we get to the last element in linkd_list
            itr = itr.next   

        itr.next = Node(data, None) # then we put last iteration as the node we want to append at last

    def insert_values(self, data_list):  # when we want to add a list of values 
        self.head = None
        for data in data_list:
            self.insert_at_end(data)  # make use of insert_at_end method we created above


    def get_length(self): # length of linked_list
        count = 0         
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count    
    
    def remove_at(self, index):    
        if index<0 or index>= self.get_length():  # because index start at 0 therefore index equal to length will also be invalid
            raise Exception('invalid index')
        
        if index ==0:
            self.head = self.head.next # just make the next element as the head of the linked_list
            return

        count = 0 
        itr = self.head
        while itr:
            if count == index -1:                # you have to stop just one before the given index to
                itr.next = itr.next.next         #replace its next element by its next element
                break
    
            itr = itr.next
            count +=1

    def insert_at(self, index, data):                
        if index<0 or index > self.get_length():  #we cannot insert an element at a index of lists length 
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

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head 
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break

            itr = itr.next  
              
    def remove_by_value(self, data):
        if self.head is None:
                return

        if self.head.data == data:
                self.head = self.head.next
                return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            
            itr = itr.next    




if __name__ == '__main__':
    ll = linked_list()
    # ll.inser_at_beg(5)
    # ll.inser_at_beg(89)
    # ll.insert_at_end(79)
    # ll.insert_at_end(7)
    # ll.insert_values(['sky','cloud','sun','rain'])
    # # ll.printlist()
    # # print(ll.get_length())    
    # # ll.remove_at(2)
    # ll.insert_at(3,'kim')
    # ll.printlist() 
    # print(ll.get_length())   
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.printlist()
    ll.insert_after_value("mango","apple")
    ll.printlist()
    ll.remove_by_value("orange")
    ll.printlist()
    ll.remove_by_value("figs")
    ll.printlist()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.printlist()
    
    