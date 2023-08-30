# Write code below 💖

import random


def play():
    symbols = ('🍒 ', '🍇 ', '🍉 ', ' 7️⃣ ')
    results = random.choices(symbols, k=3)
    result_string = '|'.join(results)
    print(result_string)
    if all(symbol == '7️⃣' for symbol in results):
        print('Jackpot! 💰')
    else:
        print('Thanks for playing!')


while True:
    play_again = input("Do you want to play again? (Y/N): ").strip().lower()
    if play_again == 'y':
        play()
    elif play_again == 'n':
        print('Thanks for playing! Have a great day!')
        break
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")


