#######################
#        LOOPS        #
#######################

def for_loop(nums):
    nums = [1, 2, 3, 4, 5]
    for num in nums:
        print(num)
# for_loop(nums)

# enumerate
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for i, color in enumerate(colors):
    ratio = ratios[i]
    # print("{}% {}".format(ratio * 100, color))

# loop over multiple lists at the same time
color_list = []
for color,ratio in zip(colors, ratios):
    color_list.append((color, ratio))
    # print("{}: {}".format(ratio * 100, color))
    # print(color_list)

if 'red' in color_list[0]: 
    print('woot')



def range_loop():
    for x in range(5):
        print(x)
    # you can also print 3,4,5
    # for x in range(3,6)

    # or you can skip numbers with an interval like 3,5,7
    # for x in range (3,8,2)
# range_loop()

def while_loop():
    count = 0

    while count < 5:
        print(count)
        count += 1
# while_loop()

def break_loop():
    count = 0
    while True:
        print(count)
        count += 1
        if count >= 5:
            break
# break_loop()

def continue_loop():
    for x in range(10):
        if x % 2 == 0:
            continue
        print(x)
#continue_loop()

txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)
final_prices = map(get_price_with_tax, txns)
# print(list(final_prices))

#######################
# LIST COMPREHENSIONS #
#######################

# list comprehensions
# print([i * i for i in range(10)])

# set comprehensions
quote = "life, uh, finds a way"
# print({i for i in quote if i in 'aeiou'})

# dictionary comprehensions
# print{i: i*i for i in range(10)}

# creating a list of pairs or a matrix
# print([[i for i in range(2)] for _ in range(3)])


#######################
#        LISTS        #
#######################

def append_list():
    squares = []
    for i in range(10):
        squares.append(i*i)
    print(squares)
# append_list()


stuff = [1, 2, 3]

# copy
stuff2 = stuff.copy()
# print(stuff2)

# clear
stuff2 = stuff.clear()
# print(stuff2)

# count
#print(stuff.count(2))

# length
print(len(stuff))

# extend needs work
# print(stuff.extend([4]))

# index
odds = [1,3,5]
# print(odds.index(3))

# insert (index, elem)
odds.insert(0,0)
# print(odds)

# pop
odds.pop()
# print(odds)

# slice
list = ['a', 'b', 'c', 'd']
# print(list[1:-1])

list[0:2] = 'z'
# print(list) 

# remove an element
list.remove('z')
#print(list)

# reverse
list.reverse()
# print(list)

# sort 
list.sort()
# print(list)

#######################
#    TUPLE METHODS    #
#######################

fruits = ("apple", "banana", "cherry")
# or 

# note the double round brackets
fruitz = tuple(("apple", "banana", "cherry"))
# print (fruits)

# print item by index
# print (fruits[1])

# last item
# print (fruits[-1])

more_fruit = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(more_fruit[2:5])

# loop through a tuple
# for fruit in more_fruit:
#     print(fruit)

# check if item exists in tuple
# if "cherry" in more_fruit:
#     print('yup!')

# check length of tuple
# print(len(more_fruit))

# you cannot add or remove items from tuples but apparently can join them?

fruits_to_the_max = fruits + more_fruit
# print(fruits_to_the_max)

# count the number of times you see something in a tuple
# print(fruits_to_the_max.count('apple'))

# can return multiple indices
# print(fruits_to_the_max.index('apple'))