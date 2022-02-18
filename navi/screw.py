import numpy
import navi.pose
from scipy.spatial.transform import Rotation

class Screw:
	def __init__(self, ang, lin):
		self.ang = ang
		self.lin = lin

	def __str__(self):
		return "{" + str(self.ang) + "," + str(self.lin) + "}"
	
	def force_carry(self, mov):
		return Screw(self.ang + numpy.cross(mov, self.lin), self.lin)

	def kinematic_carry(self, mov):
		return Screw(self.ang, self.lin + numpy.cross(self.ang, mov))

	def to_pose(self):
		return navi.pose.Pose(ang=Rotation.from_rotvec(self.ang), lin=self.lin)

	def rotate_by(self, rotation):
		return Screw(rotation.apply(self.ang), rotation.apply(self.lin))