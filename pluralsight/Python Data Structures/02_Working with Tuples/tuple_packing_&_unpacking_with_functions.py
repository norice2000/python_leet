# tuple unpacking
def compute_volume(length, width, height):
    return length * width * height

dimensions = (10, 5, 2)
length, width, height = dimensions

#instead of this below we can use the *dimensions since it cointains 3 tuples
# volume = compute_volume(length, width, height)
volume = compute_volume(*dimensions) #this is equiv to dimension[0], dimension[1], dimension[2]
print(f"Volume {volume}")


# Packing function arguments into a Tuple
def sum_numbers(*args):
    print(f"args: {args}")
    return sum(args)

print(f"Sum: {sum_numbers(1,2,3,4,5)}")

# Combining positional and variable length arguments
def generate_report(title, *sections):
    print(f"==={title}===")
    for i, section in enumerate(sections):
        print(f"{i}. {section}")

generate_report("System health Report",
                "CPU usage: 47%",
                "RAM usage: 68%",
                "Disk I/O: Normal")

# output
# ===System health Report===
# 0. CPU usage: 47%
# 1. RAM usage: 68%
# 2. Disk I/O: Normal

# Returning Multiple of Values from a function
def min_max(numbers):
    return min(numbers), max(numbers) #this is returning a tuple, since we can create tuples using <value1>, <value2> due to the comma without ()

n = [1, 20, 33, 21, 22]
min_result, max_result = min_max(n)
print(f"min_result: {min_result}\t max_result: {max_result}")