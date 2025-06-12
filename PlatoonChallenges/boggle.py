"""
Each player searches for words that fit the following criteria:

Words must be at least three letters in length.
Each letter after the first must be a horizontal, vertical, or diagonal neighbor of the one before it.
No individual letter cube may be used more than once in a word.
No capitalized or hyphenated words are allowed.
"""

import random
import string


class BoggleBoard():

    def die(self):
        boggle_dice = {
            1: 'AAEEGN',
            2: 'ELRTTY',
            3: 'AOOTTW',
            4: 'ABBJOO',
            5: 'EHRTVW',
            6: 'CIMOTU',
            7: 'DISTTY',
            8: 'EIOSST',
            9: 'DELRVY',
            10: 'ACHOPS',
            11: 'HIMNQU',
            12: 'EEINSU',
            13: 'EEGHNW',
            14: 'AFFKPS',
            15: 'HLNNRZ',
            16: 'DEILRX'
        }
        line_1 = ''.join(random.choice(boggle_dice[random.randint(1, 16)])for i in range(4))
        line_2 = ''.join(random.choice(boggle_dice[random.randint(1, 16)])for i in range(4))
        line_3 = ''.join(random.choice(boggle_dice[random.randint(1, 16)])for i in range(4))
        line_4 = ''.join(random.choice(boggle_dice[random.randint(1, 16)])for i in range(4))
        
        print(f'{line_1},\n {line_2},\n {line_3},\n {line_4}')


    #This shows the empty game upon initialization
    initialize = {
        'line1': '____',
        'line2': '____',
        'line3': '____',
        'line4': '____'
    }
    for x, y in initialize.items():
        print(y)

    # def shake(self):
        
        # output = {
        #     'line1': ''.join(random.choice(characters) for i in range(4)),
        #     'line2': ''.join(random.choice(characters) for i in range(4)),
        #     'line3': ''.join(random.choice(characters) for i in range(4)),
        #     'line4': ''.join(random.choice(characters) for i in range(4))
        # }
        # return (output.values, characters)
        # for x, y in output.items():
        #     print(y)


x = BoggleBoard()
x.die()