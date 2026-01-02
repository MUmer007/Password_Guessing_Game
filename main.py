import random
easy_words = [
    "cat", "dog", "sun", "book", "tree",
    "ball", "milk", "hat", "car", "fish"
]

medium_words = [
    "garden", "window", "yellow", "planet", "rabbit",
    "basket", "button", "pencil", "bridge", "shadow"
]

hard_words = [
    "algorithm", "philosophy", "architecture", "psychology", "encyclopedia",
    "metamorphosis", "extraordinary", "consciousness", "infrastructure", "hypothesis"
]

print("Welcome to the Password Guessing Game!")
difficulty = input("Choose a difficulty level (easy, medium, hard): ").strip().lower()

level = input("Enter difficulty level (easy, medium, hard): ").strip().lower()

if level == "easy":
    secret_word = random.choice(easy_words)
elif level == "medium":
    secret_word = random.choice(medium_words)
elif level == "hard":
    secret_word = random.choice(hard_words) 
else:
    print("Invalid difficulty level.Defaulting to easy level.")
    secret_word = random.choice(easy_words) 

attempyts = 0
print("\n Guess the Secret Password!")

while True:
    guess = input("Enter your guess: ").strip().lower()
    attempyts += 1

    if guess == secret_word:
        print(f"Congratulations! You've guessed the word '{secret_word}' in {attempyts} attempts.")
        break
    else:
        print("Incorrect guess. Try again!")


hint = ""
for i in range(len(secret_word)):
    if i < len(guess) and guess[i] == secret_word[i]:
        hint += secret_word[i]
    else:
        hint += "*"
print(f"Hint: {hint}")
print("Game Over.")         