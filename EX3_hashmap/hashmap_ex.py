# poem.txt Contains famous poem "Road not taken" by poet Robert Frost.
# You have to read this file in python and print every word and its count as show below. 
# Think about the best data structure that you can use to solve this problem and 
# figure out why you selected that specific data structure.

with open('C:\\Users\\khanc\\Desktop\\DSA\\EX_3_hashmap\\poem.txt','r') as f:
    count = 0
    words = {}
    for i in f:
        tokens = i.split(" ")
        for j in tokens:
            j=j.replace('\n','')
            if j in words:
                words[j] +=1
            else:
                words[j] = 0    
            # words.append(j)

        print(count)
        count +=1
    print(words)
        