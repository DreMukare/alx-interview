#!/usr/bin/python3
'''
module contains solution to lockboxes problem
'''


def canUnlockAll(boxes):
    '''
        function to check whether every box within boxes can be unlocked
        parameters:
            @boxes(list): list that contains all boxes
        return:
            true if all boxes can be opened
            false if not all boxes can be opened
    '''
    if not boxes:
        return False

    unlocked = [0]

    for i in range(1, len(boxes)):
        j = 0
        while j < len(boxes):
            if i in boxes[j] and i != j:
                unlocked.append(i)
            j += 1

    unlocked = list(set(unlocked))
    return True if len(unlocked) == len(boxes) else False
