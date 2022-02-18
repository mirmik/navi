import unittest
from navi.screw import Screw
import numpy

class ScrewProbe(unittest.TestCase):
	def test_init(self):
		a = Screw([0,0,0], [0,0,0])

	def test_kinematic_carry(self):
		a = Screw(ang=[0,0,10], lin=[0,0,5])
		b = a.kinematic_carry([10,0,0])
		assert(b.lin[0] == 0)
		assert(b.lin[1] == 100)
		assert(b.lin[2] == 5)
