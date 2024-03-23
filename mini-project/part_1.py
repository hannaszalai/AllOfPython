import os


# return a list of words
def get_words(path, file_name):
    words = []
    # Open the input file for reading
    with open(os.path.join(path, file_name),
              'r', encoding='utf-8') as input_file:
        for line in input_file:
            # Split the line into raw words using spaces
            line_words = line.strip().split(' ')
            for word in line_words:
                # Remove any non-alphabetic characters from the word
                cleaned_word = ''
                for c in word:
                    # isalpha() checks if c is an alphabetic character
                    # (a letter)
                    # checks if c is a single quote or a dash
                    if c.isalpha() or c in ["'", '-']:
                        cleaned_word += c  # add c to cleaned worlds
                # Convert the word to lowercase and add it to the list
                # if it's not empty
                if cleaned_word:
                    # Convert to lowercase and add to list
                    words.append(cleaned_word.lower())
    return words


# Main program starts - 1st file
path = os.getcwd()
input_file = 'brian_13374_words.txt'

words = get_words(path, input_file)

# Count the number of unique words
unique_words = set(words)
print(f'\nNumber of unique words in {input_file}: {len(unique_words)}')


# Top 10 list most frequently used words having a length larger than 4
word_counts = {}  # empty dictionary
for word in words:
    if len(word) > 4:
        if word in word_counts:
            # increment the value associated with the key [word] in the
            # dictionary word_counts by 1
            word_counts[word] += 1
        else:
            word_counts[word] = 1  # the words has been seen once so far
# sort the dictionary by count where x is a tuple (word, count)
sorted_word_counts = sorted(word_counts.items(),
                            key=lambda x: x[1], reverse=True)
top_10_words = sorted_word_counts[:10]

top_10_words_list = [(word, count) for word, count in top_10_words]
output = ', '.join(f'("{word}", {count})' for word, count in top_10_words_list)

print(f'\nTop 10 most frequently used words in {input_file}:\n{output}')


# Main program starts - 2nd file
path = os.getcwd()
input_file = 'swe_news_15102686_words.txt'

words = get_words(path, input_file)

# Count the number of unique words
unique_words = set(words)
print(f'\nNumber of unique words in {input_file}: {len(unique_words)}')


# Top 10 list most frequently used words having a length larger than 4
word_counts = {}  # empty dictionary
for word in words:
    if len(word) > 4:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            # sort the dictionary by count
sorted_word_counts = sorted(word_counts.items(),
                            key=lambda x: x[1], reverse=True)
top_10_words = sorted_word_counts[:10]  # top 10 words

top_10_words_list = [(word, count) for word, count in top_10_words]
output = ', '.join(f'("{word}", {count})' for word, count in top_10_words_list)

print(f'\nTop 10 most frequently used words in {input_file}:\n{output}')
