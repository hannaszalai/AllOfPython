File I/O

1. My Place (G)

Create a program called `my_place.py` in which you have two functions as described below. The main part of the program should print out the current absolute path (directly) as well as the number of directories (folder) and files in this directory by calling the two functions. 
```python
def count_directories(dir_path)  # Returns the number of directories

def count_files(dir_path):  # Returns the number of files
```

The output from the program should look similar to below:

```
I am right now at: /home/tanmsi/Filer/SchoolSource/PythonCourse
Below me I have 7 directories/folders
This directory contains 2 files
```

2. Moving around (G)

For this program you are going to create a file called `move_dir.py` that displays a menu of options that the user can select from. In this case the options are to _list_ directories, _change_ directory and _list_ files (as well as exiting the program). Notice that **no error handling** is needed for the task. The options to list and change directories must be separate functions that are called. It is important that these functions _return a list_ of the directories or files and **not** print them out directly in the function. Notice, as in the example below, that you need to be able to move up in the hierarchy as well using "..". Printing should be done in the main part of the program. The signature of those functions are as below:

```python
#  Returns a list of strings with the names of the directories
def list_dir(dir_path)

#  Returns a list of strings with the names of the files
def list_files(dir_path)
```

Running the program can look something like below:

```
1. List directories
2. Change directory
3. List files
4. Quit

==> 1
mini_project
.vscode
ass1
ass3
.git
ass2
temp

1. List directories
2. Change directory
3. List files
4. Quit

==> 2
Name of directory to enter: ass1

1. List directories
2. Change directory
3. List files
4. Quit

==> 3
task4.py
task6.py
task7.py
task10.py
        ### Entries removed for space ###
task8.py
task9.py

1. List directories
2. Change directory
3. List files
4. Quit

==> 2
Name of directory to enter: ..

1. List directories
2. Change directory
3. List files
4. Quit

==> 3
count_lines.py
myran.py

1. List directories
2. Change directory
3. List files
4. Quit

==> 4
```

3. Recursive Print (G)

Create a file called `recursive_print.py` which has a _recursive function_ called `print_sub(dir_path)`. The purpose of the function is to print the name (and this time it is okay to print directly from the function) of the directory and then move into it each of them and print all directories inside it by making recursive calls to the function. Example of output where `mini_project`, `ass1`, `ass2` and `ass3` are top level directories in this directory while for example `figures` and `project_data` belong to `mini_project`:

```
mini_project
figures
project_data
__pycache__
.vscode
ass1
ass3
.git
objects
c1
98
04
74
9c
e7
refs
heads
tags
remotes
origin
logs
refs
heads
remotes
origin
hooks
branches
info
ass2
__pycache__
temp
eric
__pycache__
```

4. Pretty Recursive Print (VG)

As the output from the previous task is quite ugly, create a new file called `pretty_recursive_print.py` where there is a function called `def pretty_print(dir_path, depth)` which makes the output indented based on the depth of directories. The example printout below makes it easier to see that `figure` belongs to the directory `mini_project`:

```
 mini_project
   figures
   project_data
   __pycache__
 .vscode
 ass1
 ass3
 .git
   objects
     c1
     98
     27
     9c
     e7
   refs
     heads
     tags
     remotes
       origin
   logs
     refs
       heads
       remotes
         origin
   hooks
   branches
   info
 ass2
   __pycache__
 temp
   eric
   __pycache__
```

5. Read and Write Text (G)

Write a program `read_write.py` containing two functions `read_file(file_path)` and `write_file(lines, file_path)`.
- The function `read_file(file_path)` should read the text file specified by file_path and return a list of strings containing each line in the file.
- The function `write_file(lines, file_path)` should write (line by line) the content of the list lines to the a file specified by file_path.

When used one after another (first read, then write) the output file should be an exact copy of input file (formatting and all). As an example of a text file you can use the file [mamma_mia.txt](mamma_mia.txt).
```python
# Program starts
path = os.getcwd() + "/jlnmsi_assign3/mamma_mia.txt"

# Read text file
lst = read_file(path)
print(f"Read {len(lst)} lines from file {path}")

# Write text file
path = os.getcwd() + "/jlnmsi_assign3/output.txt"
write_file(lst, path)
print("Text saved in file", path)
```


6. Statistics (G)

For this task you will need two additional text files, found [here](file_10k_integers.zip) in a zip archive. Uncompress it in your working directory or subdirectory before starting with the task. The files contain about 10000 integer values each but are formatted differently. Write a program `read_numbers.py` that reads the two files (one after each other) and for each file computes and presents the _average (mean)_ value and the _standard deviation_. We expect two separate functions `def mean(lst)` and `def std(lst)` that computes the mean and standard deviation for a given list of integers lst. [Here](https://www.mathsisfun.com/data/standard-deviation-formulas.html) you can find more information about the standard deviation.

**Notice:** We expect you to implement the functions _yourselves_ without any use of external libraries. The result when running the program is shown below:

```
Results for file A:
mean = 501.5, standard deviation = 290.1

Results for file B:
mean = 2.4, standard deviation = 289.4
```

7. Life of Brian (G)

As this is course about Python we could not resist using a script from Monty Python in it! In this file you will find the script to [Life of Brian](life_of_brian.txt) from 1979. The task this time is to count the number of words in the script. Create a program called `life_of_brian.py` that has a number of functions for reading and cleaning the script. With this we mean that the main part of the program should only call a function named `def get_words(path, file_name)` that will return a list where each word is an element. There must also be a function that saves the words in a new file with one word on each line. This is important as you will need this file for the next assignment, the project. The short main program should only print out the number of words found as well as what file it saved it to. You can use the program below as a start:

```python
# Main program
path = os.getcwd()
input_file = '/data/life_of_brian.txt'

words = get_words(path, input_file)

output_file = f'/data/brian_{len(words)}_words.txt'

save_words(path, output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)
```

**Important information**
* By a word we here mean strings containing only the English letters plus "'" and "-". Hence, we consider words like "can't", "John's", and "full-time" as valid words. One possible way to deal with this is to omit the ' and say that "can't" and "cant" are the same words. Furthermore, a word doesn't contain any digits, or symbols like ".", ",", "!", "?", etc. 
* Look at slides 41-44 in Lecture 7 to get more details about what we mean by a word.
* We expect you to implement the word counting yourself _without any use of external libraries_. Any use of _regular expressions_ is forbidden.
* We got the count of 13372 words in Life of Brian. We do not expect you to get exactly that, but say around +/- 5% from that.
* Windows users having a problem reading these files can try to use **open(..., encoding='utf-8')** when reading the files.

8. Swedish News (G)

In this task you will do the same as for the previous task, but with a new file: [Swedish News from 2020](swe_news.zip). The file contains one million sentences from Swedish newspapers and you need to create a file with all the words on a separate line, just as for the previous task. Create a copy of your previous program and call it `news_reader.py`  and make the necessary modifications to read this file instead of Life of Brian. The new file is also _much_ larger and it might take a lot of time to find all words -- can you make improvements to your code? Highlight all changes you do, if any, to make it work with the new file. We get about 15 million words and it takes, on a reasonably fast computer, somewhere between 15 seconds to one minute to run the program. It will take even longer on a slower machine, so it is a good idea to try out with a subset of the news file to begin with. As a recommendation, the execution of the program should not take more than a few minutes so if your program takes longer than that, have a good look at your code to see where it might be improved.

9. Lines of Python (VG)

It has been a lot of programming in this course. But how many lines of Python code have you actually written?
Write a program `count_lines.py` containing a function `def count_py_lines(dir_path)` returning a count (an integer) of all the non-empty lines in all Python files (ending with .py) in the directory specified by dir_path and all its subdirectories (transitively).

### Lecture 8 - Tuples, sets, and dictionaries

10. Different Values (G)

The **set** is a good way to find out how many _different_ values there are in a sequential data structure. Create a program called `different.py` that has a function called `def different(lst)` that returns a sorted list of the unique elements in the list that is sent to it. This should be done by using a set to find out the unique elements. In the main part of the program you should create a list of 100 random values ranging from 1 to 200 and show that the function works. Below you can see an example execution:

```
Different integers:
[3, 11, 13, 19, 22, 23, 26, 31, 34, 35, 40, 42, 46, 47, 48, 49, 51, 56, 57, 60, 62, 65, 66, 67, 68, 70, 79, 80, 81, 83, 85, 86, 88, 92, 97, 100, 102, 104, 105, 106, 113, 115, 118, 119, 122, 126, 127, 128, 133, 136, 137, 141, 144, 146, 149, 150, 151, 152, 153, 156, 158, 162, 164, 171, 173, 175, 181, 182, 183, 184, 189, 194, 195, 196, 197, 198, 199]
```

11. Counting Occurrences (G)

Create a program called `occurrences.py` in which you have a function `def count_occurrences(lst)` that returns a _sorted dictionary_ of the number of occurrences of integers in the list sent to the function. The main part of the program should create a list of 100 random integers ranging from 1 to 10. This list should be sent to the function and the resulting dictionary should be printed out from 1 to 10 with the number of occurrences of each integer. An example execution is shown below:

```
1       10
2       11
3       7
4       16
5       10
6       8
7       7
8       9
9       13
10      9
```

12. Letter count (VG)

In this exercise we will once again use the text file `life_of_brian.txt` that we used in Exercise 7. Knowing the character frequencies for a language has many important applications in cryptoanalysis.

Write a program letter_count.py that:
- Reads the text file `life_of_brian.txt`. Feel free to use the output from Exercise 7 if you like to.
- Use a dictionary to count the number of times each letter (a-z, upper case letters are counted as lower case letters) is occurring in the files. Notice: Upper case letter are turned into lower case letters and you only need to count occurrences of the English letters abcdefghijklmnopqrstuvwxyz. Letters with accents and non-English letters can be ignored.
- Displays a simple histogram (see example below)

```
Reading text from the file: .../life_of_brian.txt
Total number of letters: ...

Histogram (where each star represents XXX occurrences of the given letters)
a | ******
b | ****
c | **
d | ***
e | *******
f | ****
h | *** 
...
z | *     
```
**Notice**: The above histogram is just fake showing what type of histogram we are looking for. It is not the result of a frequency analysis of the text in `life_of_brian.txt``. Also, play around with different values of XXX to produce nice looking histograms.

**Hint**: Start working with much smaller text files allowing you to manually inspect the result!


### Lecture 9 - Data classes and Data Structures

13. Class Name (G)

Create a data class `Name.py` representing a name with a first name and a last name that when executed using this code (in `Name_Main.py`):
```python
# Using data class Name
import Name as nm

# Creat and initialize a Name object
me = nm.Name("Jonas", "Lundberg")
print(me.to_string())
print(me.get_first())
print(me.get_last())

# Creat an empty Name object
you = nm.Name()
you.set_first("Arnold")
you.set_last("Palmer")
print(you.get_short_name())
```
results in the following console print-out:
```
Jonas Lundberg
Jonas
Lundberg
A. Palm
```
14. Multidisplay (G)

Create a data class `MultiDisplay.py` that when executed using this code (in `Multi_Main.py`):

```python
import MultiDisplay as multi

# Program starts
md = multi.MultiDisplay()

md.set_message("Hello World!")
md.set_count(3)
print(md.to_string())                  # print-out
md.display()                           # print-out

md.set_display("Goodbye cruel world!", 2)    # print-out
print(md.to_string())                        # print-out
print("Current message:", md.get_message())  # print_out
```
results in the following console print-out:
```
Message: Hello World!, Count: 3
Hello World!
Hello World!
Hello World!
Goodbye cruel world!
Goodbye cruel world!
Message: Goodbye cruel world!, Count: 2
Current message: Goodbye cruel world!
```
The class MultiDisplay should of course be able to handle other messages and other numbers of display counts.

15. Deque Data Structure (G)

In this exercise you should implement a deque data structure using a linked head-and-tail approach. See Lecture 9 for information about deques and linked implementations.

The file [deque_skeleton.zip](deque_skeleton.zip) contains three files:

* A data class Deque.py containing the skeleton of a deque implementation. It provides a complete Node data class implementation and a non-complete Deque data class implementation. Your task is to turn the non-complete Deque class into a proper deque data structure by implementing the missing methods.
* A program deque_main.py that demonstrates how to use the Deque class.
* A text file output.txt that shows the expected output from deque_main.py for a correct complete implementation of the Deque class.

Your task is to complete the class Deque by providing code for the missing methods. We strongly suggest that you implement the methods one at the time, starting from the top with method add_last(self,n) followed by to_string(self). Use the demo program deque_main.py to verify that the implemented methods works correctly.
