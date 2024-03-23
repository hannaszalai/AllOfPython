import hashset


def count_unique_words_in_text_file(file_name1):
    word_set = hashset.HashSet()

    # Open the text file
    with open(file_name1, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()  # Split line into list of words
            for word in words:
                word_set.add(word)  # Add each word to set

    # Get statistics
    unique_word_count = word_set.get_size()
    bucket_list_size = word_set.bucket_list_size()
    max_bucket_size = word_set.max_bucket_size()
    zero_bucket_ratio = word_set.zero_bucket_ratio()

    # return statistics
    return (unique_word_count, bucket_list_size,
            max_bucket_size, zero_bucket_ratio)


file_name1 = "brian_13374_words.txt"

# call the function
unique_word_count, bucket_list_size, max_bucket_size, \
    zero_bucket_ratio = count_unique_words_in_text_file(file_name1)

# print the statistics
print(f"\nNumber of unique words in {file_name1}: {unique_word_count}")
print(f"\nBucket List Size for {file_name1}: {bucket_list_size}")
print(f"\nMax Bucket Size for {file_name1}: {max_bucket_size}")
print(f"\nZero Bucket Ratio for {file_name1}: {zero_bucket_ratio:.2f}")


print("\n*****************************************************")


def count_unique_words_in_text_file(file_name2):
    word_set = hashset.HashSet()

    # Open the text file
    with open(file_name2, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_set.add(word)

    unique_word_count = word_set.get_size()
    bucket_list_size = word_set.bucket_list_size()
    max_bucket_size = word_set.max_bucket_size()
    zero_bucket_ratio = word_set.zero_bucket_ratio()

    return (unique_word_count, bucket_list_size,
            max_bucket_size, zero_bucket_ratio)


file_name2 = "swe_news_15102686_words.txt"

unique_word_count, bucket_list_size, max_bucket_size, \
    zero_bucket_ratio = count_unique_words_in_text_file(file_name2)

print(f"\nNumber of unique words in {file_name2}: {unique_word_count}")
print(f"\nBucket List Size for {file_name2}: {bucket_list_size}")
print(f"\nMax Bucket Size for {file_name2}: {max_bucket_size}")
print(f"\nZero Bucket Ratio for {file_name2}: {zero_bucket_ratio:.2f}")
