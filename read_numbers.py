import math
import os


# Calculate the average (mean)
def mean(lst):
    return sum(lst) / len(lst)


# Calculate the standard deviation (szórás)
def std(lst):
    m = mean(lst)
    # Calculate the sum of the squared differences from x and the mean
    sol = sum([(x - m) ** 2 for x in lst])
    # Calculate the average and take the square root
    return math.sqrt(sol / len(lst))


# read a list of integers from a file
def read_file(file_path):
    lst = []
    with open(file_path, 'r') as input_files:
        for line in input_files:
            # Replace , : with space but not the - because those are
            # negative numbers
            line = line.replace(',', ' ').replace(':', ' ')
            # Split the line into a list of strings using spaces
            numbers = line.strip().split(' ')
            # Add integers to list as a string
            for n in numbers:
                lst.append(n)
        int_lst = [int(n) for n in lst if n]  # Convert strings to integers
    return int_lst


home = os.getcwd()
path = home + "/1DV501/hs223xt_assign3/assignment-03/"

file_a_path = path + 'file_10k_integers_A.txt'
file_b_path = path + 'file_10k_integers_B.txt'

lst_a = read_file(file_a_path)
lst_b = read_file(file_b_path)

mean_a = mean(lst_a)
std_a = std(lst_a)
mean_b = mean(lst_b)
std_b = std(lst_b)


print(f"\nResults for file A:\nmean = {mean_a:.1f}, " +
      f"standard deviation = {std_a:.1f}\n")
print(f"Results for file B:\nmean = {mean_b:.1f}, " +
      f"standard deviation = {std_b:.1f}")
