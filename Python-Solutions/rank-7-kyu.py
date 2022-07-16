"""
Kata: Isograms
Rank: 7 kyu
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.
"""
def is_isogram(string):
    letters = []   # holds letters to check for duplicates
    for s in string.lower():   # checks every letter in lowercase to make them uniform
        if s not in letters:   # compares letters with duplicate list
            letters.append(s)   # adds safe letters to be checked in list
        else:
            return False   # immediately ends the progam for any duplicate
    return True

"""
Kata: Complementary DNA
Rank: 7 kyu
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the 
development and functioning of living organisms. If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
Your function receives one side of the DNA; you need to return the other complementary side. 
DNA strand is never empty or there is no DNA at all.
"""
def DNA_strand(dna):
    result = ""   # initializes a string to return
    for i in dna.upper():   # ensures that all letters are uniform
        if i == "A": result += "T"   # builds the return string
        elif i == "C": result += "G"
        elif i == "T": result += "A"
        elif i == "G": result += "C"
    return result

"""
Kata: List Filtering
Rank: 7 kyu
In this kata you will create a function that takes a list of non-negative integers 
and strings and returns a new list with the strings filtered out.
"""
def filter_list(l):
    return [x for x in l if type(x) == type(int())]

"""
Kata: Vowel Count
Rank: 7 kyu
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(sentence):
    count = 0
    for i in sentence:
        if i in ["a", "e", "i", "o", "u"]:
            count += 1
    return count

"""
Kata: Get the Middle Character
Rank: 7 kyu
You are going to be given a word. Your job is to return the middle character of the word. 
If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
"""
def get_middle(s):
    half = len(s) // 2
#     if len(s) % 2 == 0:
#         return f"{s[halfish - 1]}{s[halfish]}"
#     else:
#         return s[halfish]
    return (s[half-1] + s[half]) if len(s)%2 == 0 else s[half]

"""
Kata: Reverse words
Rank: 7 kyu
Complete the function that accepts a string parameter, and reverses 
each word in the string. All spaces in the string should be retained.
"""
def reverse_words(text):
    result = []
    
    """
    Replaces the spaces from input with placeholders (~), 
    and splits entire string into a list
    """
    no_space = "".join([" ~ " if i == " " else i for i in text]).split()

    for word in no_space:
        """
        Splits every word into a list of letters, reverses 
        the letters, and joins the list back into a string
        """
        reverse = "".join(reversed([i for i in word]))
        
        """
        Adds either the newly reversed word to the result,
        or a space if the word is a placeholder (~)
        """
        result.append(reverse) if word != "~" else result.append(" ")
        
    """ Joins list of reversed words into one string """
    return "".join(result)

"""
Kata: Friend or Foe?
Rank: 7 kyu
Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
"""
def friend(x):
    return [i for i in x if len(i) == 4]

"""
Kata: Printer Errors
Rank: 7 kyu
In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, 
for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string. For example a "good" control string would 
be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced 
e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

You have to write a function printer_error which given a string will return the error rate of the printer as 
a string representing a rational whose numerator is the number of errors and the denominator the length of 
the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from ato z.

Examples:
s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"
"""
def printer_error(s):
    good_letters = "abcdefghijklm"
    count = 0
    for letter in s:
        if letter not in good_letters:
            count += 1 
    return f"{count}/{len(s)}"

"""
Kata: Two to One
Rank: 7 kyu
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the 
longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""
def longest(a1, a2):
    return ''.join(sorted(set(a1+a2)))

"""
Kata: Disemvowel Trolls
Rank: 7 kyu
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.
"""
def disemvowel(string_):
    string_ = [letter for letter in string_ if letter not in "aeiouAEIOU"]
    return ''.join(string_)

"""
Kata: Shortest Word
Rank: 7 kyu
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
"""
def find_short(s):
    s = s.split()
    l = s[0]
    for i in s:
        if len(i) < len(l):
            l = i
    return len(l) # l: shortest word length

"""
Kata: Mumbling
Rank: 7 kyu
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
"""
def accum(s):
    count = 0
    result = []
    for i in s.lower():
        result.append(i.upper() + i * count)
        count += 1
    return '-'.join(result)

"""
Kata: Sum of two lowest positive integers
Rank: 7 kyu
Create a function that returns the sum of the two lowest positive numbers given an array 
of minimum 4 positive integers. No floats or non-positive integers will be passed.
For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""
def sum_two_smallest_numbers(numbers):
    result = sorted([i for i in numbers if i >= 0])
    return result[0] + result[1]

"""
Kata: Odd or Even?
Rank: 7 kyu
Given a list of integers, determine whether the sum of its elements is odd or even.
Give your answer as a string matching "odd" or "even".
If the input array is empty consider it as: [0] (array with a zero).

Examples:
Input: [0]
Output: "even"
Input: [0, 1, 4]
Output: "odd"
Input: [0, -1, -5]
Output: "even"

Have fun!
"""
def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"

"""
Kata: Exes and Ohs
Rank: 7 kyu
Check to see if a string has the same amount of 'x's and 'o's. The method must 
return a boolean and be case insensitive. The string can contain any char.

Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""
def xo(s):
    o_count = 0
    x_count = 0
    
    for i in s.lower():
        if i == 'o': o_count += 1
        elif i == 'x': x_count += 1
        
    return True if o_count == x_count else False

"""
Kata: Remove the minimum
Rank: 7 kyu
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, 
remove the one with a lower index. If you get an empty array/list, return an empty array/list. Don't change the order of the elements that are left.

Examples
* Input: [1,2,3,4,5], output= [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]
"""
def remove_smallest(numbers):
    result = numbers[:]
    low = result[0] if len(result) > 0 else result
    for i in result:
        if i < low:
            low = i
    if len(result) > 0:
        result.remove(low)
    return result

"""
Kata: Beginner Series #3 Sum of Numbers
Rank: 7 kyu
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
"""
def get_sum(a,b):
    c = sorted([a, b])
    result = 0
    for i in range(c[0], c[1]+1):
        result += i
    return a if a == b else result

"""
Kata: Sum of the first nth term of Series
Rank: 7 kyu
Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

Rules:
You need to round the answer to 2 decimal places and return it as String.
If the given value is 0 then it should return 0.00
You will only be given Natural Numbers as arguments.

Examples:(Input --> Output)
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
"""
def series_sum(n):
    series = [(1/(1+i*3)) for i in range(n)]
    return f"{sum(series):.2f}"

"""
Kata: Binary Addition
Rank: 7 kyu
Implement a function that adds two numbers together and returns their sum in binary. 
The conversion can be done before, or after the addition.
The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))
1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
"""
def add_binary(a,b):
    return f"{bin(a+b)}"[2:]

"""
Kata: Ones and Zeros
Rank: 7 kyu
Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:
Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11

However, the arrays can have varying lengths, not just limited to 4.
"""
def binary_array_to_number(arr):
    return int('0b' + ''.join([str(i) for i in arr]), 2)



