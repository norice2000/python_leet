# Sorting a List inplace with sort(), this is more applicable for lists

files = ["log.txt", "config.txt", "error.txt", "error.txt"]

# sort by alpha
print(f"Before sort: {files}")
files.sort()
print(f"After sort: {files}")

# sort by in reverse
files.sort(reverse=True)
print(f"Reverse sort: {files}")

# files.reverse()

# Using Sorted is a function where you pass it as an argument
priority = [1, 3, 2]

print(f"Before func sorted: {priority}")
func_sort = sorted(priority)
print(f"After func sorted: {func_sort}") #output After func sorted: [1, 2, 3]

rev_sort = sorted(priority, reverse=True)
print(f"Revered func sorted: {rev_sort}") # Revered func sorted: [3, 2, 1]