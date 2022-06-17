# Kata: Multiples of 3 or 5
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
