def findSmallestInt(arr):
    #Code here
    smallest_num = arr[0]
    for num in arr:
        if num < smallest_num:
            smallest_num = num
    return smallest_num 

findSmallestInt([78,56,232,12,11,43])