routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

for start, end in routes:
    print(start,end)


x = {2:[1,2,3],5:[2,5,6]}    
x[3] = [2,3,4]
print(x)


