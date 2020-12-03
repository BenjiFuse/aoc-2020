search_sum = 2020

def find_three_sum(l):
    l.sort()
    for i in range(len(l)-1):
        j = i + 1
        k = len(l) - 1
        curr_sum = l[i] + l[j] + l[k]
        while curr_sum != search_sum :
            curr_sum = l[i] + l[j] + l[k]
            if j >= k:
                break
            if curr_sum > search_sum:
                k -= 1
            elif curr_sum < search_sum:
                j += 1
        if (curr_sum == search_sum):
            return(i, j, k)

with open("input.txt", "r") as f:
    l = [int(n) for n in f.readlines()]
    l.sort()
    i,j,k = find_three_sum(l)

    if i != None:
        print("Solution found: l[{0}]:{1}, l[{2}]:{3}, l[{4}]:{5}. product is {6}".format(
            i, l[i], j, l[j], k, l[k], l[i]*l[j]*l[k]))
    else:
        print("Failed to find two elements that sum to {0} :(".format(search_sum))