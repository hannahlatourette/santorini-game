import numpy as np

def valid_board(buildings,players,dim):
	print "valid"


def print_board(buildings,players,dim):
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

buildings = np.asarray([[2,1,0,0,3],
					    [4,2,0,0,0],
					    [3,2,0,1,0],
					    [0,2,0,0,2],
					    [3,0,1,0,4]])

print_board(buildings,[(0,0),(1,2),(4,2),(3,3)],len(buildings))