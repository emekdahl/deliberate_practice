#Select method


# Explanation in English: Search through the sequence of the numbers one through ten inclusive of ten, find all numbers that are divisible by 3 without a remainder.
p (1..10).find_all { |i|  i % 3 == 0 }   #=> [3, 6, 9]

#Select method is similar to the .find_all ruby method BUT using a range like the example above in .find_all will break the method. 

#this does NOT work
#p [1..10].select {|num| num % 3 == 0}

#this DOES work
p [1,2,3,4,5,6,7,8,9,10].select {|num| num % 3 == 0}

#if select and .find_all methods didn't exist, we'd have to do the following:
new_numbers = []

numbers = [1,2,3,4,5,6,7,8,9,10]

numbers.each do |number|
  if number % 3 == 0
    new_numbers << number
  end
end

p new_numbers
#as you can see, the output matches the above .select and .find_all methods


#Explanation in English: For the array containing the sequence of numbers 1 -5, select the numbers that are even
p [1,2,3,4,5].select { |num|  num.even?  }   #=> [2, 4]

#Again, if we didn't have .select, we'd have to do something like this to answer the problem above:

even_numbers = []

one_through_five = [1,2,3,4,5]


one_through_five.each do |number|
  if number.even?
    even_numbers << number
  end
end

p even_numbers

#three cheers for .select! 

# Try to break it - .select requires a block, which is the technical name for the part AFTER the the part in pipes, in this case |num|
#if you don't put in a block, then it returns an empty array
p [1,2,3,4,5].select { |num| } 