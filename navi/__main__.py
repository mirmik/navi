#!/usr/bin/env python3

import numpy
from navi.pose import Pose

def main():
	print("Navi")

	print(Pose().rotation().as_quat())
	print(Pose().scr())