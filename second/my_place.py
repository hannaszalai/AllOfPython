import os

place = os.getcwd()
print(f"I am righ now at: {place}")


def count_directories(dir_path):
    count = 0
    for i in os.listdir(dir_path):
        if os.path.isdir(i):
            count += 1
    return count


print(f"Below me I have {count_directories(place)} directories/folders")


def count_files(dir_path):
    count = 0
    for i in os.listdir(dir_path):
        if os.path.isfile(i):
            count += 1
    return count


print(f"This directory contains {count_files(place)} files")
