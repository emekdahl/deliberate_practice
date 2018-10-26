def positive_sum(arr):
    # Your code here
    sum = 0
    if arr == []:
        return 0
    else:
        for num in arr:
            if num >= 1:
                sum = sum + num
    return sum
    
positive_sum([1,-4,7,12])