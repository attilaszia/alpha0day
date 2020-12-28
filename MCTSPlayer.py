import numpy as np

class MctsPlayer:
    def __init__(self, mcts):
        print("MCTS initialized with %s" % mcts)
        self.mcts = mcts

    def play(self, x):
        return np.argmax(self.mcts.getActionProb(x, temp=0))

    def reset(self):
        self.mcts.reset()

