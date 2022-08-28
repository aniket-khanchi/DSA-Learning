def get_hash(key):
    hash = 0 
    for char in key:
        hash += ord(char)
    return hash % 100    


print(get_hash('aniketzzw'))
print(get_hash('ramanmzzw'))
print(get_hash('ag'))
print(get_hash('bf'))

x = [*range(0,5)]
print(x)

