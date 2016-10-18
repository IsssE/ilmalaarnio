import json
import time

import connection
import copter

import numpy as np

conn = connection.Connection("54.93.150.126")
cop = Copter(conn)

conn.loop()
time.sleep(1)
conn.get()