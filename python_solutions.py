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
