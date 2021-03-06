import json
import time

#import connection
#import copter

import numpy as np
import localization as lx

#conn = connection.Connection("54.93.150.126")
#cop = Copter(conn)

class Navigation:
	def __init__(self):
		self.beacons = {}
		self.p = lx.Project(mode='3D')


	def add_beacon(self, baddr, coord):
		#add/uppdate beacon position. coord: (x, y, z)
		self.beacons[baddr] = coord
		self.p.add_anchor(baddr, coord)

	def strength_to_distance(self, strength):
		#return approximated distance to beacon
		#todo: kaava
		return float(strength)


	def get_position(self, beacon_s):
		#returns np.array(x,y,z): approximate position. 
		#beacon_s: list of [(baddr, strength), (baddr, strength)]
		b1, b2, b3 = beacon_s
		dist_b1 = self.strength_to_distance(b1[1])
		dist_b2 = self.strength_to_distance(b2[1])
		dist_b3 = self.strength_to_distance(b3[1])

		#coord_b1 = self.beacons[b1[0]]
		t, label = self.p.add_target()
		t.add_measure("1", dist_b1)
		t.add_measure("2", dist_b2)
		t.add_measure("3", dist_b3)

		self.p.solve()
		return(t.loc.x, t.loc.y, t.loc.z)

n = Navigation()
n.add_beacon("1", (0, 0, 0))
n.add_beacon("2", (2, 2, 2))
n.add_beacon("3", (2, 0, 0))

print(n.get_position([(1, 1.4), (2, 1.4), (3, 1.4)]))

