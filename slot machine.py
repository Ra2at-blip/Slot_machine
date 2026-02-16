import random

MAX_LINES = 3
BET_PER_LINE = 10

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit?$: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")

def get_number_of_lines(balance):
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            total_bet = lines * BET_PER_LINE
            if 1 <= lines <= MAX_LINES:
                if total_bet <= balance:
                    return lines
                else:
                    print(f"Not enough balance to bet on {lines} lines. You need ${total_bet}, but you have ${balance}.")
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number.")

def spin_reels():
    symbols = ['🍒', '🍋', '🍊', '🍉', '🍇', '⭐']
    reels = [[random.choice(symbols) for _ in range(3)] for _ in range(3)]
    return reels

def display_reels(reels):
    for row in reels:
        print(" | ".join(row))

def main():
    balance = deposit()

    while True:
        print(f"\nCurrent balance: ${balance}")
        
        if balance < BET_PER_LINE:
            print("❌ Not enough balance to continue. Game over!")
            break

        lines = get_number_of_lines(balance)
        total_bet = lines * BET_PER_LINE

        balance -= total_bet
        print(f"Betting ${BET_PER_LINE} per line on {lines} lines. Total bet: ${total_bet}")
        print(f"Remaining balance: ${balance}")

        print("\nSpinning the reels...\n")
        reels = spin_reels()
        display_reels(reels)

        play_again = input("\nDo you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

    print(f"\nThanks for playing! Final balance: ${balance}")

if __name__ == "__main__":
    main()
