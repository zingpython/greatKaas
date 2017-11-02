import math

class SpaceShip:
	#Ship position is a dictionary that will hold two key:value pairs: "X" and "Y"
	ship_position = {}
	goal_position = {}
	name = ""
	speed = 0

	def __init__(self,shipX, shipY, goalX, goalY, name, speed):
		#puts shipX and shipY in the ship position dictionary
		self.ship_position["x"] = shipX
		self.ship_position["y"] = shipY
		self.goal_position["x"] = goalX
		self.goal_position["y"] = goalY
		self.name = name
		self.speed = speed

	#Time to target is calculated by finding the hypotenuse and dividing by the speed
	def timeToTarget(self):
		#A and B are the diffference between the ship position and he goal position
		a = self.goal_position["x"] - self.ship_position["x"]
		b = self.goal_position["y"] - self.ship_position["y"]
		#a^2 + b^2 = c^2
		hypotenuse = math.sqrt( (a**2) + (b**2) )
		#Divide hypotenuse by speed
		time_left = hypotenuse / self.speed
		return time_left

	def advance(self):
		#A and B are the diffference between the ship position and he goal position
		a = self.goal_position["x"] - self.ship_position["x"]
		b = self.goal_position["y"] - self.ship_position["y"]
		#a^2 + b^2 = c^2
		hypotenuse = math.sqrt( (a**2) + (b**2) )
		#If we find the degree we can use the degree to calculate the adjustment to our current x and y to get our new x and y
		degree = (math.asin(b/hypotenuse))
		#Use the degree to calculate the adjustment of Y using the SOH formula
		opposite = math.sin(degree)*self.speed
		#Use the degree to calculate the adjustment of X using the CAH formula
		adjacent = math.cos(degree)*self.speed

		#Adjust x and y using the opposite and adjacent varaibles
		self.ship_position["x"] = self.ship_position["x"]+adjacent
		self.ship_position["y"] = self.ship_position["y"]+opposite



my_ship = SpaceShip(1,1,8,8,"Hyperion",2)

print(my_ship.ship_position)
print(my_ship.goal_position)

print(my_ship.timeToTarget() )

my_ship.advance()

print(my_ship.ship_position)
print(my_ship.goal_position)