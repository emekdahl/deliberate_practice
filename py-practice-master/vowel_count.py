def getCount(inputStr):
    num_vowels = 0
    # your code here
    for char in inputStr:
        if char in "aeiouAEIUO":
            num_vowels = num_vowels + 1
    return num_vowels

getCount("abracadabra")