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

