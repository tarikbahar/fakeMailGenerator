import mouse
import time
import random

def move():
    mouse.move(random.randint(0,1500), random.randint(0,800), absolute=True, duration=2)
    print("Allahümme salli alâ Muhammed ve alâ âli Muhammed.")
    time.sleep(10)

try:
    while True:
        move()
except KeyboardInterrupt:
    pass