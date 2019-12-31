import random

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""
    # make sure guess is within range
    assert 0 < val < 101, "Val must be between 1-100"

    # set initial variables
    num_guesses = 0

    minimun = 0 

    maximum = 101

    guess = None

    # while guess is incorrect 
    while guess != val: 

        # add to num guesses
        num_guesses += 1

        # update guess 
        guess = (maximum - minimun) // 2 + minimun
        
        # reset min and max based on guess
        if guess < val:

            minimun = guess

        elif guess > val:

            maximum = guess

        
        

    return num_guesses