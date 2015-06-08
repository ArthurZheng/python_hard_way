from sys import argv

script, input_file = argv

def print_all(file_name):
	print file_name.read()
	return

def rewind(file_name):
	return file_name.seek(0)

def print_a_line(line_count, file_name):
	print line_count, file_name.readline()
	return

current_file = open(input_file)

print "First, let's print the whoel file \n"
print_all(current_file)

print "Now, let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print 3 lines."
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

print "\nEnd of the program."