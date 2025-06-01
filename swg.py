import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Welcome to Snake-Water-Gun Game!")
print("Rules: \n- Snake (s) drinks Water (w).\n- Water (w) douses Gun (g).\n- Gun (g) shoots Snake (s).")

# Computer's Turn
print("\nComputer is making its choice...")
randNo = random.randint(1, 3)
comp = 's' if randNo == 1 else 'w' if randNo == 2 else 'g'

# User's Turn with validation
while True:
    you = input("Your Turn: Choose Snake (s), Water (w), or Gun (g): ").lower()
    if you in ['s', 'w', 'g']:
        break
    print("Invalid input! Please choose 's', 'w', or 'g'.")

# Determine the result
a = game(comp, you)

print(f"\nComputer chose: {comp}")
print(f"You chose: {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
