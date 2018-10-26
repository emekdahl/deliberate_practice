#from the sys library, import the argv module
from sys import argv

#the two arguments for the argv variable will be the script name and the input file
script, input_file = argv

#the print all function reads the whole file
def print_all(f):
    print f.read()

#the rewind funtion goes back to the start of the file.
def rewind(f):
    f.seek(0)

# print a line prints the line count and then reads that line of the file.
def print_a_line(line_count, f):
    print line_count, f.readline()

#the current file variable is equal to opening the input_file
current_file = open(input_file)

print "First let's print the whole file:\n"

#output is printing the entire file
print_all(current_file)

print "Now let's rewind, kind of like a tape."
#then go back to the start
rewind(current_file)

print "Let's print three lines:"
#then print three lines, one at a time.
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line +=1
print_a_line(current_line, current_file)
