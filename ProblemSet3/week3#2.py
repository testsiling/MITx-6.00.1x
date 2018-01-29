'''
MIT 6.00.1x Week 3 Problem set: Hangman
Problem 2
'''
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    res = []
    for i in range(len(secretWord)):
        res.append('_')

    for w in lettersGuessed:
        
        # if w is character in secret word
        if w in secretWord:
            
            for i in range(len(res)):
                
                # get all index of w
                if secretWord[i] == w:
                    res[i] = w

    return ' '.join(res)
