#filter strings to only show strings starting with the letter A

names_array = ["Susie", "Bobby", "Angel", "Lorie", "Alejandro", "Roberto"] 
a_names = []

names_array.each do |first_name|
  if first_name[0] == "A"
    a_names << first_name
  end
end

p a_names