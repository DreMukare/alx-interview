#!/usr/bin/python3
'''determines if a given data set represents a valid utf-8 encoding'''

def validUTF8(data):
    # number of bytes
    numberOfBytes = 0

    # looping through dataset
    for num in data:
        # get binary representation
        # get least significant 8-bits
        binaryRepresentation = format(num, '#010b')[-8:]

        # if no bytes then process new utf-8 character
        if numberOfBytes == 0:
            # get number of 1s at beginning of string
            for bit in binaryRepresentation:
                if bit == '0': break
                numberOfBytes += 1

            if numberOfBytes == 0:
                continue

            if numberOfBytes == 1 or numberOfBytes > 4:
                return False

        else:
            if not (binaryRepresentation[0] == '1' and binaryRepresentation[1] == '0'):
                return False

        numberOfBytes -= 1

    return numberOfBytes == 0
