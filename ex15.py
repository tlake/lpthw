# imports the 'argv' module
from sys import argv

# unpacks argv and assigns whatever's in it first to the 'script'
# variable, then to the 'filename' variable
script, filename = argv

# stores, inside the variable 'txt', the result of calling 'open()'
# on 'filename' (which is assigned prior by argv)
txt = open(filename)

# prints to the console the string as written between the "",
# except for '%r', which is a placeholder for the variable named
# after the %
print "Here's your file %r:" % filename
# prints the result of calling 'read()' on whatever's been stored
# inside of the variable 'txt'
print txt.read()

# simple print statement
print "Type the filename again:"
# stores in the variable 'file_again' the user input prompted and
# gained by 'raw_input()' - the contents of the () is what the
# user sees as a propmt
file_again = raw_input("> ")

# stores, inside the variable 'txt_again', the result of calling
# 'open()' on whatever's been stored in the variable 'file_again'
txt_again = open(file_again)

# prints the result of calling 'read()' on whatever's been stored
# inside of the variable 'txt_again'
print txt_again.read()

txt.close()
txt_again.close()
