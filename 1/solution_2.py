with open('input.txt', 'r') as f:
    s = [ sum([ int(y) for y in x.splitlines() ]) for x in f.read().split('\n\n') ]
    s.sort(reverse=True)
    print(sum(s[0:3]))
