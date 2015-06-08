def print_two(*args):
	var1, var2 = args
	print "var1 is %s, and var2 is %s" % (var1, var2)
	return 

def print_two_again(arg1, arg2):
	print "arg1 is %r (it has single quotation because I used the raw print here), and arg2 is %s" % (arg1, arg2)
	return 

def print_one(arg):
	print "There is only one parameter here %s" % arg
	return

def print_no_arg():
	print "I  have no argument."
	return

print_two('Jun', 'Jiangli')
print_two_again('Jun Zheng', 'Jiangli Shi')
print_one('Me meme')
print_no_arg()
print "END of Program."
