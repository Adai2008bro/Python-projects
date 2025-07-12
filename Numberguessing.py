import random
print("Welcome to number guessing game!")
solution = int(input("Choose any number from 1 to 50: "))
answer = random.randint(1, 50)
if solution == answer:
    print("Congratulations!")
else:
    print(f"It's {answer}! 🥲")
    print("Better luck next time!")