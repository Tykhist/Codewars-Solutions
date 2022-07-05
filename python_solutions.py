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
Kata: List Filtering
Rank: 7 kyu
In this kata you will create a function that takes a list of non-negative integers 
and strings and returns a new list with the strings filtered out.
"""
def filter_list(l):
    return [x for x in l if type(x) == type(int())]

"""
Kata: Human Readable Time
Rank: 5 kyu
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""
def make_readable(seconds):
    hr = 0
    mn = 0
    
    if seconds >= 359999:
        return "99:59:59"
    
    if seconds > 60*60-1:
        remainder = seconds % (60*60)
        hr = (seconds - remainder) / (60*60)
        seconds = remainder
        
    if seconds > 59:
        remainder = seconds % 60
        mn = (seconds - remainder) / 60
        seconds = remainder
        
    return f"{int(hr):02}:{int(mn):02}:{int(seconds):02}"

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
Kata: Andy's coffee addiction
Rank: Beta
Andy LOVES coffee, he's totally addicted. Unfortunately he drinks too much so the doctor has advised he only drinks 6 espresso shots a day.
Andy only drinks one type of coffee a day, and each have the following number of espresso shots in them:

espresso = 1 shot
double espresso = 2 shots
flat white = 2 shots
latte = 1 shot
mocha = 2 shots
decaf = 0 shot

Challenge:
Create a function that returns the following:

If Andy has consumed no shots return "You haven't even had coffee today!"
If Andy has had less than 4 shots return "The doctor won't be worried yet!"
If Andy has had 4 shots return "You can have 2 more shots then no more!"
If Andy has had 5 shots return "You can only have an espresso, latte or a decaf now"
If Andy has had 6 or more shots return "Only decaf for you now!"
"""
def caffeine(coffee, number):
    shots = {
        "espresso": 1,
        "double espresso": 2,
        "flat white": 2,
        "latte": 1,
        "mocha": 2,
        "decaf": 0
    }
    
    caff = shots[coffee] * number
    
    if caff == 0: return "You haven't even had coffee today!"
    elif caff < 4: return "The doctor won't be worried yet!"
    elif caff == 4: return "You can have 2 more shots then no more!"
    elif caff == 5: return "You can only have an espresso, latte or a decaf now"
    elif caff >= 6: return "Only decaf for you now!"

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
Kata: Friend or Foe?
Rank: 7 kyu
Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
"""
def friend(x):
    return [i for i in x if len(i) == 4]

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
Kata: Range Extraction
Rank: 4 kyu
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers

or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all 
integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"

Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:
solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
"""
def solution(args):
    new = []
    for i in range(len(args[1:])):
        if args[i+1] == args[i]+1 and args[i-1] == args[i]-1:
            new.append('-')
        else:
            new.append(str(args[i]))
    new.append(str(args[-1]))
    
    new = [new[i] for i in range(len(new[:-1])) if new[i] != new[i+1]]
    new.append(str(args[-1]))
    
    new = ','.join(new)
    new = new.replace(',-,', '-')
    
    return new

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
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

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
