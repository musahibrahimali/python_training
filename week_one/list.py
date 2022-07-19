# lists

"""
    - mutable (can be changed)
    - ordered (can be accessed by index)
    - can contain multiple data types
"""

# method 1
my_list = ["name", 2, False, [1,2,4,5], ("age", "height")]
base = ("age", "age", "height")
# constructor method
my_list_const = list(base)
# print(my_list_const)

# list indexing
# index will always start from zero
# print(my_list[0])

# descriptive methods
'''
    - add
    - remove (pop)
'''
# add an item (adds an item to the list)
my_list_const.append("Dinner")

# remove an item (this removes the first instance specified value)
my_list_const.remove("age")
# print(my_list_const)

# remove the last item
my_list_const.pop()
# print(my_list_const) # two items

# remove a specified index from the list
my_list_const.pop(0)
# print(my_list_const)

numbers = [4,5,2,1,3,9,12,0]
# sorted keyword
# this is a function that takes the list as an augument
nums = sorted(numbers) # sorts in ascending order
nums = sorted(numbers, reverse=True) # sorts in the descending order
# print(nums)

# the sort keyword
# this is a property you call on the list (does an inplace sort)
my_numbers = [4,5,2,1,3,9,12,0]
# my_numbers.sort(reverse=True) # reverse = True for the oposite sorting
# print(my_numbers)

# replace an item
my_numbers[1] = 13
print(my_numbers)

# remove everything in a list
# my_numbers.clear()
# print(my_numbers)

# indexing
last_item = my_numbers[-1]
# print(last_item)

# select everything in the list
all_items = my_numbers[:]
# print(all_items)

# select some specific indexes
some_ind = my_numbers[2:4]
print(some_ind)

my_tuple = ("list", "tuple", "set", "dictionary") # immutable
print(my_tuple)

new_list = list(my_tuple)
print(new_list)
