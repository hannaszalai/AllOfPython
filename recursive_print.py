import os


# Recursive function
def print_sub_1(dir_path, n):
    # Current directory,
    # .basename returns the last component of the path (current)
    print(os.path.basename(dir_path))

    # Subdirectories in the current directory
    # .listdir to get a list of all the entries in the directory:
    # (files, directories)
    # .isdir to check if the entry is a directory
    subdirectories = [entry for entry in os.listdir(dir_path)
                      if os.path.isdir(os.path.join(dir_path, entry))]
    # Sorts the list
    for subdir in subdirectories:
        # + 1 to the depth of the directory
        print_sub_1(os.path.join(dir_path, subdir), n + 1)


# Starts the recursive call sequence
def print_sub(dir_path):
    print_sub_1(dir_path, 0)  # 0 is the starting level (depth of directory)


# Program starts
current_path = os.getcwd()
print_sub(current_path)
