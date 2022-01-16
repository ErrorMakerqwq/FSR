# -*- coding: UTF-8 -*-
'''
@Project ：FSR 
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：ErrorMaker(LLJ)
@Date    ：2022/1/16 下午4:34 
@Module characteristics：******
'''
from pyfirmata import Arduino,util
import time


board = Arduino('/dev/ttyACM0')
it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
while True:
	print(board.analog[0].read())
	time.sleep(1)
