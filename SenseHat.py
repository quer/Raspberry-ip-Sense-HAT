import sys, json
from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

for line in sys.stdin:
	data = json.loads(line[:-1])
	sense.set_pixel(data['x'], data['y'], data['r'], data['g'], data['b'])