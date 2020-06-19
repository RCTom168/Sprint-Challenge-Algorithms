'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# def count_th(word):
def count_th(word, count = 0):
    
    # TBC
    # Establish the Base Case: A word must have 2 or more letters
    if len(word) < 2:
        return count

    # Else, if a word is greater than or equal to 2
    # Check the first two letters of a word for 'th'
    elif word[0:2] == 'th':
        # Use recursion to slice the first 2 letters off the word & count each occurrence of 'th'
        return count_th(word[1:], count) + 1
    else:
        # Runs the function again, but without the first letter
        return count_th(word[1:], count)

# Should only be 3 since case matters
print(count_th('ThisandthatTheseandthoseThanandthen'))