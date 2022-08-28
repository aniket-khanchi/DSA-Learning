
#implement chaining in python to handle collisions
# t["march 6"] = 120
# t["march 17"] = 459

# print(t.get_hash('march 6'))
# print(t.get_hash('march 17'))
# although for both we are getting diff index if it would be same then
#the last item would overwrite the previous one
# print(t.arr)

class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):     # we are iterating in a element at index h 
            if len(element)==2 and element[0] == key:   # we are going to replace the element at this index. Remember the key here will be passed by us 
                self.arr[h][idx] = (key,val)            # since tuples are immutable therefore we will replace the element
                found = True                               
        if not found:
            self.arr[h].append((key,val))               # if not founded then we will add the tuple of key value pair
        
    def __delitem__(self, key):
        arr_index = self.get_hash(key)                   
        for index, kv in enumerate(self.arr[arr_index]):    
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]


t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457                
del t['march 8']
print(t.arr)
# del t['march 8']