#!/usr/bin/python3
"""
Module that determines if all lockboxes can be unlocked.
"""

def canUnlockAll(boxes: list):
    """
    Determine if all boxes can be unlocked.
    
    Args:
        boxes (list): A list of lists, where each sublist contains keys 
                      to other boxes.
    
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """

    # Start with Box 0 unlocked
    unlocked = {0}

    # Collect the keys from Box 0
    stack = boxes[0].copy()

    # Process the keys in the stack
    while stack:
        # Get a key from the stack
        key = stack.pop()

        # Check if the key corresponds to a valid, unopened box
        if key < len(boxes) and key not in unlocked:
            # Unlock the box
            unlocked.add(key)
            
            # Collect all keys from the unlocked box
            stack.extend(boxes[key])

    # Check if all boxes have been unlocked
    return len(unlocked) == len(boxes)
