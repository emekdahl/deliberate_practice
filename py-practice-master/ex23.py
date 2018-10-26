#from sys library
import sys

# countchars function initialized with the argument "filename"
def countchars(filename):
    #empty object count, setting up a counter
    count = {}

    #open a file
    with open(filename) as info:  # inputFile Replaced with filename
        #the variable readfile stands for opening a file and reading it
        readfile = info.read()
        #for each character in the file, now turned uppercase
        for character in readfile.upper():
            #count the characters in the entire file
            count[character] = count.get(character, 0) + 1
    #return count
    return count

#check sys version info to determine which version of python is being used
if __name__ == '__main__':
    #if it is greater than 3, use input
    if sys.version_info.major >= 3:  # if the interpreter version is 3.X, use 'input',
        input_func = input           # otherwise use 'raw_input'
    #otherwise, use raw_input
    else:
        input_func = raw_input
    # the variable imput file is equal to "File Name: "
    inputFile = input_func("File Name : ")
    # print out the character count then the file name
    print(countchars(inputFile))
