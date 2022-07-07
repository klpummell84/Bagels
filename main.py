import bagels

is_playing = True

bagels.intro_message()

while is_playing:
    secret_num = bagels.get_secret_number()
    print("I have thought of a number. You have %s guesses to get it." % bagels.MAX_GUESS)
    guesses = 1
    while guesses <= bagels.MAX_GUESS:
        guess = ''
        while len(guess) != bagels.NUM_DIGITS or not bagels.is_only_digits(guess):
            guess = input("Guess #%s: " % guesses)
        print(bagels.get_clues(guess, secret_num))
        guesses += 1

        if guess == secret_num:
            break
        if guesses > bagels.MAX_GUESS:
            print('You\'re all out of guesses. The answer was %s.' % secret_num)

    if not input("Would you like to play again? (Yes or No)").lower().startswith('y'):
        is_playing = False
