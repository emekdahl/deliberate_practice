def sum_of_range(arr)
  a = arr[0].to_i
  b = arr[1].to_i

  if a < b
    (a..b).reduce(:+)
  else
    (b..a).reduce(:+)
  end
end

p sum_of_range([1, 4])
p sum_of_range([4, 1]) 