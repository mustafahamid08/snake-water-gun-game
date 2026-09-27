import random

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

user_score = 0
computer_score = 0

while True:
    youstr = input("\nEnter your choice (s/w/g) or q to quit: ").lower()

    if youstr == "q":
        break

    if youstr not in youDict:
        print("Invalid choice! Please enter s, w, or g.")
        continue

    computer = random.choice([-1, 0, 1])
    you = youDict[youstr]

    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a draw!")
    elif (
        (computer == -1 and you == 1) or
        (computer == 1 and you == 0) or
        (computer == 0 and you == -1)
    ):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}")

print("\nFinal Score")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")
print("Thanks for playing!")