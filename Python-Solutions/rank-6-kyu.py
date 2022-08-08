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

"""
Kata: Bit Counting
Rank: 6 kyu
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""
def count_bits(n):
    result = 0
    for i in f"{bin(n)}":
        if i == "1":
            result += 1
    return result

"""
Kata: Consecutive strings
Rank: 6 kyu
You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Examples:
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm, "nothing" in Erlang).

Note
consecutive strings : follow one after another without an interruption
"""
def longest_consec(strarr, k):
    combos = []
    for i in range(len(strarr)):
        temp = ""
        for j in strarr[i:i+k]:
            temp += j
        combos.append(temp)
    combos = sorted(combos, key=lambda x: len(x), reverse=True)
    return combos[0] if k > 0 and k <= len(strarr) else ""

"""
Kata: Break camelCase
Rank: 6 kyu
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""
def solution(s):
    if s == s.lower():
        return s
    result = []
    temp = ""
    for i in s:
        if i.islower():
            temp += i
        else:
            result.append(temp)
            temp = i
    return " ".join(result + [temp])

"""
Kata: Replace With Alphabet Position
Rank: 6 kyu
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
"""
def alphabet_position(text):
    return " ".join(f"{int(i, 36) - 9}" for i in text if i.isalpha())

"""
Kata: Sum of Digits / Digital Root
Rank: 6 kyu
Digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. 
If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""
def digital_root(n):
    if n >= 10:
        n = digital_root( sum( [int(i) for i in str(n)] ) )
    return n

"""
Kata: Split Strings
Rank: 6 kyu
Complete the solution so that it splits the string into pairs of two characters. If the string contains an 
odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""
def solution(s):
    if len(s) % 2: s += "_"
    return [s[i-1] + s[i] for i in range(1, len(s), 2)] if s else []

"""
Kata: Detect Pangram
Rank: 6 kyu
A pangram is a sentence that contains every single letter of the alphabet at least once. For 
example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it 
uses the letters A-Z at least once (case is irrelevant). Given a string, detect whether or not 
it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""
def is_pangram(s):
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in s.lower():
            return False
    return True

"""
Kata: Collatz
Rank: 6 kyu
A collatz sequence, starting with a positive integern, is found by repeatedly applying the following function to n until n == 1 :

f(n)={n/2, if n is even3n+1, if n is oddf(n) = \begin{cases} n/2, \text{ if $n$ is even} \\ 3n+1, \text{ if $n$ is odd} \end{cases}f(n)={ 
n/2, if n is even
3n+1, if n is odd

A more detailed description of the collatz conjecture may be found on Wikipedia.

The Problem
Create a function collatz that returns a collatz sequence string starting with the positive integer argument passed into the function, in the following form:

"X0->X1->...->XN"

Where Xi is each iteration of the sequence and N is the length of the sequence.

Sample Input
Input: 4
Output: "4->2->1"

Input: 3
Output: "3->10->5->16->8->4->2->1"
Don't worry about invalid input. Arguments passed into the function are guaranteed to be valid integers >= 1.
"""
def collatz(n):
    result = str(n)
    while n > 1:
        if n % 2 == 0:
            n /= 2
            result += f"->{int(n)}"
        else:
            n = 3 * n + 1
            result += f"->{int(n)}"
    return result

"""
Kata: Persistent Bugger.
Rank: 6 kyu
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
"""
def persistence(n):
    count = 0
    numstr = str(n)
    while len(numstr) > 1:
        temp = 1
        for i in numstr:
            temp *= int(i)
        count += 1
        numstr = str(temp)
    return count

"""
Kata: Twisted Sum
Rank: 6 kyu
Find the sum of the digits of all the numbers from 1 to N (both ends included).

Examples
# N = 4
1 + 2 + 3 + 4 = 10
# N = 10
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46
# N = 12
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51
"""
def compute_sum(n):
    nums = "".join([str(i) for i in range(n+1)])
    return sum([int(i) for i in nums])

"""
Kata: Equal Sides Of An Array
Rank: 6 kyu
You are going to be given an array of integers. Your job is to take that array and find an 
index N where the sum of the integers to the left of N is equal to the sum of the integers 
to the right of N. If there is no index that would make this happen, return -1.

For example:
Let's say you are given the array {1,2,3,4,3,2,1}:
Your function will return the index 3, because at the 3rd position of the array, the sum of 
left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}:
Your function will return the index 1, because at the 1st position of the array, the sum of left 
side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

Last one:
You are given the array {20,10,-80,10,10,15,35}
At index 0 the left side is {}
The right side is {10,-80,10,10,15,35}
They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
Index 0 is the place where the left side and right side are equal.

Note: Please remember that in most programming/scripting languages the index of an array starts at 0.

Input:
An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.

Output:
The lowest index N where the side to the left of N is equal to the side to the right of N. If you 
do not find an index that fits these rules, then you will return -1.

Note:
If you are given an array with multiple answers, return the lowest correct index.
"""
def find_even_index(arr):
    result = -1
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            result = i
            break
    return result
