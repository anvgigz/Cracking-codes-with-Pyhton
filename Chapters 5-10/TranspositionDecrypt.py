# Transposition Cipher Decryption
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey,myMessage)

    #Print with a | (called "Pipe" Character) after it in case 
    # There are a spaces at the end of the decrypt message:
    print(plaintext + '|')

    pyperclip.copy(plaintext)


def decryptMessage(key, message):
    #The tranposition decrypt function will simulate the "columns" and
    #"rows" of the grid that the plaintext is written on by using a list
    # of strings. First we need to calculate a few values.

    #The number of "columns" in our transposition grid:
    numOfColumns = int(math.ceil(len(message) / float(key))) 
    #The number of "rows' in our grid:
    numOfRows = key
    #The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    #Each string in plaintext represents a column in the grid:
    plaintext = [''] * numOfColumns

    #The column and row variables point to where in the grid the next
    #Character in the encrypted message will go:
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # Point to the next column.

    #If there are no more columns OR we're at a shaded box, go back
    # To the first column and the next reow:
        if (column == numOfColumns) or (column == numOfColumns -1 and
                                        row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)

#If transpositionDecrypt.py is run  (instead of imported as a module),
#call the main() function:
if __name__ == '__main__':
    main()