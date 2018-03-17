import sys, json
from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

for line in sys.stdin:
	data = json.loads(line[:-1])
	print data['x']
	print data['y']
	print data['r']
	print data['g']
	print data['b']
	sense.set_pixel(data['x'], data['y'], data['r'], data['g'], data['b'])

#sense = SenseHat()

#while True:
#    x = randint(0, 7)
#    y = randint(0, 7)
#    r = randint(0, 255)
#    g = randint(0, 255)
#    b = randint(0, 255)
#    sense.set_pixel(x, y, r, g, b)
#    sleep(0.01)
