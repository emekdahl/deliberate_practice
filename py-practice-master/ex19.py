def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "That's enough for a party!"
    print "Text a friend. \n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "Or we can use variables from our script: "
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too: "
cheese_and_crackers(10+2, 5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def byob(wine,beer,liquor):
    print "Sorry, we're broke so this party is BYOB."
    print "Your friend brought %d bottles of wine." % wine
    print "My friend brought %d bottles of beer." % beer
    print "Your other friend brought %d bottles of liquor." % liquor

byob(2,12,1)
