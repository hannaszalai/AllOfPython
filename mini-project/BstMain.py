import BstMap

# Create a new BST for brian_13374_words.txt
bst_map = BstMap.BstMap()

with open('brian_13374_words.txt', 'r', encoding='utf-8') as file1:
    text = file1.read()
    words1 = text.split()  # need to split to filter words


# See if a word is in the map
for word in words1:
    word = word.lower()  # Convert all words to lowercase
    if len(word) > 4:  # Ckeck the lenght of the word
        if bst_map.get(word) is not None:  # Check if the word is in the BST
            # If yes, update the count by increase the value by 1
            bst_map.put(word, bst_map.get(word) + 1)
        else:
            # If no, add the word to the BST with the value of 1
            bst_map.put(word, 1)

lst = bst_map.as_list()


# Sort the list of tuples by the value of the words
lst.sort(key=lambda x: x[1], reverse=True)


# create a list of the top 10 words
top_10 = []
for pairs in lst:
    # Check if the word is longer than 4
    if len(pairs[0]) > 4:
        top_10.append(pairs)
        if len(top_10) == 10:  # Stop when the list has 10 words
            break

# Print the top 10 words
top_10_words_list = [(word, count) for word, count in top_10]

output_lst = []
for word, count in top_10_words_list:
    output_lst.append(f'("{word}", {count})')

output = ', '.join(output_lst)


print('\nTop 10 most frequently used words in '
      f'brian_13374_words.txt:\n{output}')

# a) number of tree nodes
number_of_nodes = bst_map.root.count()
print(f"\nNumber of tree nodes: {number_of_nodes}")

# b) max depth
max_tree_depth = bst_map.max_depth()
print(f"\nMax depth of the BST: {max_tree_depth}")

# c) internal node count of the BST when adding all words (as both
# key and value)
internal_node_count = bst_map.count_internal_nodes()
print(f"\nInternal node count: {internal_node_count}")


# Create a new BST for swe_news_15102686_words.txt
bst_map = BstMap.BstMap()


with open('swe_news_15102686_words.txt', 'r', encoding='utf-8') as file2:
    text = file2.read()
    words2 = text.split()


# See if a word is in the map
for word in words2:
    word = word.lower()  # Convert all words to lowercase
    if len(word) > 4:  # Ckeck the lenght of the word
        if bst_map.get(word) is not None:  # Check if the word is in the BST
            # If yes, update the count by increase the value by 1
            bst_map.put(word, bst_map.get(word) + 1)
        else:
            # If no, add the word to the BST with the value of 1
            bst_map.put(word, 1)


lst = bst_map.as_list()


# Sort the list by the value of the words
lst.sort(key=lambda x: x[1], reverse=True)


# create a list of the top 10 words
top_10 = []
for pairs in lst:
    # Check if the word is longer than 4
    if len(pairs[0]) > 4:
        top_10.append(pairs)
        if len(top_10) == 10:  # Stop when the list has 10 words
            break


# Print the top 10 words
top_10_words_list = [(word, count) for word, count in top_10]

output_lst = []
for word, count in top_10_words_list:
    output_lst.append(f'("{word}", {count})')

output = ', '.join(output_lst)


print('\nTop 10 most frequently used words in '
      f'swe_news_15102686_words.txt:\n{output}')

# a) number of tree nodes
number_of_nodes = bst_map.root.count()
print(f"\nNumber of tree nodes: {number_of_nodes}")

# b) max depth
max_tree_depth = bst_map.max_depth()
print(f"\nMax depth of the BST: {max_tree_depth}")

# c) internal node count of the BST when adding all words (as both
# key and value)
internal_node_count = bst_map.count_internal_nodes()
print(f"\nInternal node count: {internal_node_count}")
