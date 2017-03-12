#Reduce Method

# .reduce is a similar method to .inject. It is possible to use .reduce with or without a block for instances that would require a block with .inject


#Without a block
# Take the range of number 5-10 inclusive of ten and add them all together
p (5..10).reduce(:+)                             #=> 45

# Good to know, .reduce can accept an array or a range
p [5,6,7,8,9,10].reduce(:+)

# If you accidentally remove the symbol as the argument for reduce, it breaks the method
#p [5,6,7,8,9,10].reduce(+)

# Take the range of number 5-10 inclusive of ten and add them all together. When using inject, this requires a bit more code
p (5..10).inject { |sum, n| sum + n }            #=> 45

#If .reduce or .inject didn't exist, we'd have to use a loop similar to this one:
example_array = [5,6,7,8,9,10]

product = 1

example_array.each do |number|
  product = product * number
end

puts product

# .reduce with a block
# Take the range of number 5-10 inclusive of ten and multiply them all together
p (5..10).reduce(1, :*)                          #=> 151200

# Same using a .inject
p (5..10).inject(1) { |product, n| product * n } #=> 151200

