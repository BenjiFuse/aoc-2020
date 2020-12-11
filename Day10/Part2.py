def count_paths(l):
    conns = [1] + [0 for x in range(len(l)-1)]
    for i in range(len(l)):
        for j in (1,2,3):
            if l[i] + j in l:
                conns[l.index(l[i]+j)] += conns[i]
    return conns[-1]

with open('input.txt') as f:
    l = [int(i) for i in f.readlines()]
        
    l.extend([0, max(l)+3])
    l.sort()
    
    print(count_paths(l))