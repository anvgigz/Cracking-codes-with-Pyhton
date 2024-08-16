 # Transposition Cipher Encrypt/Decrypt File
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import time, os, sys, TranspositionEncrypt, TranspositionDecrypt

def main():
    inputFilename = 'whatyourencrypting.txt' #include filepath
    #Be ecareful! if afile with output filename name already exists,
    #This program will overwrite that file:
    outputFilename = 'whatyourencrypting.encrypted.txt' #output new file name of encrypted file
    myKey = 10
    myMode = 'encrypt' # Set to 'encrypt' or 'decrypt'

    # If the input file does not exist, the program terminates early:
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    # If the output file already exists, give the user a chance to quit:
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # Read in the message from the input file:
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    #Measure how long the encryption/decryption takes:
    startTime = time.time()
    if myMode == 'encrypt':
        translated = TranspositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = TranspositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    # Write out the translate message to the output file:
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, outputFilename,
                                              len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))



# If transpositionCipherFile.py is run (instead of imported as a module),
# call the main() function:
if __name__ == '__main__':
    main()