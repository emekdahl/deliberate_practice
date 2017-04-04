array_of_arrays = []

def split_array(arr,int)
  array_of_arrays << arr.each_slice(int)
  p array_of_arrays
end




p split_array([0, 1, 2, 3, 4, 5], 2)  #=> [[0, 1], [2, 3], [4, 5]]
p split_array([0, 1, 2, 3, 4, 5], 3)  #=> [[0, 1, 2], [3, 4, 5]]