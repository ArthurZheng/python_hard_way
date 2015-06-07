from sys import argv

script, filename = argv

txt = open(filename)
print "Hello there, I am srcipt %s" % script
print "Here is your file %s "  % filename
print txt.read()
txt.close()

print "Type the file name again "
file_again = raw_input(">>>")
txt_again = open(file_again)
print "Here is your file again %s " % file_again
print txt_again.read()
txt_again.close()
