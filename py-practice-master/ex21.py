def add(a,b):
    print "Adding %d + %d" % (a,b)
    return a + b

def subtract(a,b):
    print "SUBTRACTING %d - %d" % (a,b)
    return a - b

def multiply(a,b):
    print "MULTIPLYING %d * %d" % (a,b)
    return a * b


def divide(a,b):
    print "DIVIDING %d / %d" % (a,b)
    return a / b

print "Let's do some math with just functions!"

age = add (22,5)
height = subtract(73,4)
weight = multiply(55,2)
iq = divide (260,2)

print "Age: %d, Height: %d, Weight %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."

what = add(age, divide(height, multiply(weight, subtract(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
