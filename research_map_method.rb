#array 
letters = [ "a", "b", "c", "d" ]

#collect is a synonym for map. they do the same thing
# in Ruby, you can use {} instead of do
p letters.collect { |x| x + "!" }        #=> ["a!", "b!", "c!", "d!"]
p letters.map { |x| x + "!" }        #=> ["a!", "b!", "c!", "d!"]

#map does something to each item and stores each result as an item in a new array
new_letters = []
letters. each do |letter|
  new_letters << letter + "!"
end
p new_array

#map.with_index is the same as .map but also keeps track of the index of each item
p letters.map.with_index{ |x, i| x * i } #=> ["", "b", "cc", "ddd"]
p letters                               #=> ["a", "b", "c", "d"]

# Example of map on my own: 
