'''Instructions
Since 1927, a rollercoaster known as "The Cyclone" has delighted riders visiting Coney Island in Brooklyn, New York. 🎢

The operator of the ride is installing a new entry system (the height requirement is 137 cm and the cost to ride is 10 credits), and needs your help with writing the program for it!

Create a new file called the_cyclone.py.

Ask the user what their height is and how many credits they have using the int() and input() functions. Make sure to store the values in a height variable and a credits variable.

Use a combination of relational and logical operators to create the rules:

If they are tall enough and have enough credits, print "Enjoy the ride!"
Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride."
Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits."
Else, print a message saying they are not tall enough and they do not have enough credits.
Bonus: After solving, try to rework the solution to use all three operators - and, not, & or! For the not operator, use a boolean value.'''

# Write code below 💖

height = int(input("how tall are you?"))
credits = int(input("How many credits do you have?"))

if height >=137 and credits >= 10:
  print ('all ok')
elif height < 137 and credits >= 10:
  print ('you are to small')
elif height >=137 and credits < 10:
  print ('you don´t have credits')
else:
  print('not ok')