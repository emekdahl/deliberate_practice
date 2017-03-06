def find_longest_word(string)
  p string.split(" ").max_by(&:length)
end

find_longest_word("What is the longest word in this phrase ?")