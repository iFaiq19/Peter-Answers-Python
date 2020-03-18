# Use , (comma) for getting the answer. Press , again after the completion of the answer to avoid getting an error.

import time
import sys
from msvcrt import getch

# This is the default string that will be printed when you will be writing the answer in petition column.
# If the length of the answer you store is geater than the default string you will get an error and program won't work.
default = 'Please answer my question'
answer = ''
i = 1

# To submit petition and question you always have to press enter.
print('Press \'ENTER\' key to submit your petition and your question.')
print('Hint >> Write \'Please answer my question\' in petition column')
print('Enter Your Petition Here: ', end='')
sys.stdout.flush()
while 1:
    x = getch()

    # For backspace key. This works even when you are writing the answer in the petition column.
    if ord(x) == 8:
        print('\b \b', end='')
        sys.stdout.flush()
        i -= 1

    # For enter key
    elif ord(x) == 13:
        break

    elif x.decode() != ',':
        print(x.decode(), end='')
        sys.stdout.flush()
        i += 1

    # For storing the answer
    elif x.decode() == ',':
        while x.decode() == ',':
            y = getch()
            print(default[i-1], end='')
            sys.stdout.flush()
            i += 1
            if y.decode() == ',':
                break
            else:
                answer = answer + y.decode()
print('')

# Question column
b = input('Ask Your Question: ')
if b == '' or b == ' ':
    print('Please ask a question.')
else:
    
    # Not necessary, if another person is using the program, he would not know how to store the answer and hence this will be printed.
    if answer == '':
        print('I only answer to my boss!'.upper())
    else:
        print('\nThinking your answer, wait a bit', end='')
        for i in range(4):
            print('.', end='')
            sys.stdout.flush()
            time.sleep(1)
        print('')
        print('\nThe Answer to Your Question Is: ', answer.title())
