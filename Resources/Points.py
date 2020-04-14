import math

class Points:
	def __init__(self, x=0.0, y=0.0):
		self.x = float(x)
		self.y = float(y)

	def cartesianDistance(self,P):
		print(self.x, P.x, self.y, P.y)
		return math.sqrt((self.x - P.x)**2.0 + (self.y - P.y)**2.0)

