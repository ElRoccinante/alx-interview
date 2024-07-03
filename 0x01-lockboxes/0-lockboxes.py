#!/usr/bin/python3
"""
0x01. Lockboxes
"""


def canUnlockAll(boxes):
    """A function that determines if all the boxes can be opened."""
    unlocked_boxes = {0}  # Start with box 0 unlocked
    prev_count = 0

    while len(unlocked_boxes) > prev_count:
        prev_count = len(unlocked_boxes)

        for box in unlocked_boxes.copy():
            unlocked_boxes.update(boxes[box])

    return len(unlocked_boxes) == len(boxes)
