import random as r

NUM_DIGITS = 3
MAX_GUESS = 10

def get_secret_number():
    """Returns a string of unique random digits that is NUM_DIGITS long."""
    numbers = list(range(10))
    r.shuffle(numbers)
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num

def get_clues(guess: str, secret_num: str):
    """Returns a string with the Pico, Fermi, & Bagels clues to the user."""
    if guess == secret_num:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)

def is_only_digits(num: str):
    """Returns True if num is only digits and NOT an empty string. Otherwise, returns False."""
    if num == '' or None:
        return False

    for i in num:
        if i not in '0,1,2,3,4,5,6,7,8,9'.split(','):
            return False

    return True

def intro_message():
    print("I am thinking of a %s-digit number. Try to guess what it is." % NUM_DIGITS,
          "\nWhen I say:       That means:\n"
          "    Bagels           None of the digits is correct.\n"
          "    Pico             One digit is correct but is in the wrong position.\n"
          "    Fermi            One digit is correct and is in the right position.")
