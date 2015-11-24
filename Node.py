# node.py

class Node:

	def __init__(self, coord, action, visited):
		self._c = coord
		self._a = action
		self._v = visited

	@property
	def c(self):
		return self._c

	@c.setter
	def c(self, value):
		self._c += value

	@property
	def a(self):
		return self._a

	@a.setter
	def a(self, value):
		self._a = value

	@property
	def v(self):
		return self._v

	@v.setter
	def v(self, value):
		self._v = value