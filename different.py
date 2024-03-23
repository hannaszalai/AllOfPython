import random


def different(lst):
    unique_set = set(lst)  # Create a set from the list
    unique_list = sorted(list(unique_set))  # Create a sorted list from the set
    return unique_list


random_list = []
for i in range(100):
    random_list.append(random.randint(1, 200))

unique_list = different(random_list)
print("Different integers:")
print(unique_list)
