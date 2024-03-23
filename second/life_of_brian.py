import os


# return a list of words
def get_words(path, file_name):
    words = []
    # Open the input file for reading
    with open(os.path.join(path, file_name), 'r') as input_file:
        for line in input_file:
            # Split the line into raw words using spaces
            line_words = line.strip().split(' ')
            for word in line_words:
                # Remove any non-alphabetic characters from the word
                cleaned_word = ''
                for c in word:
                    # check if c is a valid character
                    if c.isalpha() or c in ["'", '-']:
                        cleaned_word += c  # add c to cleaned worlds
                # Convert the word to lowercase and add it to the list
                # if it's not empty
                if cleaned_word:
                    # Convert to lowercase and add to list
                    words.append(cleaned_word.lower())
    return words


# Save a list of words to a file, one word per line
def save_words(path, file_name, words):
    with open(os.path.join(path, file_name), 'w') as output_file:
        for word in words:
            output_file.write(word + '\n')


# Main program starts
path = os.getcwd() + '/1DV501/hs223xt_assign3/assignment-03/'
input_file = 'life_of_brian.txt'

words = get_words(path, input_file)

output_file = f'brian_{len(words)}_words.txt'

save_words(path, output_file, words)
print(f'\nSaved {len(words)} words in the file '
      f'{os.path.join(path, output_file)}')
