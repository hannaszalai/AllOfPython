import random


def count_occurrences(lst):
    counts = {}  # create an empty dictionary
    for k in lst:
        if k in counts:
            counts[k] += 1
        else:
            counts[k] = 1
    # sort the dictionary by key using lambda, first element (0)
    key_sorted = dict(sorted(counts.items(), key=lambda tpl: tpl[0]))
    return key_sorted


# Create a list
random_list = []
for i in range(100):
    random_list.append(random.randint(1, 10))

counts = count_occurrences(random_list)  # count the occurencies
for k in sorted(counts.keys()):
    print(f"{k}\t{counts[k]}")
