#double every other array in an array of numbers

numbers = [1, 2, 3, 4, 5]

new_numbers = numbers.map.with_index {|number, i| i % 2 == 0 ? number : number * 2 }

p new_numbers

# i = 0

# loop do
#   # multiply the first item in the array by two
#   numbers.each

#   #insert that value back into the new array

#   #add add one to the index value

#   #push that value straight into the new array

# end