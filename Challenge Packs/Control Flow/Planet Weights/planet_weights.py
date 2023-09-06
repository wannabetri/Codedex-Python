# Write code below 💖

print('==============')
print('Planet Weights')
print('==============')
print('')

earth_weigh = float(input('what is your weight?'))
planet = float(input('What planet are you on?'))

if planet == 1 :
  destination_weight=earth_weigh * 0.38
  print ("Your weight is:", destination_weight)
elif planet == 2:
  destination_weight=earth_weigh * 0.91
  print ("Your weight is:", destination_weight)
elif planet == 3:
  destination_weight=earth_weigh * 0.38
  print ("Your weight is:", destination_weight)
elif planet == 4:
  destination_weight=earth_weigh * 2.53
  print ("Your weight is:" + destination_weight)
elif planet == 5:
  destination_weight=earth_weigh * 1.07
  print ("Your weight is:", destination_weight)
elif planet == 6:
  destination_weight=earth_weigh * 0.89
  pprint ("Your weight is:", destination_weight)
elif planet == 7:
  destination_weight=earth_weigh * 1.14
  print ("Your weight is:", destination_weight)
else:
  print ("We do not have more data than gravity on previous planets")
