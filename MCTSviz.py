import time
from anytree import AnyNode, RenderTree


class MCTSviz():
    def __init__(self):
        self.base = AnyNode(id="init", mctsn=0)
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
            node = AnyNode(id=boardstr, parent=parent, mctsn=0)
            self.nodes[boardstr] = node

    def update_data(self, Ns):
        for s in Ns:
            try:
                self.nodes[s].mctsn = Ns[s]
            except KeyError:
                pass

    def show(self, Ns):
        self.update_data(Ns)
        for pre, fill, node in RenderTree(self.base):
            print("%s %s" % (pre, node.mctsn))
        time.sleep(0.1)


#print(udo)
#print(joe)

#for pre, fill, node in RenderTree(udo):
#    print("%s%s" % (pre, node.name))

#print(dan.children)

        
