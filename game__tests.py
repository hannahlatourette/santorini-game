from santorini_objects import *
from game import *

# # Create game
# p1 = 'Hannah'
# p1pc  = [(1,2), (2,2)]
# p2 = 'Andrew'
# p2pc  = [(2,3), (3,3)]
# G = Game(5, p1, p1pc, p2, p2pc)
# p1 = G.get_current_player()
# p2 = G.get_current_player()

# # Test move validation
# G.next_turn()
# print(p1)
# print(p2)
# print(G)
# G.move_piece(p1, 0, 2, 2)
# print(G)
# G.move_piece(p1, 0, 4, 4)
# print(G)
# G.move_piece(p1, 0, 1, 1)
# print(G)
# G.build_level(0, 1)
# G.build_level(0, 1)
# G.build_level(0, 1)
# G.build_level(0, 1)
# G.move_piece(p1, 0, 0, 1)
# print(G)

# Create game
p1 = 'Hannah'
p1pc  = [(1,1), (1,3)]
p2 = 'Andrew'
p2pc  = [(3,1), (3,3)]
G = Game(5, p1, p1pc, p2, p2pc)
p1 = G.get_current_player()
G.next_turn()
p2 = G.get_current_player()

print(G)

# Test build validation
# cannot build on current space
G.build_level(p1, 0, 1, 1)
print(G)
# cannot build more than 1,1 space away
G.build_level(p2, 1, 0, 0)
print(G)
# cannot build on occupied space
G.move_piece(p2, 0, 3, 2)
G.build_level(p2, 1, 3, 2)
print(G)
# cannot build higher than 4 levels
for i in range(5):
	G.build_level(p2, 0, 2, 2)
print(G)