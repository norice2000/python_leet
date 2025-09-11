# path folders
folders = ["home", "user", "documents", "project"]

# For Linux/MacOS use '/'
linux_path = '/'.join(folders)
print(f"Linux/MacOS Path: {linux_path}") # Linux/MacOS Path: home/user/documents/project

# Windows use '\\ (escaped backlash)
windows_path = '\\'.join(folders)
print(f"Windows Path: {windows_path}") # Windows Path: home\user\documents\project

#Use split to remove pattern out
split_linux = linux_path.split('/') # also split it as a list
print(split_linux) #['home', 'user', 'documents', 'project']

# Aggregate Functions!!
readings = [0.0, 0.1, 0.0, 0.2]

print(f"Sum of values: {sum(readings)}")
print(f"Find Max in a list: {max(readings)}")
print(f"Find the Min in a list: {min(readings)}")
print(f"Contains any truthy (boolean true) values using any(): {any(readings)}") # returns true since we have a more than 0.0 e.g. 0.1 and 0.2
print(f"Return falsey if boolean is false using all(): {all(readings)}") # returns false, since we have 2x 0.0 in the list