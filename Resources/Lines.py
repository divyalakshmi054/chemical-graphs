import Resources.Points as pt
import math

class Lines:
	def __init__(self, p1 = pt.Points(), p2 = pt.Points()):
		self.p1 = p1
		self.p2 = p2

	def slope(self):
		p_inf = float("inf")
		n_inf = float("-inf")
		if self.p1.x == self.p2.x:
			if self.p2.y > self.p1.y:
				return p_inf
			else:
				return n_inf
		return (self.p2.y - self.p1.y)/(self.p2.x - self.p1.x)

	def angle(self):
		return math.atan(self.slope())