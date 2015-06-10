lst = []
print "Enter 10 numbers: "
for i in range(10):
	lst.append(int(raw_input(">>:")))

print "\nDone!\n Now printing the list out.>>>\n"

for i in lst:
	print "number:", i, " "


print "\n\nEnter 10 numbers separated by spaces from one line: "
s = raw_input(">>>>")

items = s.split()
lst2 = [int(x) for x in items]

print "Done again! Now, list is printed out >>>>>>."
for i in lst2:
	print "number is:", i, " "

print "\nEnd of the Program."