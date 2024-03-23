import os

test = print(os.getcwd())  # current working directory


#  Returns a list of strings with the names of the directories
def list_dir(dir_path):
    with os.scandir(dir_path) as entries:
        # Use a list comprehension to get the names of the directories
        dir_list = [entry.name for entry in entries if entry.is_dir()]
    return dir_list


#  Returns a list of strings with the names of the files
def list_files(dir_path):
    with os.scandir(dir_path) as entries:
        file_list = [entry.name for entry in entries if entry.is_file()]
    return file_list


# Print directory
def print_directory(dir_path):
    print(f"\nContents of {dir_path}:")
    print("Directories:")
    for directory in list_dir(dir_path):
        print(directory)


def print_files(dir_path):
    print(f"\nContents of {dir_path}:")
    print("Files:")
    for file in list_files(dir_path):
        print(file)


# Program start
# current working directory
dir_path = os.getcwd()
while True:
    # menu options
    print("\n1. List directories\n2. Change directory\n3. List files\n4. Quit")
    # user input
    choice = input("\n==> ")
    if choice == "1":
        print_directory(dir_path)
    elif choice == "2":
        new_dir = input("Name of directory to enter: ")
        if new_dir == "..":
            # Go up one directory:
            # .abspath gets the absolute path !! , .join joins the path,
            # .pardir gets the parent directory of the current
            # directory(dir_path)
            dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
        else:
            # Join the current path with the new directory
            dir_path = os.path.join(dir_path, new_dir)
    elif choice == "3":
        print_files(dir_path)
    elif choice == "4":
        break
