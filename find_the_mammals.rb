#Array of Hashes - return only species which are mammals

living_beings = [
  {"species" => "lion", "kingdom" => "mammal"},
  {"species" => "mushroom", "kingdom" => "fungus"},
  {"species" => "blue whale", "kingdom" => "mammal"},
  {"species" => "aloe plant", "kingdom" => "plant"},
  {"species" => "blue bird", "kingdom" => "mammal"},
]

mammals = []
# mammals = living_beings.select {|being|[:species]}



living_beings.each do |being|
  if being["kingdom"].include? "mammal"
    mammals << being
  end
end

p mammals
