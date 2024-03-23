from dataclasses import dataclass
from typing import List


# Define the main HashSet class (structure)
@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def __init__(self):
        # Initiallize the size, number of elements in the set
        # to make them empty
        self.size = 0
        self.buckets = [[] for i in range(8)]  # Initial bucket size of 8

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        hash_value = 0  # start with the value 0
        for char in word:  # Iterates through each character in the input word
            # ord() gives each character a an ASCII value
            # sums the ASCII values of all characters in the word
            hash_value += ord(char)
        # get the remainder of the hash value divided by the number of buckets
        hash_value = hash_value % len(self.buckets)
        return hash_value

    # Resize the buckets when it becomes full
    def rehash(self):
        # copy and clear to preserve the data before the rehashing
        buckets_copy = self.buckets.copy()  # make a copy of the buckets
        self.buckets.clear()  # clear the buckets
        self.size = 0  # reset the size
        # Create new buckets with double the size of the old buckets
        # 2 because it's more efficient
        self.buckets = [[] for i in range(len(buckets_copy) * 2)]
        for bucket in buckets_copy:  # iterate through the buckets
            # For each element in the copy:
            # add it to enlarged bucket list using the add function
            for word in bucket:  # iterate through the words in the bucket
                self.add(word)  # add the node to the new buckets

    # Adds a word to hashset if not already added
    def add(self, word):
        key = self.get_hash(word)  # get the hash key (from ASCII) for the word
        bucket = self.buckets[key]  # select the bucket where the word goes
        if word not in bucket:  # if it's not in the bucket
            bucket.append(word)
            self.size += 1
        # if number of elements in hashset = number of current buckets,
        # (set is full), rehash
        if self.size == len(self.buckets):  # check if rehashing is needed
            self.rehash()

    # Returns a string representation of the set content (human-readable)
    # convert elements in buckets into list then into string
    def to_string(self):
        words = []  # initialize a list to store the words
        # nested loop to iterate through the buckets
        for bucket in self.buckets:
            for word in bucket:
                words.append(word)
        words_as_string = str(words)
        return words_as_string

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        key = self.get_hash(word)  # get the hash key (from ASCII) for the word
        bucket = self.buckets[key]  # select the bucket where the word goes
        if word in bucket:
            return True
        return False

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        key = self.get_hash(word)  # get the hash key (from ASCII) for the word
        # Select the specific bucket where the word should be found
        bucket = self.buckets[key % len(self.buckets)]

        # Initialize a variable to keep track of the word to remove
        to_remove = None
        for node in bucket:  # iterate through the nodes in the bucket
            # check if the node is the one needs to be removed
            if node == word:
                to_remove = node  # set the node to remove
                break  # exit the loop

        # If the word was found, remove the node then -1
        if to_remove is not None:
            bucket.remove(to_remove)  # remove the node from the bucket
            self.size -= 1  # decrease the size of the hashset

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        # keep track of the maximum bucket size
        max_size = 0
        # Iterate through the buckets in the hash set
        for bucket in self.buckets:
            # Calculate the size (number of elements) of the current bucket
            current_bucket_size = len(bucket)
            # check if the size of the current bucket
            # is greater than the current maximum
            if current_bucket_size > max_size:
                # Update the maximum bucket size if a larger bucket is found
                max_size = current_bucket_size
        return max_size

    # Returns the ratio of buckets of lenght 0
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        # count the number of empty buckets
        empty_buckets = 0  # keep track of empty buckets
        for bucket in self.buckets:
            if not bucket:  # if it's empty add 1
                empty_buckets += 1
        total_buckets = len(self.buckets)  # total number of buckets
        return empty_buckets / total_buckets  # return the ratio

    # Returns a list with all words in the set
    def as_list(self):
        lst = []  # to store the words
        for bucket in self.buckets:
            # appends the elements of one list to another list
            # (from bucket to lst)
            lst.extend(bucket)
        return lst
