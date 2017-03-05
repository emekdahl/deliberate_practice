#filter out any numbers greater than 5 given the array [1,77,3,99,4,10,87,2]
numbers = [1,77,3,99,4,10,87,2]
small_numbers = []

numbers.each do |number|
  if number <= 5
    small_numbers << number
  end
end

p small_numbers