# A,X -> +3+1 = +4
# A,Y -> +6+2 = +8
# A,Z -> +0+3 = +3
# B,X -> +0+1 = +1
# B,Y -> +3+2 = +5
# B,Z -> +6+3 = +9
# C,X -> +6+1 = +7
# C,Y -> +0+2= +2
# C,Z -> +3+3 = +6
with open('input.txt', 'r') as f:
    s = 0
    for l in f.readlines():
        print(l)
        if l == 'A X\n':
            s += 4
        elif l == 'A Y\n':
            s += 8 
        elif l == 'A Z\n':
            s += 3
        elif l == 'B X\n':
            s += 1
        elif l == 'B Y\n':
            s += 5
        elif l == 'B Z\n':
            s += 9
        elif l == 'C X\n':
            s += 7
        elif l == 'C Y\n':
            s += 2
        elif l == 'C Z\n':
            s += 6
        
    print(s)
         
    
