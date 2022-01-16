# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import matplotlib.pyplot as plt
from pyfirmata import Arduino,util
SIZEOFDATA=20


def FIFO(ForceData_list):
	if len(ForceData_list) == SIZEOFDATA:
		i = 0
		while (i < SIZEOFDATA - 1):
			ForceData_list[i] = ForceData_list[i + 1]
			i = i + 1
		ForceData_list[SIZEOFDATA - 1] = val
		print("***")
	else:
		ForceData_list.append(val)
		print("+++")
	return ForceData_list

import time
board = Arduino('/dev/ttyACM0')
it = util.Iterator(board)
plt.figure(figsize=(10, 10))
f = open('/home/ubantu/Desktop/test.csv','w',encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(["force"])

ForceData_list=[]*SIZEOFDATA
it.start()
board.analog[0].enable_reporting()
while True:
	print(ForceData_list)
	plt.clf()

	val=board.analog[0].read()
	csv_writer.writerow([val])


	plt.plot(FIFO(ForceData_list))
	plt.pause(0.0001)
	plt.draw()

