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

"""
Kata: Categorize New Member
Rank: 7 kyu
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help 
with an application form that will tell prospective members which category they will be placed.
To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet 
club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input:
Input will consist of a list of pairs. Each pair contains information for a single potential member. 
Information consists of an integer for the person's age and an integer for the person's handicap.

Output:
Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the 
respective member is to be placed in the senior or open category.

Example
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
"""
def open_or_senior(data):
    output = []
    for i in data:
        if i[0] >= 55 and i[1] >7:
            output.append("Senior")
        else:
            output.append("Open")
    return output

"""
Kata: Find the next perfect square!
Rank: 7 kyu
You might know some pretty large perfect squares. But what about the NEXT one? Complete the findNextSquare 
method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral 
perfect square is an integer n such that sqrt(n) is also an integer. If the parameter is itself not a perfect 
square then -1 should be returned. You may assume the parameter is non-negative.

Examples:(Input --> Output)

121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square
"""
import math

def find_next_square(sq):
    square = math.sqrt(sq)
    return (square+1)**2 if square == int(square) else -1

"""
Kata: Regex validate PIN code
Rank: 7 kyu
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""
def validate_pin(pin):
    if len(pin) != 4 and len(pin) != 6: return False
    for i in pin:
        if i.isnumeric(): continue
        else: return False
    return True

"""
Kata: Find the stray number
Rank: 7 kyu
You are given an odd-length array of integers, in which all of them are the same, except for one single number.
Complete the method which accepts such an array, and returns that single different number.
The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
"""
def stray(arr):
    return [i for i in arr if arr.count(i) == 1][0]
    
"""
Kata: Highest and Lowest
Rank: 7 kyu
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""
def high_and_low(numbers):
    numbers = [int(i) for i in numbers.split()]
    return f"{max(numbers)} {min(numbers)}"

"""
Kata: Is It Negative Zero (-0)?
Rank: 7 kyu
There exist two zeroes: +0 (or just 0) and -0.
Write a function that returns true if the input number is -0 and false otherwise (True and False for Python).

In JavaScript / TypeScript / Coffeescript the input will be a number.
In Python / Java / C / NASM / Haskell / the input will be a float.
"""
def is_negative_zero(n):
    return True if n == -0.0 and "-" in str(n) else False

"""
Kata: Vowel one
Rank: 7 kyu
Write a function that takes a string and outputs a strings of 1's and 0's where vowels become 1's and non-vowels become 0's.
All non-vowels including non alpha characters (spaces,commas etc.) should be included.

Examples:
vowelOne "abceios" -- "1001110"
vowelOne "aeiou, abc" -- "1111100100"
"""
def vowel_one(s):
    return "".join(['1' if i.lower() in "aeiou" else '0' for i in s])

"""
Kata: Colour Association
Rank: 7 kyu
Colour plays an important role in our lifes. Most of us like this colour better then another. User 
experience specialists believe that certain colours have certain psychological meanings for us.
You are given a 2D array, composed of a colour and its 'common' association in each array element. 
The function you will write needs to return the colour as 'key' and association as its 'value'.

For example:
var array = [["white", "goodness"], ...] returns [{'white': 'goodness'}, ...]
"""
def colour_association(arr):
    return [{color[0]: color[1]} for color in arr]

"""
Kata: String destroyer
Rank: 7 kyu
You have a starting string of the lowercase alphabet, space-separated:
"a b c d e f g h i j k l m n o p q r s t u v w x y z"
Then you are given random sets of letters to throw against this string. For example:
{'e', 'B', 'F', 'i'}
Whenever there is a match (case sensitive), the letter in the original string is knocked out 
and replaced by an underscore. Using the random set above as an example would result in:
"a b c d _ f g h _ j k l m n o p q r s t u v w x y z"

Write a function destroyer(input_sets) that takes input as a tuple of one or more of these random character 
sets and returns the alphabet formatted as shown, with underscores showing where matches knocked out a letter.
For example:
>>> input_sets = ({'A', 'b'}, {'d', 'C', 'b'})
>>> destroyer(input_sets)
>>> "a _ c _ e f g h i j k l m n o p q r s t u v w x y z"
"""
def destroyer(input_sets):
    result = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    for i in result:
        for j in range(len(input_sets)):
            if i in input_sets[j]:
                result = result.replace(i, "_")
    return result

"""
Kata: Number of Decimal Digits
Rank: 7 kyu
Determine the total number of digits in the integer (n>=0) given as input to the function. For example, 
9 is a single digit, 66 has 2 digits and 128685 has 6 digits. Be careful to avoid overflows/underflows.
All inputs will be valid.
"""
def digits(n):
    return len(str(n))

"""
Kata: Love vs friendship
Rank: 7 kyu
If　a = 1, b = 2, c = 3 ... z = 26
Then l + o + v + e = 54
and f + r + i + e + n + d + s + h + i + p = 108

So friendship is twice stronger than love :-)
The input will always be in lowercase and never be empty.
"""
def words_to_marks(s):
    dict = {}
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        dict[letters[i]] = i+1
    result = [dict[i] for i in s]
    return sum(result)

"""
Kata: String ends with?
Rank: 7 kyu
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""
def solution(string, ending):
    return True if string[len(string) - len(ending):] == ending else False

"""
Kata: Switcheroo
Rank: 7 kyu
Given a string made up of letters a, b, and/or c, switch the position of letters a and b 
(change a to b and vice versa). Leave any incidence of c untouched.

Example:
'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'
"""
def switcheroo(s):
    result = ""
    for i in s:
        if i == "a":
            result += "b"
        elif i == "b":
            result += "a"
        else:
            result += i
    return result

"""
Kata: Smallest value of an array
Rank: 7 kyu
Write a function that can return the smallest value of an array or the index of that value. 
The function's 2nd parameter will tell whether it should return the value or the index.
Assume the first parameter will always be an array filled with at least 1 number and no duplicates. 
Assume the second parameter will be a string holding one of two values: 'value' and 'index'.

min([1,2,3,4,5], 'value') // => 1
min([1,2,3,4,5], 'index') // => 0
"""
def find_smallest(numbers,to_return):
    if to_return == 'value':
        return min(numbers)
    else:
        return numbers.index(min(numbers))Write a function that can return the smallest value of an array or the index of that value. The function's 2nd parameter will tell whether it should return the value or the index.

"""
Kata: Reverse list
Rank: 7 kyu
Write reverseList function that simply reverses lists.
"""
def reverse_list(lst):
    return lst[::-1]

"""
Kata: Jaden Casing Strings
Rank: 7 kyu
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). 
Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known 
for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how 
contractions are expected to be in the example below. Your task is to convert strings to how they would be written 
by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

Example:
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

Link to Jaden's former Twitter account @officialjaden via archive.org
"""
def to_jaden_case(string):
    return " ".join([i[0].upper() + i[1:].lower() for i in string.split(" ")]) if string else ""

"""
Kata: Testing 1-2-3
Rank: 7 kyu
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
Write a function which takes a list of strings and returns each line prepended by the correct number.
The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples: (Input --> Output)
[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
"""
def number(lines):
    return [f"{i+1}: {lines[i]}" for i in range(len(lines))]

"""
Kata: Remove Duplicates
Rank: 7 kyu
You are to write a function called unique that takes an array of integers and returns the array with duplicates removed. 
It must return the values in the same order as first seen in the given array. Thus no sorting should be done, if 52 appears 
before 10 in the given array then it should also be that 52 appears before 10 in the returned array.

Assumptions
All values given are integers (they can be positive or negative).
You are given an array but it may be empty.
They array may have duplicates or it may not.

Example
print unique([1, 5, 2, 0, 2, -3, 1, 10])
[1, 5, 2, 0, -3, 10]

print unique([])
[]

print unique([5, 2, 1, 3])
[5, 2, 1, 3]

"""
def unique(integers):
    return [integers[i] for i in range(len(integers)) if integers[i] not in integers[:i]]
"""
Kata: Form The Minimum
Rank: 7 kyu
Given a list of digits, return the smallest number that could be formed from these digits, using the digits only once (ignore duplicates).

Notes:
Only positive integers will be passed to the function (> 0 ), no negatives or zeros.

Input >> Output Examples:
minValue ({1, 3, 1})  ==> return (13)
Explanation:
(13) is the minimum number could be formed from {1, 3, 1} , Without duplications

minValue({5, 7, 5, 9, 7})  ==> return (579)
Explanation:
(579) is the minimum number could be formed from {5, 7, 5, 9, 7} , Without duplications

minValue({1, 9, 3, 1, 7, 4, 6, 6, 7}) return  ==> (134679)
Explanation:
(134679) is the minimum number could be formed from {1, 9, 3, 1, 7, 4, 6, 6, 7} , Without duplications
"""
def min_value(digits):
    return int("".join(sorted({str(i) for i in digits})))

"""
Kata: Small enough? - Beginner
Rank: 7 kyu
You will be given an array and a limit value. You must check that all values in the array are below 
or equal to the limit value. If they are, return true. Else, return false.
You can assume all values in the array are numbers.
"""
def small_enough(array, limit):
    for i in array:
        if i > limit: return False 
    return True

"""
Kata: Stanton measure
Rank: 7 kyu
The Stanton measure of an array is computed as follows: count the number of occurences for value 1 in the array. 
Let this count be n. The Stanton measure is the number of times that n appears in the array.
Write a function which takes an integer array and returns its Stanton measure.

Examples
The Stanton measure of [1, 4, 3, 2, 1, 2, 3, 2] is 3, because 1 occurs 2 times in the array and 2 occurs 3 times.
The Stanton measure of [1, 4, 1, 2, 11, 2, 3, 1] is 1, because 1 occurs 3 times in the array and 3 occurs 1 time.
"""
def stanton_measure(arr):
    x = arr.count(1)
    return arr.count(x)
