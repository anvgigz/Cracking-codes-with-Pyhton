# Transposition Cipher Test
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import random, sys, TranspositionEncrypt, TranspositionDecrypt

## how to generate truly random numbers -- random.SystemRandom().randint()
def main():
    random.seed(42) # set the random "seed" to a static value.

    for i in range(20): # Run 20 tests.
        #Generate random messages to test.

        # The message will have a random length:
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # Convert the message string to a list to shuffle it:
        message = list(message)
        random.shuffle(message)
        message = ''.join(message) #Convert the list back to a string

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        # Check all possible keys for each message:
        for key in range(1, int(len(message)/2)):
            encrypted = TranspositionEncrypt.encryptMessage(key, message)
            decrypted = TranspositionDecrypt.decryptMessage(key, encrypted)

            # If the decrypted doesn't match the original message, display
            #an error message and quit:
            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('Tranposition cipher passed.')

# If transpositiontestprogram.py is run  (instead of imported as a module) call
# The main function:
if __name__ == '__main__':
    main()
                      
                      
