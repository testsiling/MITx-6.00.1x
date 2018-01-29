'''
MIT 6.00.1x Week 3 Problem set: Hangman
Problem 4
'''
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    counter = 8
    lettersGuessed = []
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is %d letters long." % len(secretWord))
    print("-------------")

    while counter > 0:
        print("You have %d guesses left." % counter)
        print("Available letters: %s" % getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")

        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: %s" % getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guess)

            if guess in getGuessedWord(secretWord, lettersGuessed):
                print("Good guess: %s" % getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word: %s" % getGuessedWord(secretWord, lettersGuessed))
                counter -= 1

        print("------------")
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break

    if counter <= 0:
        print("Sorry, you ran out of guesses. The word was else.")
        print("My secret word is %s" % secretWord)


