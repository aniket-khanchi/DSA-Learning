# #tester
# a = [4,2,3,1,5,6]

# if a.count(7) == 1:
#     b=a.index(7)
#     "Do something with variable b"

# # print(a.count(4))    

# #_____________________________________________________________________________________________________________________________________________
# a = [4,2,3,1,5,6]

# try:
#     b=a.index(4)
# except ValueError:
#     print("Do nothing")
# else:
#     print("Do something with variable b")

# def com():
    
#     n = 2
    
#     def com2():
#         nonlocal n
#         n = 4 
#         print(n)

#     com2()
#     print(n)    

# com()

# def outer():
#     """Prints the value of n."""    
#     n = 1
    
#     def inner():
#         # nonlocal n        
#         n = 2        
#         print(n)    
        
#     inner()    
#     print(n)
    
# outer()        


ll = [ 1,2,3,4,5,6,7]
a = ll[0]
while a in range(len(ll)):
    print(ll[a])