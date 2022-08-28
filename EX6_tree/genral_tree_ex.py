#tree_ex_1
class TreeNode:
    def __init__(self,name,post):
        self.name = name
        self.post = post
        self.children = []    #there could be multiple childrens of parent node 
        self.parent = None   #the will be no parent of node element

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self,property):
        if property == "both":
            value = self.name + "(" +  self.post + ")"
        elif property == "name":  
            value = self.name
        else:
            value = self.post

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else "" #ternary operator
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property)

    def add_child(self,child):
        child.parent = self          #the object of instance will act as the aprent of the child element
        self.children.append(child)    # now you are adding the child to self hence self will become its parent

def build_management_tree():
     # CTO Hierarchy
    infra_head = TreeNode("Vishwa","Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels","HR Head")

    hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo




    
if __name__ == "__main__":  
    root_node = build_management_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")