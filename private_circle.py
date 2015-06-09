import math

class Circle:

	def __init__(self, radius = 1):
		self.__radius = radius

	def getRadius(self):
		return self.__radius

	def getPerimeter(self):
		return 2 * self.__radius * math.pi 

	def getArea(self):
		return self.__radius * self.__radius * math.pi 


def main():
	print "Inside main function."
	c = Circle(5)
	print "The object's raidus is ", c.getRadius()
	print "The object's perimettr is ", c.getPerimeter()
	print "The object's area is: ", c.getArea()

main()
print "End of program."
