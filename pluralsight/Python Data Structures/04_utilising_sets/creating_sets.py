# Sets are unique amd remove duplicates
# sets are unordered
my_set = {1, 2, 3, "s1", "s2"}
print(f"my set: {my_set}")

# Create empty sets with the set() constructor
empty_set = set()
print(f"Empty set: {empty_set}")

#output
# my set: {1, 2, 3, 's2', 's1'}
# Empty set: set()

# Empty curly braces would create a dictionary,  e.g empty_dict = {}

#set removing duplicates
set_rm_dupl = {1, 1, 2, 2, 3, 3}
print(f"my_set: {set_rm_dupl}")

# set can be used to remove duplicates

# sets and strings
string_set = set("Hello")
print(f"string_set: {string_set}")
# string_set: {'l', 'o', 'H', 'e'}

string_set = {"Hello"} #this assumes you create an empty set()
print(f"string_set: {string_set}")
# string_set: {'Hello'} 


# aggregate fucntions
number_sets = {3, 2, 7,9, 5} #this is already a set

print(f"Number in elements: {len(number_sets)}")
print(f"Sum in elements: {sum(number_sets)}")
print(f"minimum in elements: {min(number_sets)}")
