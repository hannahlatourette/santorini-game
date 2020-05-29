from santorini_objects import *

class Game:

	def __init__(self, dimension, p1info, p2info):
		self.board = Board(dimension)
		self.players = list()
		p1a = self.board.get_space(p1info['pc1loc'])
		p1b = self.board.get_space(p1info['pc2loc'])
		p2a = self.board.get_space(p2info['pc1loc'])
		p2b = self.board.get_space(p2info['pc2loc'])
		self.players.append(Player(p1info['name'], p1a, p1b))
		self.players.append(Player(p2info['name'], p2a, p2b))
		self.turn = 0 # 0 = p1, 1 = p2

	def get_current_player(self):
		return self.players[self.turn]

	def next_turn(self):
		self.turn = 0 if self.turn == 1 else 1

	def valid_move(current_loc, new_loc):
		# move a max of one unit U/D and L/R
		diff = current_loc - new_loc
		if abs(diff.x) > 1 or abs(diff.y) > 1:
			print("ERROR: Piece can only move one unit vertically and/or horizontally per turn")
			return False
		# no pieces outside of board bounds
		try:
			new_space = self.board.get_space(new_loc)
		except IndexError:
			print("ERROR: Attempt to move to invalid board location")
			return False
		# no 2 pieces on same square
		if new_space.is_occupied():
			print("ERROR: There is already a piece at that spot!")
			return False
		# no pieces on crowned spaces
		if new_space.get_level() == 4:
			print("ERROR: A player cannot stand on a space which has been crowned!")
			return False
		# piece can only climb one level per turn
		if current_loc.get_level() < new_loc.get_level() - 1:
			print("ERROR: A piece can only climb one level per turn.")
			return False
		return True

	def move_piece(player, piece_num, current_space, new_space):
		if self.valid_move(current_space, new_space):
			player.move_piece(piece_num, new_space)
			current_loc.leave() # mark old space unoccupied
			new_loc.occupy() # mark new space occupied

	def valid_build(space):
		# cannot build on occupied space
		if new_space.is_occupied():
			print("ERROR: Cannot build on an occupied space!")
			return False
		# no pieces on crowned spaces
		if new_space.get_level() == 4:
			print("ERROR: This space has been crowned, no more room to build!")
			return False

	def build_level(space):
		if self.valid_build(space):
			space.build()
			