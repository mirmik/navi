import numpy
from scipy.spatial.transform import Rotation
import navi.screw

class Pose:
	def __init__(self, ang=Rotation.identity(), lin=[0,0,0]):
		self.ang = ang
		self.lin = lin

	def rotation(self):
		return self.ang

	def scr(self):
		return navi.screw.Screw(self.ang.as_rotvec(), self.lin)

	def small_movement(self, scr, delta):
		small = scr.to_small_movement(delta)
		self.ang = self.ang.concatenate(small.ang)
		self.lin = self.lin + small.lin

