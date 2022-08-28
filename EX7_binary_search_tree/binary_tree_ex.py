# Add following methods to BinarySearchTreeNode class

# 1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. calculate_sum(): calcualtes sum of all elements
# 4. post_order_traversal(): performs post order traversal of a binary tree
# 5. pre_order_traversal(): perofrms pre order traversal of a binary tree

class BinarySearchTreeNode:
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:    # as data in the nodes should be unique 
            return               # NOde already exists  

        if data < self.data:                  # then it should goes into left leaf node
            # add data in left subtree
            if self.left:                     # if there is already some element in leaf node then  
                self.left.add_child(data)     # recursively same process again                    
            else:
                self.left = BinarySearchTreeNode(data)                  
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
         

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements


    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements       


    def find_max(self):
        x = self.in_order_traversal()
        return x[-1]

    def find_min(self):
        x = self.in_order_traversal()
        return x[0]

    def cal_sum(self):
        x = sum(self.in_order_traversal())            
        return x

    # def pre_order_traversal(self):
        
    #     return


def build_tree(elements):
        print("Building tree with these elements:",elements)
        root = BinarySearchTreeNode(elements[0])

        for i in range(1,len(elements)):
            root.add_child(elements[i])

        return root


if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print("max_num:",numbers_tree.find_max())
    print("min_num:",numbers_tree.find_min())
    print("cal_sum:",numbers_tree.cal_sum())
    print("post_order_traversal:",numbers_tree.post_order_traversal())
    print("pre_order_traversal:",numbers_tree.pre_order_traversal())
    


