def palindrome(string)
  compared_string = string.downcase.reverse

  if string == compared_string
    return true
  else
    return false
  end
end

p palindrome("racecar")   #=> true
p palindrome("wazzzzup")  #=> false