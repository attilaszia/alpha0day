import time
from anytree import AnyNode, RenderTree


class MCTSviz():
    def __init__(self):
        self.base = AnyNode(id="init", mctsn=0, action=None)
        self.nodes = {}
        self.nodes["init"] = self.base
        self.Nsa = None

    def add_node(self, boardstr, parent, a):
        try:
            parent = self.nodes[parent]
        except KeyError:
            parent = self.base
        if (boardstr in self.nodes):
            pass
        else:
            node = AnyNode(id=boardstr, parent=parent, mctsn=0, action=a)
            self.nodes[boardstr] = node

    def rebase(self, s):
        for child in self.base.children:
            #print("%s should be removed" % child.action)
            child.parent = None

    def update_data(self, Ns, Nsa):
        self.Nsa = Nsa
        for s in Ns:
            try:
                self.nodes[s].mctsn = Ns[s]
            except KeyError:
                pass

    def show(self, Ns, Nsa, s):
        self.update_data(Ns, Nsa)
        if s in self.nodes:
            root = self.nodes[s]
        else:
            root = self.base
        for pre, fill, node in RenderTree(root):
            try:
                print("%s n:%s nsa:%s a:%s" % (pre, node.mctsn, self.Nsa[(node.parent.id,node.action)],node.action))
            except AttributeError:
                print("%s %s a:%s" % (pre, node.mctsn, node.action))
                pass
            except KeyError:
                print("%s %s a:%s" % (pre, node.mctsn, node.action))
                pass
        time.sleep(0.1)


#print(udo)
#print(joe)

#for pre, fill, node in RenderTree(udo):
#    print("%s%s" % (pre, node.name))

#print(dan.children)

        
