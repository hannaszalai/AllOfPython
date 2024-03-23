# Mini-project report 
Members: Vilma Garrido and Hanna Szalai  
Program: Software Technology  
Course: 1DV501 
Date of submission: 2023-12-03

## Introduction  
This mini-project, a part of our Software Technology course (1DV501). It involved tackling tasks like counting unique words and figuring out the top 10 most frequently used words in two text files. The most difficult task was making a HashSet and a Binary Search Trees (BST), two key data structures in the world of computer science. We used two fairly large text files from Assignment 3 as our input data. This report provides an overview of the journey we undertook, highlighting the challenges we encountered and the invaluable knowledge we acquired throughout the process. 

## Part 1: Count unique words 1
- The 2 large text files from Assignment 3:  
``life_of_brian`` had 13.374 words and ``swedish_news_2020`` had 15.102.686 words.
Henceforth we worked with the corresponding files from now on ``brian_13374_words.txt`` and ``swe_news_15102686_words.txt``.
- To identify the top 10 most frequently used words with a length greater than 4 characters in each text file, we wrote the code as seen below.

```
# Top 10 list most frequently used words having a length larger than 4
word_counts = {}  # empty dictionary
for word in words:
    if len(word) > 4:
        if word in word_counts:
            word_counts[word] += 1
        else:
			# the words has been seen once so far
            word_counts[word] = 1
# sort the dictionary by count where x is a tuple (word, count)
sorted_word_counts = sorted(word_counts.items(),
                            key=lambda x: x[1], reverse=True)
top_10_words = sorted_word_counts[:10]
```

- We used a dictionary to count the occurrences of each word and then sorts the dictionary by count to get the top 10 words. To store word frequencies, we created an empty dictionary called word_counts and iterated through the list of words, and if a word had a length greater than 4 characters, we updated its count. After processing the words, we sort the dictionary by the count in descending order. It will give us the ouput with the words and their counts. Finally, we retrieved the first 10 words.

- Output for ``brian_13374_words.txt``:
   - Number of unique words in brian_13374_words.txt: 2057  
   - Top 10 most frequently used words in brian_13374_words.txt:  
("brian", 368), ("crowd", 161), ("centurion", 121), ("mother", 104), ("right", 99), ("crucifixion", 78), ("pilate", 68), ("pontius", 64), ("don't", 59), ("rogers", 52)

- Output for ``swe_news_15102686_words.txt``:
   - Number of unique words in swe_news_15102686_words.txt: 408001
   - Top 10 most frequently used words in swe_news_15102686_words.txt:  
("under", 54037), ("säger", 47542), ("efter", 44089), ("kommer", 42851), ("eller", 32077), ("också", 30477), ("sedan", 30396), ("andra", 28054), ("finns", 27583), ("många", 26818)


## Part 2: Implementing data structures
The task involves implementing two fundamental data structures: a binary search tree (BST) based map (dictionary) and a hash-based set suitable for storing words. The implementations should adhere to the provided code skeletons and should work seamlessly with the example given. The BST-based map enables efficient key-value pair management, while the hash-based set is designed for word storage and retrieval. These data structures are foundational in computer science and have various practical applications.

#### For the HashSet 

- The add method in the hash-based set first calculates the hash key for the given word using the get_hash function, then selects the corresponding bucket. It checks if the word is not already in the bucket and, if not, appends the word to the bucket and increments the size of the set. If the current number of elements equals the number of buckets (indicating that the load factor has reached its limit), it triggers rehashing to double the size of the bucket list, ensuring efficient storage and retrieval of words in the set.
```
def add(self, word):
        key = self.get_hash(word)  # get the hash key for the word
        bucket = self.buckets[key]  # select the bucket
        # check if the word is not already in the bucket
        if word not in bucket:
            bucket.append(word)
            self.size += 1
        if self.size == len(self.buckets):  # check if rehashing is needed
            self.rehash()
```
- The get_hash method computes a hash value for a given word by initializing hash_value to 0 and then iterating through each character in the word. It accumulates the ASCII values of each character by using the ord(char) function and adds them to hash_value. To ensure that the hash value falls within the range of available buckets, it calculates the remainder of hash_value when divided by the number of buckets (len(self.buckets)) using the modulus operator. This approach leverages character ASCII values to create a relatively uniform distribution of words across the buckets in the hash-based set. 
```
def get_hash(self, word):
        hash_value = 0  # start with th value 0
        for char in word:
            # add the ASCII value of every character
            hash_value += ord(char)
        # get the remainder of the hash value divided by the number of buckets
        hash_value = hash_value % len(self.buckets)
        return hash_value
    # we are using the ord() function to
    # get the ASCII values and summing them up
```
- The rehash method is responsible for increasing the capacity of the hash-based set when the number of elements equals the number of buckets. It first creates a copy of the existing buckets, clears the original buckets, and resets the size to zero. Then, it creates new buckets with double the size of the old ones. Next, it iterates through the copy of the buckets, and for each word within each bucket, it uses the add method to insert the word into the newly enlarged bucket list, effectively redistributing the elements across the larger set of buckets to maintain a suitable load factor.
```
def rehash(self):
        buckets_copy = self.buckets.copy()  # make a copy of the buckets
        self.buckets.clear()  # clear the buckets
        self.size = 0  # reset the size
        # Create new buckets with double the size of the old buckets
        self.buckets = [[] for i in range(len(buckets_copy) * 2)]
        for bucket in buckets_copy:  # iterate through the buckets
            for word in bucket:  # iterate through the nodes in the bucket
                self.add(word)  # add the node to the new buckets
        # For each element in the copy:
        # add it to enlarged bucket list using the add function
```
- The variations observed in the results between our implementation in hash_main.py and the provided ones were minimal, with the sole difference being a zero bucket ratio of 0.38 compared to the expected 0.5. Upon discussing this difference with our teacher during a lab session, we gained clarity that this difference was not important. In fact, it indicated a more refined Hashset, as the lower zero bucket ratio implied fewer empty buckets, underscoring the efficiency of our implementation. This insight from our teacher provided validation for the effectiveness of our work.

#### For the Binary Search Tree 

- The put function is in charge of inserting a key-value pair into the map. As we know, left nodes are smaller and right nodes are larger. First, checked if the given key is less than the key of the current node. If it is, move to the left child of the current node. If there is no left child, create one and call the put() function again. The same goes for the right ones. If the map is empty (it doesn't have a root node), it creates a new one with the given key and value. And if the value already exists it means we met a duplicate, then update it's value to not have one.

```
	def put(self, key, value):
        if key < self.key:
            # If there is no left child, create a new node
            if self.left is None:
                self.left = Node(key, value)
            else:
        # If there is, move to the left child and def put() again
                self.left.put(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.put(key, value)
        else:
        # Update value if it already exists to not have duplicates
            self.value = value
```

- The max_depth function returns the maximum depth of the tree, the longest root-to-leaf path. This is done by traversing the tree again and again, calculating the depth of the left and right subtrees, and returning the maximum of these depths +1 which is the root node. And of course if we don't have a left or a right node it will return 0.

```
    def max_depth(self):
        if self is None:
            return 0

        # Depth of the left subtree
        if self.left is None:
            left_depth = 0
        else:
            left_depth = self.left.max_depth()

        # Depth of the right subtree
        if self.right is None:
            right_depth = 0
        else:
            right_depth = self.right.max_depth()

        return 1 + max(left_depth, right_depth)
```

- We wanted our code to look the same as the given output so there isn't much of a difference from the ``bst_main.py``.


## Part 3: Count unique words 2
- For each word we checked to see if it already exists in the BST map, if we found it with the get() function, we increased the count by 1. If we didn't find it, we added it with a count of 1 to the tree. Then, using the as_list() function, sorted the key-value pairs by their values (counts, [1]). Then, just like in the first part, we iterated through the sorted list, and selected the first 10 to find the words. According to the instructions, we got the same results as in part 1 which is:  
Top 10 most frequently used words in brian_13374_words.txt:  
("brian", 368), ("crowd", 161), ("centurion", 121), ("mother", 104), ("right", 99), ("crucifixion", 78), ("pilate", 68), ("pontius", 64), ("don't", 59), ("rogers", 52)

```
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
```
- Output for ``BstMain.py``:
  - Top 10 most frequently used words in brian_13374_words.txt:  
("brian", 368), ("crowd", 161), ("centurion", 121), ("mother", 104), ("right", 99), ("crucifixion", 78), ("pilate", 68), ("pontius", 64), ("don't", 59), ("rogers", 52)
  - Number of tree nodes: 1453
  - Max depth of the BST: 24
  - Internal node count: 980
  - Top 10 most frequently used words in swe_news_15102686_words.txt:  
("under", 54037), ("säger", 47542), ("efter", 44089), ("kommer", 42851), ("eller", 32077), ("också", 30477), ("sedan", 30396), ("andra", 28054), ("finns", 27583), ("många", 26818)
  - Number of tree nodes: 393673
  - Max depth of the BST: 115
  - Internal node count: 263719

#### Max depth and internal node count
  Max depth and internal node count can be used to evaluate the efficiency of the BstMap. As we know a balanced BST is one of the most efficient data structure to search and retreive data, that's why we should check with these 2 functions if the tree is a balanced tree or not.   
  The max depth can be used to measure how tall a tree is. If it's too big it's not efficient, if it's a little big but not that much it's reasonable. But the optiomal tree isn't too short nor too tall, just perfect. It's usually half the number of the brances.  
  Internal Node Count is about how many nodes on the tree have other nodes attached to them or in other words, how many of them have 1 or 2 children. They can also show whether a tree is balanced or not. In an optimal tree, the internal node count is low compared to the total number of elements. For a balanced BST, the number of internal nodes typically half the number of elements. In a reasonable tree, the internal node count could be between half the number of elements and the number of all elements. And the tree is poor if the count is close to the number of all elements.

#### Max bucket size and zero bucket ratio in HashSet
Max Bucket Size and Zero Bucket Ratio serve as important indicators when evaluating the performance and quality of a hash function within a HashSet data structure. These metrics provide valuable insights into how well the hash function distributes elements across buckets and whether it efficiently utilizes available resources.
In an ideal scenario, an optimal hash function results in a well-balanced distribution of elements across buckets, ensuring that no individual bucket contains significantly more elements than others. This balance is reflected in a low max bucket size. Additionally, there should be a minimal number of empty buckets, indicating an efficient utilization of memory. This results in a low zero bucket ratio.
Reasonable values for these metrics allow for some variation. While there may be moderate differences in bucket sizes and a reasonable number of empty buckets, the overall distribution remains balanced. The performance is not significantly affected in this case.

Max Bucket Size:
- Definition: Max bucket size is the maximum number of elements stored in any individual bucket within the set.
Evaluation:
- Optimal: An optimal value for max bucket size would be relatively balanced, where no single bucket contains significantly more elements than others. This indicates an even distribution of elements and efficient bucket usage.
- Reasonable: A reasonable value allows for some variation in bucket sizes but still maintains a generally balanced distribution of elements. It should not lead to performance degradation.
- Poor: A poor value for max bucket size would be when a single bucket becomes excessively large compared to others. This can lead to inefficient searches and slower retrieval times, indicating a suboptimal hash function.

Zero Bucket Ratio:
- Definition: The zero bucket ratio is the proportion of empty buckets (buckets with zero elements) in the HashSet.
Evaluation:
- Optimal: An optimal value for the zero bucket ratio is low, indicating that most buckets are utilized, and there are few empty buckets. This suggests that the hash function is effectively distributing elements across the buckets.
- Reasonable: A reasonable value allows for a moderate number of empty buckets, but it should not dominate the overall bucket distribution. Some degree of unused buckets is acceptable in a reasonably efficient hash function.
- Poor: A poor value for the zero bucket ratio would be a high proportion of empty buckets. This indicates that the hash function is not distributing elements effectively, and many buckets remain unused, which can lead to wasted memory and inefficient searches.

## Project conclusions and lessons learned
I would lie if I said it went smoothly. Making our own hash-based set and binary search tree was challenging. But it was a great learning experience for the both of us.
The process of developing our own hash-based set and binary search tree was undoubtedly challenging, but it offered valuable learning experiences. It required a deep understanding of hashing, tree structures, and algorithmic efficiency. We learned how to optimize code, troubleshoot complex issues, and translate theoretical knowledge into practical solutions. This project not only improved our programming skills but also underscored the significance of data structure design in real-world applications.

### Technical issues 
- The major technical challange was definitely GitLab! As adding, commenting, pushing weren't enough we also needed to learn how to work with brances. In my opinion, if they would've been named 'workspaces' instead of 'brances' we wouldn't have to ask for help that much. But as scary as it first looked it wasn't that bad actually and when we learn new things the older ones become easier. 
- The most time consuming part was actually understanding what we should do, how to even start with the project or watch the counless youtube videos sitting in our Watch Later library. 
- We don't think we would do anything differently, we read the instructions, understood, made a plan, devided the exercises then started to work until we were done. We didn't jump right into we understood it first I think that't the most important part. 
- If we were given a bit more time to complete the task I think we would find more ways to shorten the code and make it more efficient.

### Project issues
- Our team organized the work through communication. We assigned tasks, tracked progress on Gitlab, and set deadlines for each part. We met every 2 days, where we discussed progress, challenges, shared ideas and of course merged our work. We always made sure to attend the lab sessions too.

  - From Hanna's side: I was responsible for the first part which consisted of counting the amount of unique words within the provided text files and to produce a top 10 list of the ten most frequently used words. I was also in charge of implementing the binary search tree. I spent an average 35 hours a week researching, writing the code and actually making it work. I finished with it first then me and my partner had to brainstorm to make the hashing work. Overall this assignment was an excellent learning opportunity. I learned about solving complex technological challenges and the value of successful teamwork. It definitely aided my personal and professional development. I'm proud of both of us for how we overcame obstacles and what we accomplished as a team.

  - From Vilma's side: I was assigned several responsibilities throughout the project, including developing the initial part for the unique word counter and creating the Hashset, as well as working on the third part, integrating Hash_main with our text files. During our class sessions, I initially faced challenges in comprehending the functioning of the Hashset and how to effectively implement it. To address this, I turned to external resources such as YouTube videos and attended lab sessions, which significantly contributed to my understanding of the concept and its practical implementation. I realized that the concept was not as complex as I initially perceived. However, it's worth noting that the task consumed around 21 hours per week, as I prefer working in shorter, focused intervals due to my susceptibility to distractions. The experience undoubtedly improved my coding skills, arguably more so than any previous assignments. In hindsight, I would have chosen to be more attentive during class to reduce the need for independent research and look for more assistance through additional lab sessions, which ultimately proved immensely helpful.
