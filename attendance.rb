#ATTENDENCE CHECK
  
#Create a function that takes a weekday String as an argument. It then iterates over the classRoom array and returns an array of all the students present for class on that weekday

class_room = [
  {
    "Marnie" => [
        {"Monday" => true},
        {"Tuesday" => true},
        {"Wednesday" => true},
        {"Thursday" => true},
        {"Friday" => true}
      ]
  },
  {
    "Lena" => [
        {"Monday" => false},
        {"Tuesday" => false},
        {"Wednesday" => true},
        {"Thursday" => false},
        {"Friday" => true}
      ]
  },
  {
    "Shoshanna" => [
        {"Monday" => true},
        {"Tuesday" => true},
        {"Wednesday" => false},
        {"Thursday" => true},
        {"Friday" => false}
      ]
  },
  {
    "Jessa" => [
        {"Monday" => false},
        {"Tuesday" => false},
        {"Wednesday" => false},
        {"Thursday" => false},
        {"Friday" => true}
      ]
  }
]

present = []

def attendance (weekday)
  class_room.each do |person, weekday|
    if person[weekday] == true
      present << person
    end
  end
end

puts attendance("Monday")