def ordinal(n):
    if 11 <= n <= 13:
        return str(n) + 'th'
    if n % 10 == 1:
        return str(n) + 'st'
    if n % 10 == 2:
        return str(n) + 'nd'
    if n % 10 == 3:
        return str(n) + 'rd'
    return str(n) + 'th'

alphabet = 'abcdefghijklmnopqrstuvwxyz'

while True:
    letter = input("Enter a letter: ").strip().lower()
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
