with open('input.txt', 'r') as f:
    s = max([ sum([ int(y) for y in x.splitlines() ]) for x in f.read().split('\n\n')])
    print(s)
