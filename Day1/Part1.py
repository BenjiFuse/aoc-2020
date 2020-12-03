search_sum = 2020

with open("input.txt", "r") as f:
    l = [int(i) for i in f.readlines()]
    l.sort()
    i = 0
    j = len(l) - 1
    curr_sum = l[i] + l[j]
    while curr_sum != search_sum:
        curr_sum = l[i] + l[j]
        if i >= j:
            break
        if curr_sum > search_sum:
            j -= 1
        elif curr_sum < search_sum:
            i += 1

if (curr_sum == search_sum):
    print("Solution found: l[{0}]:{1}, l[{2}]:{3}, product is {4}".format(i, l[i], j, l[j], l[i]*l[j]))
else:
    print("Failed to find two elements that sum to {0} :(".format(search_sum))