'''# Instructions
The Magic 8 Ball is a popular office toy and children's toy invented in the 1940's for fortune-telling and advice seeking. 🎱

It's an oversized 8 ball with some of the following answers:

Yes - definitely.
It is decidedly so.
Without a doubt.
Reply hazy, try again.
Ask again later.
Better not tell you now.
My sources say no.
Outlook not so good.
Very doubtful.
Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

The output should have the following format:

Question:      [Question]
Magic 8 Ball:  [Answer]

For example:

Question:      Is Codédex better than Udemy yet?
Magic 8 Ball:  Better not tell you now.'''

# Write code below 💖

import random

Question = input('')
random_number = random.randint(1, 9)

if random_number == 1:
    answer = 'Yes - definitely'
elif random_number == 2:
    answer = 'It is decidedly so'
elif random_number == 3:
    answer = 'Without a doubt'
elif random_number == 4:
    answer = 'Reply hazy, try again'
elif random_number == 5:
    answer = 'Ask again later'
elif random_number == 6:
    answer = 'Better not tell you now'
elif random_number == 7:
    answer = 'My sources say no'
elif random_number == 8:
    answer = 'Outlook not so good'
elif random_number == 9:
    answer = 'Very doubtful'
else:
    answer = 'Error'

print('Question:      ' + Question)
print('Magic 8 Ball:  ' + answer)