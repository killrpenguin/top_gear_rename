import os
from os.path import isdir

# if the repl changes dir, it affects the project. Reset repl before testing.


visited = []
queue = []

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.cwd = os.getcwd()
        self.root = None

 
    @property
    def key(self) -> int:
        try:
            return len(os.listdir(self.cwd))
        except NotADirectoryError:
            return 0

    
    def set_root(self):
        return setattr(self, "root", os.getcwd())


def explore_node(visited, queue):
    node = Node()
    if len(visited) == 0 and len(queue) == 0:
       node.set_root()


