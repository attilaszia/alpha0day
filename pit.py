import Arena
from MCTS import MCTS
from tictactoe.TicTacToeGame import TicTacToeGame
from tictactoe.keras.NNet import NNetWrapper as NNet
from tictactoe.TicTacToePlayers import HumanTicTacToePlayer
#from othello.OthelloGame import OthelloGame
#from othello.OthelloPlayers import *
#from othello.pytorch.NNet import NNetWrapper as NNet


import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""

mini_othello = False  # Play in 6x6 instead of the normal 8x8.
human_vs_cpu = False

#if mini_othello:
#    g = OthelloGame(6)
#else:
#    g = OthelloGame(8)

g = TicTacToeGame()

# all players
#rp = RandomPlayer(g).play
#gp = GreedyOthelloPlayer(g).play
hp = HumanTicTacToePlayer(g).play

class MctsPlayer:
    def __init__(self, mcts):
        self.mcts = mcts

    def play(self, x):
        return np.argmax(self.mcts.getActionProb(x, temp=0))

    def reset(self):
        self.mcts.reset()



# nnet players
n1 = NNet(g)
n1.load_checkpoint('./temp','best.pth.tar')

#if mini_othello:
#    n1.load_checkpoint('./pretrained_models/othello/pytorch/','6x100x25_best.pth.tar')
#else:
#    n1.load_checkpoint('./pretrained_models/othello/pytorch/','8x8_100checkpoints_best.pth.tar')
args1 = dotdict({'numMCTSSims': 3, 'cpuct':1.0})
mcts1 = MCTS(g, n1, args1, vizshow = False)
#n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))
n1p = MctsPlayer(mcts1)

if human_vs_cpu:
    player2 = hp
else:
    n2 = NNet(g)
    n2.load_checkpoint('./temp', 'best.pth.tar')
    args2 = dotdict({'numMCTSSims': 9, 'cpuct': 1.0})
    mcts2 = MCTS(g, n2, args2, vizshow = True)
    n2p = MctsPlayer(mcts2)
    #n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

    player2 = n2p  # Player 2 is neural network if it's cpu vs cpu.

arena = Arena.Arena(n1p, player2, g, display=TicTacToeGame.display)

print(arena.playGames(10, verbose=True))
