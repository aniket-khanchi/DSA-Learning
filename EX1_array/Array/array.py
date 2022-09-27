"""
Is it possible to advance from the start of the array to the last element 
given that the maximum you can advance from a position is based on the 
value of the array at the index you are currently present on?
"""

def array_game(l):
    cur_pos = 0
    while cur_pos < len(l) and l[cur_pos] > 0:
        cur_pos = 1 + l[cur_pos]
        cur_pos = l[cur_pos]
        print(cur_pos)
        if cur_pos == len(l) -1:
            print('yeah')


x = [1,3,1,0,2,0,1]
array_game(x)


