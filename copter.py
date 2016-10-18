class Copter:
	def __init__(self, conn, control=40):
		self.conn = conn
		self.m_up = 1 		#ascent motor: default speed
		self.x_control = control

		self.latest_horizontal_x = []
		self.average.x = 0
	def horizontal(self, x):
		#print(x)
		

		if (x > self.x_control):
			print(str(x) + " suurempi " + str(self.x_control))
			self.conn.send(2,1, 2, 30)
			time.sleep(0.5)
		elif (x < (self.x_control * -1)):
			print(str(x) < str(self.x_control * -1))
			self.conn.send(1,2, 2, 30)
			time.sleep(0.5)


	def fix_horizon_direction(self):

		entry_list = conn.get()
		
		for entry in entry_list: 	

			json_entry = json.loads(entry)
			self.latest_horizontal_x.append(json_entry['x'])

		for x in self.latest_horizontal_x:
			all_x = x + all_x

		print(all_x)
		self.horizontal(all_x)

	
