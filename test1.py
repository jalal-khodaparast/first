import numpy as np
import math
import matplotlib.pyplot as plt

import argparse
import math
import datetime
import time
##############################################

points = []
times = []
ys = []

f=1/60
omega=2*math.pi*(f)
now = datetime.datetime.today()

for t in range(0, 60):
        y = 1000*np.sin(omega*t)

        point = {
            "measurement": 'foobar',
            "time": int(now.strftime('%f'))+t,
            "fields": {"value": y}
        }
        points.append(point)

        times.append(t)
        ys.append(y)



print(times)
plt.plot(times,ys)
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.grid(True)
plt.title("sine waveform")
plt.show()
######################################################
from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost', port=8086)
#client.create_database('pyexample')
#client.create_database('jalal')
dbs=client.get_list_database()

print(dbs)

USER = 'root'
PASSWORD = 'root'
DBname= 'pyexample2'

client = InfluxDBClient('localhost', 8086, USER, PASSWORD, DBname)
print("Create database: " + DBname)
client.create_database(DBname)
client.switch_database(DBname)

client.write_points(points)

time.sleep(1)


