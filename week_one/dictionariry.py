# dictionary

'''
    key, value pairs (key: value)
    similar to JSON (javascript object notation) {"name": "John", "age": "30"}
'''

# create a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# call the key of the dictionary to get the value
print(my_dict["name"])

# add an item
my_dict["job"] = "programmer"

# remove an item (del === used for removing  / deleting)
del my_dict["city"]

# replace an item
my_dict["name"] = "Jane"
print(my_dict)
