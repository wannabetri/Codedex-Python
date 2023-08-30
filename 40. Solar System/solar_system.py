# Write code below 💖

import random
import math
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Saturn']

random_planet = random.choices(planets)
print (random_planet)
if random_planet == ['Mercury']:
  r = 2440
  area=4*math.pi*(r**2)
  print (round(area))
elif random_planet == ['Venus']:
  r = 6052
  area=4*math.pi*(r**2)
  print (round(area))
elif random_planet == ['Earth']:
  r = 6371
  area=4*math.pi*(r**2)
  print (round(area))
elif random_planet == ['Mars']:
  r = 3390
  area=4*math.pi*(r**2)
  print (round(area))
elif random_planet == ['Saturn']:
  r = 58232
  area=4*math.pi*(r**2)
  print (round(area))
else:
  print ('Oops! An error occurred.')