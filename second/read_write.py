import os


# This function reads a text file
def read_file(file_path):
    with open(file_path, 'r') as input_file:  # in read mode
        lines = input_file.readlines()
    return lines
# input_file.read() = read the whole file as a string
# input_file.readline() = read one line at a time


# This function writes a text file from a list of lines
def write_file(lines, file_path):
    with open(file_path, 'w') as f:  # in write mode
        f.writelines(lines)  # # write each line in the list to the file
# input_file.write() = write a single string to a file
# input_file.writelines() = write a list of strings to a file (lines)


# Program starts
path = os.getcwd() + "/1DV501/hs223xt_assign3/assignment-03/mamma_mia.txt"

# Read text file
lst = read_file(path)
print(f"\nRead {len(lst)} lines from file {path}")

# Write text file
# Name the file
path = os.getcwd() + "/1DV501/hs223xt_assign3/assignment-03/output.txt"
write_file(lst, path)  # Save to a new file
print("\nText saved in file", path)
