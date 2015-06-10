
def choose_month():
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
	month_input = int(raw_input("Enter a number for the month (1-12)"))
	print "The month you pick is ", month_input, " month name: ", months[month_input-1]

def main():
	print "Enter a month number to get your month name."

	print "How many times do you want to play this game?"

	times = int(raw_input(">>>"))

	for i in range(times):
		print "\nRound number ", i +1
		choose_month()

	print "\nEnd of the Game."

main()
