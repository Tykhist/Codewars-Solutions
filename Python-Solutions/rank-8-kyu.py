"""
Kata: Square(n) Sum
Rank: 8 kyu
Complete the square sum function so that it squares each number passed into it and then sums the results together.
For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
"""
def square_sum(numbers):
    result = [i ** 2 for i in numbers]
    return sum(result)

"""
Kata: Double Char
Rank: 8 kyu
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
Good Luck!
"""
def double_char(s):
    return "".join(i+i for i in s)

"""
Kata: Calculate average
Rank: 8 kyu
Write a function which calculates the average of the numbers in a given list.
Note: Empty arrays should return 0.
"""
def find_average(numbers):
    return sum(numbers) / len(numbers)

"""
Kata: Exclamation marks series #4: Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string
Rank: 8 kyu
Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. 
For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.

Examples
remove("Hi!") === "Hi!"
remove("Hi!!!") === "Hi!"
remove("!Hi") === "Hi!"
remove("!Hi!") === "Hi!"
remove("Hi! Hi!") === "Hi Hi!"
remove("Hi") === "Hi!"
"""
def remove(s):
    return "".join([i for i in s if i != "!"]) + "!"

"""
Kata: Reversed Strings
Rank: 8 kyu
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
"""
def solution(string):
    return "".join([string[i] for i in range(len(string)-1, -1, -1)])

"""
Kata: Function 3 - multiplying two numbers
Rank: 8 kyu
Implement a function which multiplies two numbers.
"""
def multiply(a, b):
    return a * b

"""
Kata: You only need one - Beginner
Rank: 8 kyu
You will be given an array a and a value x. All you need to 
do is check whether the provided array contains the value.
Array can contain numbers or strings. X can be either.
Return true if the array contains the value, false if not.
"""
def check(seq, elem):
    return True if elem in seq else False

"""
Kata: Convert boolean values to strings 'Yes' or 'No'.
Rank: 8 kyu
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""
def bool_to_word(boolean):
    return "Yes" if boolean else "No"
