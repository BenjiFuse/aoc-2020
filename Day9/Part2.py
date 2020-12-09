window_len = 25

def pair_exists(l, s):
    """returns whether a pair of values exists in the list l that equals s"""
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

def find_contiguous_subarray(l, s):
    """attempts to find a contiguous subarry of l that sums to s"""
    curr_sum = l[0]
    start = 0 

    for i in range(1, len(l)):
        
        while curr_sum > s:
            curr_sum = curr_sum - l[start]
            start += 1

        if curr_sum == s:
            return l[start:i]

        curr_sum += l[i]        

    return None


with open('input.txt') as f:
    nums = [int(l) for l in f.readlines()]
    i = 0
    
    while (pair_exists(nums[i:i+window_len], nums[i+window_len])):
        i += 1

    sl = find_contiguous_subarray(nums[:i+window_len-1], nums[i+window_len])

    print(min(sl)+max(sl))