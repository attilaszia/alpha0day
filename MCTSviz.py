import time
from anytree import Node, RenderTree


class MCTSviz():
    def __init__(self):
        self.base = Node("init")
        self.nodes = {}
        self.nodes["init"] = self.base

    def add_node(self, boardstr, parent):
        try:
            parent = self.nodes[parent]
        except KeyError:
            parent = self.base
        if (boardstr in self.nodes):
            pass
        else:
            node = Node(boardstr, parent=parent)
            self.nodes[boardstr] = node

    def show(self):
        for pre, fill, node in RenderTree(self.base):
            print("%s." % (pre))
        time.sleep(0.1)


#print(udo)
#print(joe)

#for pre, fill, node in RenderTree(udo):
#    print("%s%s" % (pre, node.name))

#print(dan.children)

        
