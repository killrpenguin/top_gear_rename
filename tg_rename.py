import os
from os.path import isdir


class Graph_Traversal:
    def __init__(self) -> None:
        self.visited = []
        self.stack = []
        self.stop_recursion = False


class Node:
    def __init__(self, name="Top_Gear") -> None:
        """
        Name: The name of the file or folder the node represents.

        Root: Root directory of the file structure being traversed.
        
        Loc: Location within the tree of the structure being traversed.

        is_file: Property for destinguishing files from folders.

        set_root: Property for managing the repl's cwd.
            This should always be the same. /home/david/Videos/Top_Gear

        children: List of child items to be converted to nodes.
        """

        
        self.name = name
        self.root = None
        if self.name != "Top_Gear":
            self.loc = f'{os.getcwd()}/{self.name}'
        else:
            self.loc = os.getcwd()

    @property
    def is_file(self) -> bool:
         return os.path.isfile(f'{self.loc}')

        
    def set_root(self) -> None:
        setattr(self, "root", os.getcwd())


    @property
    def children(self) -> list:
        children = [a for a in os.listdir(self.loc) if os.path.isdir(a) is True and "Season" in a]
        if len(children) == 0:
            children = [a for a in os.listdir(self.loc) if ".vsmeta" not in a]
        return children

    def rename_file(self) -> None:
        try:
            print(f'os.rename(src:{self.loc}, dst: new_name_Dict)')
        except NotADirectoryError:
           print("test") 



def explore_node(traversal_object):
    print("a")
    if traversal_object.stop_recursion is True:
        return
    
    if len(traversal_object.visited) == 0:
        traversal_object.stack.append(Node())
        traversal_object.stack[0].set_root()

    node = traversal_object.stack.pop()

    traversal_object.visited.append(node)
####################
    os.chdir(node.loc)
####################    
    for name in node.children:
        traversal_object.stack.append(Node(name))
        print(name)

    if node.is_file is True:
        node.rename_file()

    if len(traversal_object.stack) == 0:
        setattr(traversal_object, "stop_recursion", True)
    else:
        explore_node(traversal_object=traversal_object)
       


prog = Graph_Traversal()
explore_node(prog)
