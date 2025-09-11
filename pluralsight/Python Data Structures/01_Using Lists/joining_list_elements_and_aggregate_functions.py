# path folders
folders = ["home", "user", "documents", "project"]

# For Linux/MacOS use '/'
linux_path = '/'.join(folders)
print(f"Linux/MacOS Path: {linux_path}") # Linux/MacOS Path: home/user/documents/project

# Windows use '\\ (escaped backlash)
windows_path = '\\'.join(folders)
print(f"Windows Path: {windows_path}") # Windows Path: home\user\documents\project

#Use split to remove pattern out
split_linux = linux_path.split('/')
print(split_linux) #['home', 'user', 'documents', 'project']