# True and False must be capitalized

# takes in an integer x
# returns a bool
# don't change the integer to a string, if possible

def isPalindrome(self, x: int) -> bool:
    return str(x) == (str(x)[::-1])
