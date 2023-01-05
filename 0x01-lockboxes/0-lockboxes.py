#!/usr/bin/python3
"""
Lockbox - all box
"""


def canUnlockAll(boxes):
    unlocked_boxes = [False] * len(boxes)  # set unlock all boxes to False
    unlocked_boxes[0] = True  # first box is always unlocked
    taskes = [0]

    while taskes:  # add or remove task while taskes in not completed
        boxe = taskes.pop()  # get a next boxe
        for key in boxes[boxe]:  # for all key insides current box
            if not unlocked_boxes[key]:  # if box is not unlocked yet
                unlocked_boxes[key] = True
                taskes.append(key)
    return all(unlocked_boxes)  # like a every method in javascript
