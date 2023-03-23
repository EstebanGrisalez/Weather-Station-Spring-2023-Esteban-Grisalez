from gpiozero import Button

rain_sensor = Button(6)
BUCKET_SIZE = 0.2794
count = 0

def bucket_tipped():
	global count
	count += 1
	print (count * BUCKET_SIZE, end="\r")
	
def reset_rainfal():
	global count
	count = 0
	
while True:
    rain_sensor.when_pressed = bucket_tipped
