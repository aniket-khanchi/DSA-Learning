#implementation of hashmap in python
def get_hash(key):
    hash = 0 
    for char in key:
        hash += ord(char)
    return hash % 100    

# print(get_hash("march 6"))    

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [ None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)      #       
        return hash % self.MAX
    
    def __getitem__(self, index):  # these __getitem__ are in build python operators 
        h = self.get_hash(index)   # and we can overide them for our own use 
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val 


        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None    



t = HashTable()
t["march 6"] = 310
print(t.arr)       

