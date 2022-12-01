with open('input.txt', 'r') as f:

    elve_load = []
    s = 0
    for l in f:
        l = l.splitlines()
        if l[0] != '':
            s = s + int(l[0])
        else:
            elve_load.append(s)
            s = 0 
    print(max(elve_load))
