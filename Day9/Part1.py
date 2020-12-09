window_len = 25

def pair_exists(l, s):
    l.sort()
    i, j = 0, len(l)-1

    while (i < j):
        temp_sum = l[i] + l[j]
        if temp_sum == s:
            return True
        if temp_sum < s:
            i += 1
        elif temp_sum > s:
            j -= 1
    
    return False

with open('input.txt') as f:
    nums = [int(l) for l in f.readlines()]
    i = 0
    
    while (pair_exists(nums[i:i+window_len], nums[i+window_len])):
        i += 1

    print(nums[i+window_len])