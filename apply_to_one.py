def apply_to_one(f):

    """ calls the function f with 1 as its argument """
    return f(1)


y = apply_to_one(lambda x: x + 4)

print(y)
