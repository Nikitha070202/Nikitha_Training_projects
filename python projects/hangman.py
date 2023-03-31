import time
import random

name = input("What is your name? ")
print("Hello, " + name, "It,s time to play now!")
time.sleep(1)
print("Start guessing...\n")
time.sleep(0.5)

## A List Of Secret Words
words = ['python','programming','treasure','creative','medium','horror']
word = random.choice(words)
guesses = ''
turns = 5
hints = 2
start_time = time.time()

def get_hint(word, guesses):
    """
    Returns a hint for the player by revealing a random letter
    that has not been guessed yet.
    """
    unguessed_letters = [c for c in word if c not in guesses]
    hint_letter = random.choice(unguessed_letters)
    return hint_letter

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1
    if failed == 0:
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"\nYou won in {time_taken:.2f} seconds")
        break
    guess = input("\nguess a character:")
    if guess == "hint":
        if hints > 0:
            hints -= 1
            hint = get_hint(word, guesses)
            print(f"\nHint: the word contains the letter '{hint}'")
        else:
            print("\nSorry, no more hints!")
        continue
    guesses += guess
    if guess not in word:
        turns -= 1
        print("\nWrong")
        print("\nYou have", + turns, 'more guesses')
        if turns == 0:
            print("\nYou Lose")
            end_time = time.time()
            time_taken = end_time - start_time
            print(f"\nThe word was '{word}'. You took {time_taken:.2f} seconds to lose.")
