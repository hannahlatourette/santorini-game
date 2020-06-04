from santorini_objects import *
from game import *

# Create game
p1 = 'Hannah'
p1pc  = [(1,2), (2,2)]
p2 = 'Andrew'
p2pc  = [(2,3), (3,3)]
G = Game(5, p1, p1pc, p2, p2pc)

# Test move validation
p1 = G.get_current_player()
G.next_turn()
p2 = G.get_current_player()
print(p1)
print(p2)
print(G)
G.move_piece(p1, 0, 2, 2)
print(G)
G.move_piece(p1, 0, 4, 4)
print(G)
G.move_piece(p1, 0, 1, 1)
print(G)
G.build_level(0, 1)
G.build_level(0, 1)
G.build_level(0, 1)
G.build_level(0, 1)
G.move_piece(p1, 0, 0, 1)
print(G)