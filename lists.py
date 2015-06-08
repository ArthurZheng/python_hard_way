ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list, let us fix that."
stuff = ten_things.split(' ')

more_stuff = []
more_stuff = range(1, 23)

# length = len(stuff)
# for i in range(length, 10):
# 	next_one = more_stuff.pop()
# 	print "Adding: ", next_one
# 	stuff.append(next_one)
# 	print "There are now %d itmes now." % len(stuff)

print "While loop is used here."
while len(stuff) < 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff
print "Let's do some things with stuff."
print stuff[1]
print stuff[-1]
print stuff.pop()
# print ' '.join(stuff)
# print '#'.join(stuff[3:5])