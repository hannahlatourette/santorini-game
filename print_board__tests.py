import print_board as pb
import numpy as np

'''
This code tests the print_board function (and
valid_board function called within it) to 
ensure no valid boards can be printed
'''

if __name__ == '__main__':
	buildings = np.asarray([[2,1,0,0,3],
						    [4,2,0,0,0],
						    [3,2,0,1,0],
						    [0,2,0,0,2],
						    [3,0,1,0,4]])
	players = [(0,0),(1,2),(4,2),(3,3)]
	
	# valid board
	print "======================================"
	print "VALID BOARD: "
	pb.print_board(buildings, players, len(buildings))
	print

	# players on same square
	print "======================================"
	print "MULTIPLE PLAYERS ON SAME SQUARE: "
	players[1] = (0,0)
	pb.print_board(buildings, players, len(buildings))
	print
	players = [(0,0),(1,2),(4,2),(3,3)] # change back	

	# board with negative level
	print "======================================"
	print "NEGATIVE LEVEL BOARD:"
	buildings[0][2] -= 1
	pb.print_board(buildings, players, len(buildings))
	print
	buildings[0][2] += 1 # change back

	# board with over-built building
	print "======================================"
	print ">4 LEVEL BOARD:"
	buildings[3][4] += 5
	pb.print_board(buildings, players, len(buildings))
	print
	buildings[3][4] -= 5 # change back

	# players out of bounds
	print "======================================"
	print "PLAYERS OUT OF BOUNDS:"
	# x low, P1A
	players[0] = (-1,2)
	pb.print_board(buildings, players, len(buildings))
	players = [(0,0),(1,2),(4,2),(3,3)] # change back
	print
	# x high, P1B
	players[1] = (5,2)
	pb.print_board(buildings, players, len(buildings))
	players = [(0,0),(1,2),(4,2),(3,3)] # change back
	print
	# y low, P2A
	players[2] = (2,-1)
	pb.print_board(buildings, players, len(buildings))
	players = [(0,0),(1,2),(4,2),(3,3)] # change back
	print
	# y high, P2B
	players[3] = (2,5)
	pb.print_board(buildings, players, len(buildings))
	players = [(0,0),(1,2),(4,2),(3,3)] # change back
	print