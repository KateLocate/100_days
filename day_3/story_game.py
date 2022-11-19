from scenario import SCENARIO


class Node:
    def __init__(self, position, left, right, text):
        self.position = position
        self.left = left
        self.right = right
        self.text = text
