#set are unordered unique
collection = {1,2,3,4,5}
collection.add(6)
collection.remove(1)
collection.add("I am meredith")
collection.add(("Oracle","Damon","Stephan"))
#print(collection)
#print(len(collection))
#print(type(collection))

#duplicates will be ignored
duplicate = {"Vismaya"}
#duplicate.clear()
#print(duplicate)
#print(len(duplicate))
print(collection.union(duplicate))




 