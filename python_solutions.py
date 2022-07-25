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

"""
Kata: Simple Pig Latin
Rank: 5 kyu
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""
# Note: Easiest 5 kyu I've done
def pig_it(text):
    text = text.split()
    result = []
    for i in text:
        if i.isalpha(): result.append(i[1:] + i[0] + 'ay') 
        else: result.append(i)
    return " ".join(result)

"""
Kata: Directions Reduction
Rank: 5 kyu
Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed a mountainous desert the smart way.
The directions given to the man are, for example, the following (depending on the language):

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]
You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

["WEST"]
or
{ "WEST" }
or
[West]
Other examples:
In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away.

The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [] (nil in Clojure).

In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

Task
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South.
The Clojure version returns nil when the path is reduced to nothing.
The Rust version takes a slice of enum Direction {North, East, West, South}.
See more examples in "Sample Tests:"
Notes
Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
if you want to translate, please ask before translating.
"""
# Note: Hardest 5 kyu I've done
def dirReduc(arr):
    """
    First we write code that will delete a pair of opposing directions.
    Since we'll this code 4 times, it is easiest to make it a function.
    """
    def temp(a, b):
        for i in range(len(arr)-1): # We use the length minus 1 to avoid exceeding list length.
            """The following conditional checks two list elements side by side and determines 
            whether or not they are opposite. If they are, they are turned into placeholders."""
            if arr[i] == a and arr[i+1] == b:
                arr[i] = 0
                arr[i+1] = 0
        return [i for i in arr if i != 0] # The placeholders are removed here
    
    """Each time the temp function is called, the result is 'cleaned'.
    We have to repeat this process twice to fully 'clean' the data."""
    for i in range(2):
        arr = temp("NORTH", "SOUTH")
        arr = temp("EAST", "WEST")
        arr = temp("SOUTH", "NORTH")
        arr = temp("WEST", "EAST")
        
    return arr

"""
Kata: Moving Zeros To The End
Rank: 5 kyu
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""
def move_zeros(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(0)
    return lst
