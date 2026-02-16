import random

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
 
def load_apple_wordlist():
    path = "/usr/share/dict/words"
    with open(path, encoding="utf-8", errors="ignore") as f:
        return [w.strip().lower() for w in f if w.strip().isalpha()]

words = load_apple_wordlist()

five = [w for w in words if len(w) == 5]

"""
print(len(five))
print(five[:])

"""


# print random letter and split into a list
answer = random.choice(five)
# print(answer)
answer_list = list(answer)
# print(answer_list)

num_guesses = 0

guess = input("What's your first guess? ")
while guess != answer and num_guesses < 4:
    letters = list(guess)
    print("You entered:", guess)

    for x in range(len(answer_list)):
        # correct letter, correct spot
        if letters[x] == answer_list[x]:
            print(f"{Color.GREEN}{letters[x]}{Color.END}", end="")

        # letter exists somewhere in word
        elif letters[x] in answer_list:
            print(f"{Color.YELLOW}{letters[x]}{Color.END}", end="")

        # not in word
        else:
            print(letters[x], end="")

    print()   # newline


    print()
    num_guesses = num_guesses + 1
    guess = input("What's your next guess? ")

if num_guesses > 3:
    print(f"You lose lmao the word was {Color.RED}{answer}{Color.END}. Better luck next time!")
    
elif guess == answer:
    print(f"Congrats you guessed the word correctly and the word was {Color.GREEN}{answer}{Color.END}. And unlike NYT wordle, you can play again today!!!")