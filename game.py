from santorini_objects import *

class Game:

	def __init__(self, dimension, p1, p1pc, p2, p2pc):
		self.board = Board(dimension)
		self.players = list()
		# initial places of each board piece
		p1a = self.board.get_space(p1pc[0][0], p1pc[0][1])
		p1b = self.board.get_space(p1pc[1][0], p1pc[1][1])
		p2a = self.board.get_space(p2pc[0][0], p2pc[0][1])
		p2b = self.board.get_space(p2pc[1][0], p2pc[1][1])
		# occupy these spaces
		p1a.occupy()
		p1b.occupy()
		p2a.occupy()
		p2b.occupy()

		# make players
		self.players.append(Player(p1, p1a, p1b))
		self.players.append(Player(p2, p2a, p2b))
		self.turn = 0 # 0 = p1, 1 = p2

	def get_current_player(self):
		return self.players[self.turn]

	def get_player(self, player_num):
		return self.players[player_num]

	def get_players(self):
		return self.players

	def get_piece_locs(self):
		# return a flat list of each piece location
		# [p1p1, p1pc2, p2pc1, p2pc2]
		players = self.get_players()
		pieces = list()
		for p in players:
			for l in p.get_pieces():
				pieces.append( (l.get_loc().x(), l.get_loc().y()) )
		print(pieces)
		return pieces

	def next_turn(self):
		self.turn = 0 if self.turn == 1 else 1

	def valid_move(self, current_space, new_space):
		# move a max of one unit U/D and L/R
		diff = current_space.get_loc() - new_space.get_loc()
		if abs(diff.x()) > 1 or abs(diff.y()) > 1:
			print("ERROR: Piece can only move one unit vertically and/or horizontally per turn")
			return False
		# no pieces outside of board bounds

		# no 2 pieces on same square
		if new_space.is_occupied():
			print("ERROR: There is already a piece at that spot!")
			return False
		# no pieces on crowned spaces
		if new_space.get_level() == 4:
			print("ERROR: A player cannot stand on a space which has been crowned!")
			return False
		# piece can only climb one level per turn
		if current_space.get_level() < new_space.get_level() - 1:
			print("ERROR: A piece can only climb one level per turn.")
			return False
		return True

	def move_piece(self, player, piece_num, new_x, new_y):
		current_space = player.get_piece_space(piece_num)
		try:
			new_space = self.board.get_space(new_x, new_y)
		except IndexError:
			print("ERROR: Attempt to move to invalid board location")
			return False		
		if self.valid_move(current_space, new_space):
			player.move_piece(piece_num, new_space)
			current_space.leave() # mark old space unoccupied
			new_space.occupy() # mark new space occupied

	def valid_build(self, new_space):
		# cannot build on occupied space
		if new_space.is_occupied():
			print("ERROR: Cannot build on an occupied space!")
			return False
		# no pieces on crowned spaces
		if new_space.get_level() == 4:
			print("ERROR: This space has been crowned, no more room to build!")
			return False
		return True

	def build_level(self, x, y):
		space = self.board.get_space(x, y)
		if self.valid_build(space):
			space.build()

	def __str__(self):

		dim = self.board.get_dim()
		players = self.get_piece_locs()
		spaces  = self.board.get_spaces()

		# standard strings to print pieces of board
		player_labels   = ['  P1A  ','  P1B  ','  P2A  ','  P2B  ']
		space_labels = ['       ',' * * * ','  * *  ','   *   ']
		blank_space   = '       '
		full_space = '   X   '
		row_line = '-'*8*dim + '-'


		for board_row in range(self.board.get_dim()):
			print(row_line)

			# print location of each of the 4 players
			player_str = '|'
			for board_col in range(dim):
				if (board_row, board_col) in players:
					player_num = players.index((board_row,board_col))
					player_str += player_labels[player_num]
				# print X for full space to show player cannot move here
				elif spaces[board_row][board_col].get_level() == 4:
					player_str += full_space
				else:
					player_str += blank_space
				player_str += '|'
			print(player_str)

			# print buildings on each space
			top_row = '|'
			mid_row = '|'
			low_row = '|'
			space_row = spaces[board_row]
			tmp = [x.get_level() for x in space_row]
			for board_col in range(dim):
				# form top row
				top_row += space_labels[3] if space_row[board_col].get_level() >= 3 else blank_space
				top_row += '|'
				# form mid row
				mid_row += space_labels[2] if space_row[board_col].get_level() >= 2 else blank_space
				mid_row += '|'
				# form bottom row	
				low_row += space_labels[1] if space_row[board_col].get_level() >= 1 else blank_space
				low_row += '|'		
			print(top_row)
			print(mid_row)
			print(low_row)

		print (row_line)
		return ''