# the syntax is list.sort() list.reverse()

# check for key in dict with if X in dict

def largestUniqueNumber(self, A: List[int]) -> int:
    num_tracker = {}
    A.sort()
    A.reverse()

    for num in A:
        if num in num_tracker:
            num_tracker[num] += 1
        else:
            num_tracker[num] = 1

    for item in num_tracker:
        if num_tracker[item] == 1:
            return item

    return -1
