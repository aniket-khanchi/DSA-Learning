# Implement hash table where collisions are handled using linear probing. 
# We learnt about linear probing in the video tutorial.
# Take the hash table implementation that uses chaining and modify methods to use linear probing. 
# Keep MAX size of arr in hashtable as 10.

#issues in this code 
# 1. cant update a value of a given key
# 2. last index in the array
#

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
            hash += ord(char)             
        return hash % self.MAX
    
    def __getitem__(self, index):  # these __getitem__ are in build python operators 
        h = self.get_hash(index)   # and we can overide them for our own use 
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)

        if self.arr[h] != None:
            for i in range(h,len(self.arr)):
                if self.arr[i] == None:
                    self.arr[i] = val
                    break
        elif h == len(self.arr)-1 and self.arr[h] != None:
            for j in range(len(self.arr)):
                if self.arr[j] == None:
                    self.arr[j] = val
        else:    
            self.arr[h] = val 


        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None    



t = HashTable()
t["march 6"] = 310
print(t.arr)       

t['aniketzzw'] = 55555
t['ramanmzzw'] = 22222
t['aniket'] = 3423
t['aniket'] = 235
t['ag'] = 21
t['bf'] = 35
print(t.arr)       