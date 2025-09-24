def ordinal(n):
    if 11 <= n % 100 <= 13:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + suffix

alphabet = 'abcdefghijklmnopqrstuvwxyz'

while True:
    try:
        letter = input("Enter a letter: ").strip().lower()
    except EOFError:
        print("\nGoodbye.")
        break
    except KeyboardInterrupt:
        print("\nGoodbye.")
        break

    if letter == 'stop':
        print("Goodbye.")
        break
    if len(letter) != 1:
        print("Please enter a single letter.")
        continue
    if letter not in alphabet:
        print("Please enter a letter from the English alphabet.")
        continue

    pos = alphabet.index(letter) + 1
    print(f"'{letter}' is the {ordinal(pos)} letter of the alphabet.")
