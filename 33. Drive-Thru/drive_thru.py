# Write code below 💖
def welcome():
  print('Welcome to Giant cachopo\'s!')
  print('Here\'s the menu:')
  print('1. 🥩 Cachopo')
  print('2. 🥟 Croqueta')
  print('3. 🍾 Sidra')
  print('4. 🥧 Tarta gijonesa')
  print('5. 🥞 Frixuelos')

def get_item(x):
  if x == 1:
    return '🥩 Cachopo'
  elif x == 2:
    return '🥟 Croqueta'
  elif x == 3:
    return '🍾 Sidra'
  elif x == 4:
    return '🥧 Tarta gijonesa'
  elif x == 5:
    return '🥞 Frixuelos'
  else:
    return "invalid option"


welcome()

option = int(input('What would you like to order?'))
print(get_item(option))