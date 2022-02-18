#!/usr/bin/env

import numpy

class IneriaMomentum:
	def __init__(self, Jxx=1, Jyy=1, Jzz=1, Jxy=0, Jxz=0, Jyz=0):
		self.matrix = numpy.ndarray([
			[Jxx, Jxy, Jxz],
			[Jxy, Jyy, Jyz],
			[Jxz, Jyz, Jzz]
		])

class Inertia:
	def __main__(self, moment=IneriaMomentum(), mass):
		self.moment = moment		
		self.mass = mass