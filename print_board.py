import numpy as np

def valid_board(buildings,players,dim):
	''' verifies current board is valid according to 
		logistics and game rules '''
	player_names = {0:"P1A", 1:"P1B", 2:"P2A", 3:"P2B"}
	
	# no players on same square
	if len(players) > len(set(players)):
		print "ERROR: Two players cannot be on the same square!"
		return False
	# no players outside of board bounds
	for i,(x,y) in enumerate(players):
		if x < 0 or x > dim-1 or y < 0 or y > dim-1:
			print "ERROR: Player",player_names[i],"moved out of the bounds of the board."
			return False
	# no players on capped buildings
	for loc in players:
		if buildings[loc[0]][loc[1]] == 4:
			print "ERROR: A player cannot stand on a building which has been crowned!"
			return False
	# building size valid
	for row in buildings:
		for building in row:
			if building < 0:
				print "ERROR: Building cannot be at level lower than 0."
				return False
			if building > 4:
				print "ERROR: The maximum level of a building is 4."
				return False
	return True

def print_board(buildings,players,dim):
	''' print current status of board as grid '''

	# check that board is valid before printing
	if not valid_board(buildings,players,dim):
		print "Cannot print board."
		return False

	# standard strings to print pieces of board
	player_labels   = ['  P1A  ','  P1B  ','  P2A  ','  P2B  ']
	building_labels = ['       ',' * * * ','  * *  ','   *   ']
	blank_space   = '       '
	full_building = '   X   '
	row_line = '-'*8*dim + '-'

	for board_row in range(dim):
		print row_line

		# print location of each of the 4 players
		player_str = '|'
		for board_col in range(dim):
			if (board_row,board_col) in players:
				player_num = players.index((board_row,board_col))
				player_str += player_labels[player_num]
			# print X for full building to show player cannot move here
			elif buildings[board_row][board_col] == 4:
				player_str += full_building
			else:
				player_str += blank_space
			player_str += '|'
		print player_str

		# print current building sizes
		top_row = '|'
		mid_row = '|'
		low_row = '|'
		building_row = buildings[board_row]
		for board_col in range(dim):
			# form top row
			top_row += building_labels[3] if building_row[board_col] >= 3 else blank_space
			top_row += '|'
			# form mid row
			mid_row += building_labels[2] if building_row[board_col] >= 2 else blank_space
			mid_row += '|'
			# form bottom row	
			low_row += building_labels[1] if building_row[board_col] >= 1 else blank_space
			low_row += '|'		
		print top_row
		print mid_row
		print low_row

	print row_line