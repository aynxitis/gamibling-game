import random
# still needs withdrawing money or deposit
print("Welcome to this gambling game!\n")
credit = 20.0
choice_play = input("Do you want to start the game (y/n): ").lower()

while choice_play not in ("y", "n"):
    print("\nInvalid choice!")
    choice_play = input("Do you want to start the game (y/n): ").lower()

if choice_play == "n":
    print("\nThanks for your visit!")
else:
    while choice_play == "y":
        print(f"\nYour credit is {credit}$")
        print("[01] Withdraw your money\n[02] Deposit money\n[03] Start playing")
        
        choice_credit = input("\nPlease enter a number (1-3): ")
        if not choice_credit.isdigit():
            print("\nInvalid input! Numbers only.")
            continue

        choice_credit = int(choice_credit)
        if choice_credit not in (1, 2, 3):
            print("\nYour input should be from 1 to 3.")
            continue

        if choice_credit == 1:
            if credit <= 0:
                print("\nNot enough credit to withdraw :(")
            else:
                print(f"\nWithdrawing your credit of {credit}$ ")
            continue 

        elif choice_credit == 2:
            print(f"\nDepositing money")
            continue 

        elif choice_credit == 3:
            if credit <= 0:
                print("\nNot enough credit to play. Please deposit money and try again :(")
                continue

            
            while True:
                bet_input = input(f"\nHow much would you like to bet out of {credit}$: ")
                if not bet_input.isdigit():
                    print("\nInvalid input! Numbers only.")
                    continue
                bet = int(bet_input)
                if bet <= 0 or bet > credit:
                    print("\nYou can't bet that amount!")
                    continue
                break  

            print(f"\nBet amount = {bet}$")

            
            while True:
                die1_input = input("\nPlease enter your first die number (1-6): ")
                die2_input = input("\nPlease enter your second die number (1-6): ")
                if not (die1_input.isdigit() and die2_input.isdigit()):
                    print("\nInvalid input! Numbers only.")
                    continue
                input_die1 = int(die1_input)
                input_die2 = int(die2_input)
                if not (1 <= input_die1 <= 6 and 1 <= input_die2 <= 6):
                    print("\nDice numbers must be between 1 and 6.")
                    continue
                break

            print(f"\nSo your pick is ({input_die1};{input_die2})")

            
            choice = input("\nRoll the dice (y/n): ").lower()
            while choice not in ("y", "n"):
                print("\nInvalid choice!")
                choice = input("Roll the dice (y/n): ").lower()

            if choice == "n":
                print("\nThanks for playing!")
                break

            
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f"\nRolled dice: ({die1};{die2})")

            if (die1 == input_die1 and die2 == input_die2) or (die1 == input_die2 and die2 == input_die1):
                print(f"\nLUCKY DAY! You won {bet * 5}$!")
                credit += bet * 5
            else:
                print(f"\nBetter luck next time! You lost {bet}$")
                credit -= bet

        choice_play = input("\nDo you want to play again (y/n): ").lower()
        while choice_play not in ("y", "n"):
            print("\nInvalid choice!")
            choice_play = input("Do you want to play again (y/n): ").lower()

    print("\nThanks for your visit!")
