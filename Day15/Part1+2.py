with open('input.txt') as f:
    nums = [int(i) for i in f.read().split(',')]
    last_turns = {n:[i] for i, n in enumerate(nums)}
    i = len(nums)
    
    while i < 30000000:  # change to 'i < 2020' for part 1 answer
        last_spoken = nums[-1]
        indexes = last_turns.get(last_spoken, 0)
        n = 0   # last occurence was first time, say '0'
        if len(indexes) > 1:
            n = indexes[-1] - indexes[-2]           # last occurence was spoken twice before
        if not n in last_turns: last_turns[n] = []  # add new word key+list to diff
        last_turns[n] = last_turns[n][-1:] + [i]
        nums.append(n)
        i += 1

    print(nums[-1])