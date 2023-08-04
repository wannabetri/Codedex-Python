'''Instructions
Here's the final project of the chapter!

We just got back from a trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

🇨🇴 Columbian pesos
🇵🇪 Peruvian soles
🇧🇷 Brazilian reais
Create a currency.py program that asks the user for the amount they have in peso, soles, and reais and calculates the total in USD.

Make sure to Google the current exchange rates!

The output of the program should look like this:

What do you have left in pesos? 5600
What do you have left in reais? 105
What do you have left in soles? 280
413.0

The sequence should be:

Currency code example

Bonus: If you can complete this problem and you are a tryhard like me, go back to your code and try to change it into something else (crypto exchange, measurement conversion, different countries, etc.).

Post a screenshot of your code to Twitter by clicking the icon, and then go to #CodedexCurrency to review two other people's work. Be supportive of your fellow coders!'''

# Write code below 💖

pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

total = pesos * 0.058 + soles * 0.28 + reais * 0.21

print(total)