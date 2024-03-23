import random
import math

# 1
n = 0

for i in range(1, 101):
    if i % 2 == 0:
        n += i

print("Sum of the 100 first even numbers is:", n)

# 2
n = int(input("Enter a positive integer: "))

print("\n" + "Odd numbers using for:", end=" ")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
print()

print("Odd numbers using while:", end=" ")
i = 1
while i <= n:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
print()

# 3
n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please provide a positive integer.")
else:
    i = 1
    while i > 0:
        if i % 2 != 0 and sum(range(1, i + 1, 2)) > n:
            print(f"\n{i} is the smallest k such that 1+3+5+...+k > {n}")
            break
        i += 1

    i = 0
    while i <= n:
        if i % 2 == 0 and sum(range(0, i + 1, 2)) >= n:
            i -= 2
            break
        i += 2
    print(i, "is the largest k such that 0+2+4+6+...+k <", n)

# 4
number = random.randint(1, 100)
max_guesses = 10
guess = 0
guesses = 0

while guesses < max_guesses:
    guess = int(input(f"Guess {guesses + 1}: "))
    if guess > number:
        print("Clue: lower")
    elif guess < number:
        print("Guess: higher")
    else:
        print("Correct!")
        break

    guesses += 1

if guesses == max_guesses:
    print("You've reached the maximum of guesses.")


# 5

primes_n = []
for num in range(2, 21):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes_n.append(num)

print(primes_n)


def hi(lst):
    first = lst[0]

    for i in range(len(lst) - 1):
        lst[i] = lst[i + 1]

    lst[-1] = first
    return lst


lst = [1, 2, 3, 4]
print(hi(lst))

# 6
n = int(input("Enter number of integers to be generated: "))

if n <= 0:
    print("n must be a positive integer !")
else:
    total = 0
    smallest = 100
    largest = 1
    print("\nGenerated values:", end=" ")
    for i in range(n):
        num = random.randint(1, 100)
        total += num
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
        print(num, end=" ")
    average = total / n
    print(f"\nAverage, min, and max are {average:.2f}, " +
          f"{smallest} and {largest}")

# 7
n = int(input("Enter an odd positive integer: "))

print("\nRight-Angled Triangle: ")
for i in range(n):
    for j in range(i + 1):
        print(" ", end="")
    for j in range(i, n):
        print("*", end="")
    print()

print("\nIsosceles Triangle:")
for i in range(1, n + 1, 2):
    for j in range((n - i) // 2):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# 8
n = int(input("Enter a large positive integer: "))

zeros = 0
odd = 0
even = 0

if n < 0:
    print("Please provide a positive integer")
else:
    while n > 0:
        digit = n % 10
        if digit == 0:
            zeros += 1
        elif digit % 2 == 0:
            even += 1
        else:
            odd += 1
        n //= 10

    print(f"\nZeros: {zeros}")
    print(f"Odd: {odd}")
    print(f"Even: {even}")


# 9
total_boxes = 0
remaining_candles = 0

for age in range(1, 101):
    if remaining_candles < age:
        # Calculate boxes needed using ceiling division
        boxes_needed = -(-max(0, age - remaining_candles) // 24)
        # Add boxes needed to total boxes
        total_boxes += boxes_needed
        # Add new candles to remaining candles
        remaining_candles += boxes_needed * 24
        # Print the number of boxes bought this year
        print(f"Before birthday {age}, buy {boxes_needed} box(es)")
    # Subtract the age (candles used) from remaining candles
    remaining_candles -= age

print(f"\nTotal number of boxes: {total_boxes}", end=", ")
print(f"Remaining candles: {remaining_candles}")


# 10

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

dist = distance(x1, y1, x2, y2)  # itt adjuk meg az adatokat

print(f"\nThe distance between ({x1}, {y1}) and ({x2}, {y2})"
      f" is {dist:.3f}")


# 11
def inc(n):
    return n + 1


def inc_with(n, t):
    return n + t


def greatest(n1, n2):
    return max(n1, n2)


def is_even(n):
    if n < 0:
        return False
    else:
        if n % 2 == 0:
            return True
        return False


def power(x, n):
    return x**n


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
            return True


print("41 plus 1:", inc(41))
print("30 plus 12:", inc_with(30, 12))
print("Which is greater, 24 or 42?", greatest(24, 42))
print("Is 42 even?:", is_even(42))
print("2 to the power of 10:", power(2, 10))
print("Factorial of 5:", factorial(5))
print("Is 41 a prime?:", is_prime(41))


# 12

print("Enter positive integers. End by giving a negative integer.")


def count_positive(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count


ints = []

for i in range(1, 6):
    user_input = int(input(f"Integer {i}: "))
    if user_input < 0:
        break
    ints.append(user_input)

positive_count = count_positive(ints)

print(f"\nNumber of positive integers: {positive_count}")
print("Positive numbers:", ints)

# 13
counts = [0] * 11

for i in range(10000):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    total = roll1 + roll2
    counts[total - 2] += 1

print("Frequency table (sum,count) for rolling two dices 10000 times")
for i in range(2, 13):
    print(f"{i} \t {counts[i-2]}")


# 14
lst = []

for i in range(7):
    lst.append(random.randint(1, 36))

lst.sort()

print("The Lotto numbers this week:")
for num in lst:
    print(num, end=" ")

# 15


def is_palindrome(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    return s == s[::-1]


print(is_palindrome("Was it a rat I saw?"))
print(is_palindrome("A nut for a jar of tuna."))
print(is_palindrome("Madam"))
print(is_palindrome("Ni talar bra latin!"))
print(is_palindrome("12321"))
print(is_palindrome("Palindrome"))

# filter = removes all non-letter characters
# lower = converts the input string to lowercase
# join =  concatenates the letters in the iterable into a single string,
# with no separator between the letters
