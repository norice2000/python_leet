
# Learning curve to understand how to do tuples within a list
## Adding contents to a list
# create empty list
shopping_bag = []
print(f"Empty shopping bag: {shopping_bag}")

# add apple to list
shopping_bag.append("apple")
print(f"Added apple: {shopping_bag}")

## Think of tuple like a items taped together to be a package, this is paired info
fruit_info = ("apple", "red")
print(f"Fruit info: {fruit_info}")
print(f"Name of fruit index 0: {fruit_info[0]}, name of colour index 1: {fruit_info[1]}")

# Now putting tuples inside a list
# create empty list
student_grades = []

# add grades to the tuples 1 by 1
student_grades.append(("Math", "A"))
print(student_grades) #outputs [('Math', 'A')]

student_grades.append(("English", "B"))
print(student_grades) #outputs [('Math', 'A'), ('English', 'B')]

student_grades.append(("Science", "C"))
print(student_grades) # outputs [('Math', 'A'), ('English', 'B'), ('Science', 'C')]

# Now to iterate of getting our list of tuples
print("All Grades")
for i in range(len(student_grades)):
    grade_processed = student_grades[i] # this jumps from 1st tuple, 2nd tuple and 3rd tuple of the list each increment. e.g. student_grades[0] == ('Math', 'A)
    print(f"Subject: {grade_processed[0]}, Grade: {grade_processed[1]}")


# unpack method
for grade_tuple in student_grades:
    subject, grade = grade_tuple #this assigns index 0 = Math, index 1 = A
    print(f"UNPACK METHOD Subject: {subject}, Grade: {grade}")


# barcode practice
config_parts = "0001LAJ5KBX9H8|0003UKURNK403F|0002MO6K1Z9WFA|0004OWRXZFMS2C".split("|")
parsed_configs = []
for config in config_parts:
    print(config)
    ordinal_index = config[:4]
    config_index = config[4:]
    tuple_pair = (ordinal_index, config_index) # creates a tuple
    parsed_configs.append(tuple_pair) # append the list with the tuple

print(str(parsed_configs)) #outputs [('0001', 'LAJ5KBX9H8'), ('0003', 'UKURNK403F'), ('0002', 'MO6K1Z9WFA'), ('0004', 'OWRXZFMS2C')]