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
print(len(five))
print(five[:])


# print random letter and split into a list
answer = random.choice(five)
print(answer)
answer = list(answer)
print(answer)


guess = input("What's your first guess? ")
letters = list(guess)
print("You entered:", guess)

for x in range(len(answer)):
    # correct letter, correct spot
    if letters[x] == answer[x]:
        print(f"{Color.GREEN}{letters[x]}{Color.END}", end="")

    # letter exists somewhere in word
    elif letters[x] in answer:
        print(f"{Color.YELLOW}{letters[x]}{Color.END}", end="")

    # not in word
    else:
        print(letters[x], end="")

print()   # newline


print()


print("\033[92mHELLO\033[0m")
print("NORMAL")
    
 

print("Letters:", letters)