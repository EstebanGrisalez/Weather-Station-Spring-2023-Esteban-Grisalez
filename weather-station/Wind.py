from gpiozero import Button
import time
import math
import statistics

wind_count = 0
radius_cm = 9.0
wind_interval = 5

CM_IN_A_KM = 100000.0
SECS_IN_AN_HOUR = 3600
ADJUSTMENT = 1.18

store_speeds = []

def spin():
    global wind_count
    wind_count = wind_count + 1
    print( wind_count )

def calculate_speed(time_sec):
    global wind_count
    circumference_cm = (2*math.pi)*radius_cm
    rotations = wind_count / 2.0

    dist_km = (circumference_cm*rotations)/CM_IN_A_KM

    km_per_sec = dist_km / time_sec
    km_per_hour = km_per_sec*SECS_IN_AN_HOUR

    return km_per_hour*ADJUSTMENT

def reset_wind():
    global wind_count
    wind_count = 0

wind_speed_sensor = Button(5)
wind_speed_sensor.when_activated = spin

while True:
    start_time = time.time()
    while time.time() - start_time <= wind_interval:
        reset_wind()
        time.sleep(wind_interval)
        final_speed = calculate_speed(wind_interval)
        store_speeds.append(final_speed)

    wind_gust = max(store_speeds)
    wind_speed = statistics.mean(store_speeds)
    print(wind_speed, wind_gust)
    
