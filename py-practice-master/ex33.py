

def printNum(inc):
    numbers = [0,1,2,3,4,5,6]
    for number in numbers:
        print "At the top i is %d" % number

        number += inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % number

    print "The numbers: "

    for number in numbers:
        print number

printNum(2)
