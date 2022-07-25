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
