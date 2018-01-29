'''
MIT 6.00.1x Week 3 Problem set: Hangman
Problem 1: 
'''
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    word_dict = {}
    for w in secretWord:
        word_dict[w] = 0

    for w in lettersGuessed:
        if w in secretWord:
            word_dict[w] = 1

    if 0 in word_dict.values():
        return False
    else:
        return True
