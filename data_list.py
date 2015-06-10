NUMBER_OF_ELEMENTS = 5
numbers = []
sum = 0

for i in range(NUMBER_OF_ELEMENTS):
	value = int(raw_input("Enter a new number: "))
	numbers.append(value)
	sum += value

average = sum / NUMBER_OF_ELEMENTS

above_numbers = []

count = 0 # The number of elements above average
for i in range(NUMBER_OF_ELEMENTS):
	if numbers[i] > average:
		above_numbers.append(numbers[i])
		count += 1


print "Average is ", average
print "Number of elements above the average is ", count 

for i in range(len(above_numbers)):
	print "Abover number is ", above_numbers[i]


print "End of Program."