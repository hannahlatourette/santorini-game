class Position:

	def __init__(self, x, y):
		self.x_pos = x
		self.y_pos = y

	def __str__(self):
		return "position (%d, %d)" % (self.x_pos, self.y_pos)

	def __add__(self,other_pos):
		self.x_pos += other_pos.x_pos
		self.y_pos += other_pos.y_pos

	def __sub__(self,other_pos):
		x_res = self.x() - other_pos.x()
		y_res = self.y() - other_pos.y()

		return Position(x_res, y_res)

	def x(self):
		return self.x_pos

	def y(self):
		return self.y_pos		

class Space:

	def __init__(self, x, y):
		self.location = Position(x, y)
		self.level = 0
		self.occupied = False

	def __str__(self):
		if self.occupied:
			return "Occupied space at %s and building level %d" % (self.location, self.level)
		else:
			return "Unoccupied space at %s and building level %d" % (self.location, self.level)

	def build(self):
		if self.occupied:
			print("ERROR: Cannot build on an occupied space")
		elif self.level == 4:
			print("ERROR: Cannot build higher than 4 levels")
		else:
			self.level += 1

	def occupy(self):
		if self.occupied:
			print("ERROR: Cannot move to occupied space")
		else:
			self.occupied = True

	def leave(self):
		self.occupied = False

	def get_coords(self):
		return ( self.location.x(), self.location.y() )

	def get_loc(self):
		return self.location

	def get_level(self):
		return self.level

	def is_occupied(self):
		return self.occupied

class Board:

	def __init__(self, dimension):
		self.dim = dimension
		self.spaces = list()
		for i in range(self.dim):
			self.spaces.append(list())
			for j in range(self.dim):
				self.spaces[i].append(Space(j,i))

	def __str__(self):
		s = ''
		for i in range(self.dim):
			levels = [b.level for b in self.spaces[i]]
			s += str(levels)
			s += '\n'
		return s

	def get_dim(self):
		return self.dim

	def get_spaces(self):
		return self.spaces

	def get_space(self, x, y):
		if x < 0 or y < 0:
			print("ERROR: Attempt to access space above or to the left of board boundaries.")
			return False
		try:
			return self.spaces[y][x]
		except IndexError:
			print("ERROR: Attempt to access space below or to right of board boundaries.")
			return False

class Player:

	def __init__(self, name, piece1space, piece2space):
		self.name = name
		self.pieces = list()
		self.pieces.append(piece1space)
		self.pieces.append(piece2space)

	def __str__(self):
		return "Player %s has piece A at %s and piece B at %s" % (self.name, self.pieces[0].location, self.pieces[1].location)

	def get_pieces(self):
		return self.pieces

	def get_piece_space(self, piece_num):
		return self.pieces[piece_num]

	def move_piece(self, piece_num, new_space):
		self.pieces[piece_num] = new_space