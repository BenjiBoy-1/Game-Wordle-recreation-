def load_system_dict(path="/usr/share/dict/words"):
    with open(path, encoding="utf-8", errors="ignore") as f:
        return [w.strip().lower() for w in f if w.strip().isalpha()]
five = [w for w in words if len(w) == 5]


guess = input("What's your first guess? ")
letters = list(guess)
print("You entered:", guess)
print("Letters:", letters)