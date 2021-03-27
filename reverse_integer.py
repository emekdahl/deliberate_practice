def reverse(self, x: int) -> int:
    chars = [char for char in str(x)]
    index = len(chars) - 1
    new_string = ''

    if chars[0] == '-':
        new_string = new_string + '-'
        chars = chars[1:]
        index -= 1

    while index >= 0:
        new_string = new_string + chars[index]
        index -= 1

    reversed_int = int(new_string)

    if reversed_int >= 2**31 or reversed_int <= -2**31:
        return 0

    return reversed_int
