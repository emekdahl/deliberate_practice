def plusOne(self, digits: List[int]) -> List[int]:
    stringy = ''
    for digit in digits:
        stringy += str(digit)

    return [char for char in str(int(stringy) + 1)]


plusOne(self, [1, 2, 3])

# should return [1,2,4]
