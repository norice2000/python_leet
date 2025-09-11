# Unpacking Requires the Same Number of Variables as List Elements, if this is not met a ValueError will be raised
dimensions = [10, 20, 5]

# list unpack each element
# remove the need of index assignment
width, height, depth = dimensions

print(f"width: {width}")
print(f"height: {height}")
print(f"depth: {depth}")


# Example of too many variables
user_info = ["champ", "lucky", "lulu"]

try:
    name, job, country, dob = user_info
except ValueError as e:
    print(f"Too many variables {e}")

# too few
try:
    name,job = user_info
    
except ValueError as e:
    print(f"Too few {e}")

# Extended unpackwithing with the Star * Operator, which only works for the last variable if you are unsure
http_response = [200, "OK", "Data loaded succesfully", "Time: 0.22s"]

try:
    status_code, condition, *message = http_response
    print(f"status_code: {status_code} \t condition: {condition} \n message: {message}")
except ValueError as e:
    print(f"unknonw: {e}")

# outputs
# status_code: 200         condition: OK 
#  message: ['Data loaded succesfully', 'Time: 0.22s']
