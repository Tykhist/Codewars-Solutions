"""
Kata: Find the unique number
Rank: 6 kyu
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""
def find_uniq(arr):
    for i in range(len(arr)):
        if arr[i] != arr[i-1] and arr[i] != arr[i-2]:
            return arr[i]

""" 
Kata: Multiples of 3 or 5
Rank: 6 kyu
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
Additionally, if the number is negative, return 0. If the number is a multiple of both 3 and 5, only count it once.
"""
def solution(number):
    if number < 0:
        return 0
    
    multiples = []
    i = 1
    while i < number:
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
        i += 1
        
    total = 0
    for m in multiples:
        total += m
    return total

"""
Kata: Playing with digits
Rank: 6 kyu
Some numbers have funny properties. For example:
89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p,
we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the 
successive powers of p is equal to k * n. In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
If it is the case we will return k, if not return -1.
Note: n and p will always be given as strictly positive integers.
"""
def dig_pow(n, p):
    """
    1. Split n into digits
    2. Give each digit an exponent, starting with p and increasing by 1
    3. Add these new numbers together
    4. Divide by n
    5. Return quotient if it is an integer
    6. Return -1 otherwise
    """ 
    digits = list(str(n))

    exponents = []
    for i in range(len(digits)):
        exponents.append(int(digits[i])**(p+i))

    if sum(exponents) % n == 0:
        return sum(exponents) / n

    return -1

"""
Kata: Mexican Wave (https://en.wikipedia.org/wiki/Wave_(audience))
Rank: 6 kyu
In this simple Kata your task is to create a function that turns a string into a Mexican Wave. 
You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 
Rules:
The input string will always be lower case but maybe empty.
If the character in the string is whitespace then pass over it as if it was an empty seat
"""
def wave(people):
    """
    1. Initialize results list
    2. Iterate through string letters
    3. If letter is blank, skip iteration (continue)
    4. Capitalize each letter, lower the previous one (if applicable),
    and save the word in this state to the results list
    5. Return results
    """
    # Code below is one line, with line breaks for readability
    return [
        "".join(
            [people[:i].lower(), people[i].upper(), people[i+1:].lower()]
        ) \
        for i in range(len(people)) \
        if people[i] != " "
    ]
    
    # Code below was made before refactoring, and is more readable
    """
    results = []
    for i in range(len(people)):
        if people[i] == "" or people[i] == " ":
            continue
        results.append("".join(
            [people[:i].lower(), people[i].upper(), people[i+1:].lower()]
        ))
    return results
    """

"""
Kata: Counting Duplicates
Rank: 6 kyu
Write a function that will return the count of distinct case-insensitive alphabetic characters 
and numeric digits that occur more than once in the input string. The input string can be 
assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
"""
def duplicate_count(text):
    count = 0
    for i in set(text.lower()):
        if text.lower().count(i) > 1:
            count += 1
    return count

"""
Kata: Stop gninnipS My sdroW!
Rank: 6 kyu
Write a function that takes in a string of one or more words, and returns the same string, 
but with all five or more letter words reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
"""
# Note that since the last kata, I realized that a word can be reversed simply by using word[::-1]
def spin_words(sentence):
    result = [letter[::-1] if len(letter) >= 5 else letter for letter in sentence.split()]
#     result = []
#     words = sentence.split()
#     for letter in words:
#         if len(letter) >= 5:
#             result.append(letter[::-1])
#         else:
#             result.append(letter)
    return " ".join(result)

"""
Kata: Unique In Order
Rank: 6 kyu
Implement the function unique_in_order which takes as argument a sequence and returns a list of items
without any elements with the same value next to each other and preserving the original order of elements.

For example:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""
def unique_in_order(iterable):
    if len(iterable) <= 0: return []
    return [iterable[i] for i in range(len(iterable)-1) if iterable[i] != iterable[i+1]] + [iterable[-1] if len(iterable) > 0 else None]

"""
Kata: Sort the odd
Rank: 6 kyu
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""
def sort_array(source_array):
    odd = sorted([i for i in source_array if i % 2 == 1])
    count = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            source_array[i] = odd[count]
            count += 1
    return source_array

