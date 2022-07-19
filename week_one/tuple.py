# tuples

'''
    - array like list
    - immutable (cannot be changed once set)
    - all the methods on list is also accessible here
'''

my_tuple = ("list", "tuple", "set", "dictionary")
# all indexing methods
print(my_tuple[:3])

# remove an item 
# my_tuple.remove() # this will return an error
# print(my_tuple)

# cant replace items
# my_tuple[1] = 1

my_tuple = ("list", ["tuple", "set"], "dictionary", False, 34)
my_tuple[1][0] = "changed"
print(my_tuple)



