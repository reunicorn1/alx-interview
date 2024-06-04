#!/usr/bin/python3
"""
0. Lockboxes
"""
from queue import Queue


def canUnlockAll(boxes):
    """
    boxes (list): a list of lists for all boxes and their keys

    Returns true or false if all the boxes can be opened or not
    """
    if isinstance(boxes, list) and all(isinstance(sublist, list)
                                       for sublist in boxes):
        visited = set()
        q = Queue(maxsize=0)
        q.put(0)
        while not q.empty():
            value = q.get()
            if value < len(boxes) and value not in visited:
                for v in boxes[value]:
                    q.put(v)
                visited.add(value)
        return set(range(len(boxes))) == visited
