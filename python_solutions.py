""" 
Kata: Multiples of 3 or 5
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
Additionally, if the number is negative, return 0 (for languages that do have them).
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
