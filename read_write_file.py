from sys import argv
script, filename = argv

print "Hello there, my name is script: %r" %script
print "We are going to erase %r. " % filename
print "If you don't want that, hit CTRL_C. Or else, hit RETURN."

raw_input("????..............:")

print "Opening the file...."
file = open(filename, 'w')
print "Truncating the file.. Goodbye!"
file.truncate() # truncate empties the file

print "I am going to ask you for 3 lines..."
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I am going to write these to the file."
file.write(line1)
file.write("\n")
file.write(line2)
file.write("\n")
file.write(line3)
file.write("ENd of the file.")

print "And finally, we close it."
file.close()
