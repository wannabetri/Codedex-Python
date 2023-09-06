# Write code below 💖

import random
answer = int(input('What is the total (2-12)?'))
dado_one = random.randint(1, 6)
dado_two = random.randint(1, 6)
total = dado_one + dado_two

while answer != total:
  answer = int(input('What is the total (2-12)?'))
else:
  print('You got it!')