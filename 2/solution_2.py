import functools
m = {
    'A X\n': 3, # +0+3
    'A Y\n': 4, # +3+1
    'A Z\n': 8, # +6+2
    'B X\n': 1, # +0+1
    'B Y\n': 5, # +3+2
    'B Z\n': 9, # +6+3
    'C X\n': 2, # +0+2
    'C Y\n': 6, # +3+3
    'C Z\n': 7, # +6+1
}
    
with open('input.txt', 'r') as f:
    print(functools.reduce(lambda a, b: m.get(a, a)+m[b], f))
 
