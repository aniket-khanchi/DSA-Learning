#DSA_EX_1_2
#You have a list of your favourite marvel super heros.

heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange
#    (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order 
#    (Hint. Use dir() functions to list down all functions available in list)

#ANS1
print (len(heros))

#ANS2
heros.append("black panther")
print(heros)

#ANS3
heros.pop(-1)
print("black panther is removed",heros)
heros.insert(3,"black panther")
print("black panther is added after hulk",heros)

#ANS4
heros[1:3] = ['doctor strange']  # different items in a lsit can be replaced by list only 
print(heros)  

#ANS5
heros.sort()
print(heros)

#Given Solution

# 2. You have a list of your favourite marvel super heros
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this list

heros=['spider man','thor','hulk','iron man','captain america']
# 1. Length of the list
print(len(heros))
# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]=['doctor strange']
print(heros)
# 5. Sort the list in alphabetical order
heros.sort()
print(heros)
