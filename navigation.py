import json
import time

import connection
import copter

#import numpy as np

conn = connection.Connection("54.93.150.126")
cop = copter.Copter(conn)

while True:
	conn.loop()
	print(conn.get(5))
