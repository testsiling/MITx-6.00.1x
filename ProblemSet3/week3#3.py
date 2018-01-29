'''
MIT 6.00.1x Week 3 Problem set: Hangman
Problem 3
'''
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    res = list(letters)

    for w in lettersGuessed:
        if w in letters:
            res.remove(w)

    return ''.join(res)

