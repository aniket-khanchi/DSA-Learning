import mincemeat
#Here we define the data for the mapper input
data = ["Humpty Dumpty sat on a wall",
 "Humpty Dumpty had a great fall",
 "All the King's horses and all the King's men",
 "Couldn't put Humpty together again",
 ]
#Mapper
def mapfn(k, v):
    for w in v.split():
        yield w, 1

#Reducer
def reducefn(k, vs):
    result = 0
    for v in vs:
        result += v
    return result


s = mincemeat.Server()

# The data source can be any dictionary-like object
s.datasource = dict(enumerate(data))
s.mapfn = mapfn
s.reducefn = reducefn


results = s.run_server(password="changeme")
print(results)