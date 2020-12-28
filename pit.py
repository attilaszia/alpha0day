import Arena
import DiffArena
from MCTS import MCTS
from MCTSPlayer import MctsPlayer
from tictactoe.TicTacToeGame import TicTacToeGame
from tictactoe.keras.NNet import NNetWrapper as NNet
from tictactoe.TicTacToePlayers import HumanTicTacToePlayer
import os

#from othello.OthelloGame import OthelloGame
#from othello.OthelloPlayers import *
#from othello.pytorch.NNet import NNetWrapper as NNet


import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""

os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

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

# nnet players
n1 = NNet(g)
n1.load_checkpoint('./temp','best.pth.tar')

#if mini_othello:
#    n1.load_checkpoint('./pretrained_models/othello/pytorch/','6x100x25_best.pth.tar')
#else:
#    n1.load_checkpoint('./pretrained_models/othello/pytorch/','8x8_100checkpoints_best.pth.tar')
args1 = dotdict({'numMCTSSims': 6, 'cpuct':1.0, 'color':'blue'})
mcts1 = MCTS(g, n1, args1, vizshow = True)
#n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))
n1p = MctsPlayer(mcts1)


nw = NNet(g)
nw.load_checkpoint('./temp','best.pth.tar')
args_w = dotdict({'numMCTSSims': 6, 'cpuct':1.0, 'color':'blue'})
mcts_w = MCTS(g, nw, args_w, vizshow = False)
#n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))
w_p = MctsPlayer(mcts_w)

if human_vs_cpu:
    player2 = hp
else:
    n2 = NNet(g)
    n2.load_checkpoint('./temp', 'best.pth.tar')
    args2 = dotdict({'numMCTSSims': 9, 'cpuct': 1.0, 'color':'green'})
    mcts2 = MCTS(g, n2, args2, vizshow = True)
    n2p = MctsPlayer(mcts2)
    #n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

    player2 = n2p  # Player 2 is neural network if it's cpu vs cpu.

arena = DiffArena.DiffArena(n1p, player2, w_p, g, display=TicTacToeGame.display)
print(arena.playGames(2, verbose=True))
