#!/usr/bin/python3
"""LOCKED"""

def canUnlockAll(boxes):
    """
    Check if it's possible to unlock all the boxes based on a set of keys.

    Parameters:
    - boxes (List[List[int]]): A list of lists.

    Returns:
    - bool: True if all boxes can be unlocked, False otherwise.
    """
    total_boxes = len(boxes)
    keys = [0]
    count = 0
    queue = 0

    while queue < len(keys):
        setkey = keys[queue]
        for key in boxes[setkey]:
            if 0 < key < total_boxes and key not in keys:
                keys.append(key)
                count += 1
        queue += 1

    return count == total_boxes - 1
