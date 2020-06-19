'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(string):
    if len(string) < 2:
        return 0
    if len(string) == 2:
        if string == 'th':
            return 1
        else:
            return 0
               
    return count_th(string[0:2]) + count_th(string[1:])
