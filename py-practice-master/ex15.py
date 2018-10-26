#from the sys library, import the argument variable function
from sys import argv

#the argument variables will be script and filename
script, filename = argv

# the variable txt is equivalent to opening the file named in the argv above
txt = open(filename)

#let the user know what the file name is
print "Here's your file %r: " % filename
#print out the contents of the file
print txt.read()
close (filename)
# the variable txt_again is equivalent to opening the file named in the argv above
print "Type the filename again: "
file_again = raw_input("> ")

#here's the file read again
txt_again = open(file_again)

#here's the file text again
print txt_again.read()
close(file_again)
