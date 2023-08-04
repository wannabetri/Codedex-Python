'''# Instructions
If you slept through your geometry class, a Pythagorean theorem is the relationship between the three sides of a right triangle. It was named after the Greek philosopher Pythagoras, born around 570 BC.

The equation has the form of:


a
2
 +b
2
 =c
2


Take a closer look at this formula:

The a is the length of a short side.
The b is the length of a short side.
The c is the length of the hypotenuse.
The hypotenuse is the longest side of the right triangle.

Create a hypotenuse.py program that asks the user for two numbers, a and b, and calculates the hypotenuse using the Pythagorean equation, rewritten like so:


c=
a
2
 +b
2

​


Bonus: If you can solve this problem and are still looking for a challenge, try the Quadratic formula after!'''

# Write code below 💖

a = float(input('what is the length of a short side?'))
b = float(input('what is the length of a short side?'))
#c = float(input('what is the length of the hypotenuse?'))
c = ((a**2)+(b**2))**0.5
print (c)