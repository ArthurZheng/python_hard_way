def add(a, b):
	print "Adding %d and %d together." % (a, b)
	return a + b

def subtract(a, b):
	print "Subtracting %d and %d." %(a, b)
	return a - b

def multiply(a, b):
	print "multiplying %d, %d" %(a, b)
	return a * b

def division(a, b):
	print "Dividing %d and %d" %(a, b)
	return a / b

print "Let's do some math with just functions.!"

age = add(22, 33)
height = subtract(100, 2)
weight = multiply(23, 3)
iq = division(232, 0.5 )

print "Age %d, height %d, weight %d and iq %d" %(age, height, weight, iq)

print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, division(iq, 2))))
print "That becomes: ", what, "Can you do that by hand?"
