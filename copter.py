import json
import time

import connection

class Copter:
	def __init__(self, conn, destination=30, control = 15):
		self.conn = conn
		self.m_up = 1 		#ascent motor: default speed
		self.x_control = control
		self.x_destination = destination

		self.latest_horizontal_x = []
		
	#checks if given x is in the control direction
	def horizontal(self, x):
		#print(x)
		

		if  x > (self.x_destination + self.x_control):
			self.conn.send(1,2, 0, 5)
			
		elif x < (self.x_destination - self.x_control):
			self.conn.send(2,1, 0, 5)
		

	#Takes amount given and compas data, calculates average and 
	#sends the average to horizonta()
	def fix_horizon_direction(self, amount):
		
		all_x = 0
		self.latest_horizontal_x = []
		entry_list = self.conn.get(amount)

		if not entry_list:
			return
		for entry in entry_list: 	

			json_entry = json.loads(entry)
			self.latest_horizontal_x.append(int(json_entry['x']))

		all_x = sum(self.latest_horizontal_x) / amount

		print all_x		
		self.horizontal(all_x)

	
