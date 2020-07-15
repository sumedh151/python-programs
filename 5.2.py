import os

print("OS name is : ",os.name)
print("\n\n")

print("Current working directory is: ",os.getcwd())
print("\n\n")

print("absolute path on the system is: ",os.path.abspath('.'))
print("\n\n")

print("files and directories in the current directory are: ",os.listdir('.'))
print("\n\n")

print("os dir is: ",dir(os))
print("\n\n")

print("os directories are: ", os.mkdir('sub_dir1'))
print("\n\n")

print("Renaming OS directories: ",os.rename('sub_dir1','sub_dir_renamed'))
print("\n\n")

print("Making directories: ",os.makedirs('sub_dir_renamed/inside_sub'))
print("\n\n")

print("Changing directories: ",os.chdir('sub_dir_renamed/inside_sub'))
print("\n\n")

print("Removing directories: ",os.rmdir('sub_dir_renamed\inside_sub'))
print("\n\n")

