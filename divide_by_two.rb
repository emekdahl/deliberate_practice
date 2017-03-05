#divide every number in an array by 2

numbers = [1,2,3,4,5]

new_numbers = numbers.map {|number| number.to_f / 2}

p new_numbers