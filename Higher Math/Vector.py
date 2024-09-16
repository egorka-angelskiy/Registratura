from utils import *

class Vector:

	def __init__(self, coords: list | set | tuple=None) -> None:
		if coords:
			#if len(coords) > 3:
			#	raise Exception('Плохие данные!')

			condition_row: list[list[int | float]] = [isinstance(coord, list) for coord in coords]
			condition_col: list[int | float] = [isinstance(coord, int) or isinstance(coord, float) for coord in coords]
			
			if not (all(condition_row) or all(condition_col)):
				raise Exception('Плохие данные!')
			
			self.row: int = sum(condition_row) if sum(condition_row) > 0 else sum(condition_row) + 1
			self.col: int = sum(condition_col) if sum(condition_col) > 0 else sum(condition_col) + 1
			self.coords: list[list[int | float] | int | float] = list(coords)
			self.type_: str = 'v' if self.row > self.col else 'h'
			self.mod: int | float = sum([self.coords[0][i] ** 2 if self.row > self.col else self.coords[i] ** 2 for i in range(self.row if self.row > self.col else self.col)]) ** .5
			self.guid_cos: tuple[int | float] | None = None if all([coord == 0 for coord in coords]) else tuple([coord / self.mod for coord in coords])
			self.maxim: int | float = max(self.coords)
			self.minim: int | float = min(self.coords)

			return

		self.row: int = 1
		self.col: int = 3
		self.coords: list[int | float] = [random.randint(-10, 10) for _ in range(3)]
		self.type_: str = 'h'
		self.mod: int | float = sum([self.coords[i] ** 2 for i in range(self.col)]) ** .5
		self.guid_cos: tuple[int | float] = tuple([coord / self.mod for coord in self.coords])
		self.maxim: int | float = max(self.coords)
		self.minim: int | float = min(self.coords)

	def transpose(self) -> typing.Self:
		self.coords = tuple(map(lambda x: x[0] if self.row > self.col else [x], list(self.coords)))
		self.row, self.col = self.col, self.row
		return Vector(self.coords)

	def solution_vector(self, a) -> typing.Self:
		if not self.exist_op(a):
			raise Exception(f'Кол-во строк и столбцов различны:\n\tСтроки: {self.row}, {a.row}\n\tСтолбцы: {self.col}, {a.row}')
		return Vector([a.coords[i] - self.coords[i] for i in range(self.col)])
	
	def scalar_product(self, a) -> int | float:
		if not isinstance(a, Vector):
			raise TypeError(f'unsupported operand type(s) for scalar product: {type(self).__name__} and {type(a).__name__}')
		
		if not self.exist_op(a):
			raise Exception(f'Кол-во строк и столбцов различны:\n\tСтроки: {self.row}, {a.row}\n\tСтолбцы: {self.col}, {a.row}')
		
		return sum([self.coords[i] * a.coords[i] if self.col > self.row else self.coords[i][0] * a.coords[i][0] for i in range(self.col if self.col > self.row else self.row)])
	
	def angel(self, a) -> int | float:
		return self.scalar_product(a) / (self.mod * a.mod)

	def projection(self, a) -> int | float:
		return self.scalar_product(a) / a.mod
	
	def collinear(self, a) -> bool:
		return 'Векторы коллиниарные' if a == self * (a.coords[0] / self.coords[0]) else 'Вектор не коллиниарные'
	
	def orthogol(self, a) -> bool:
		return 'Векторы ортогональны' if self.scalar_product(a) == 0 else 'Векторы не ортогональны'
	
	def triangle(self, a) -> int | float:
		return .5 * (self * a).mod

	def parallelogram(self, a) -> int | float:
		return (self * a).mod

	def mixed_product(self, a, b) -> int | float:
		...
	
	def complementarity(self, a, b) -> bool:
		...

	def pyramid(self, a, b) -> int | float:
		...
	
	def bazis(self, a, b, c=None) -> bool | typing.Self:
		...

	#def guid_cos(self) -> list[int | float]:
	#	return Vector([coord / self.mod for coord in self.coords])
	
	def exist_op(self, a) -> bool:
		return self.col == a.col and self.row == a.row
	
	def __add__(self, a) -> typing.Self:
		if not isinstance(a, type(self)):
			raise TypeError(f'unsupported operand type(s) for +: {type(self).__name__} and {type(a).__name__}')
		
		if not self.exist_op(a):
			raise Exception(f'Кол-во строк и столбцов различны:\n\tСтроки: {self.row}, {a.row}\n\tСтолбцы: {self.col}, {a.row}')
		
		if self.type_ == 'v':
			return Vector([[self.coords[i][0] + a.coords[i][0]] for i in range(a.row)])

		return Vector([self.coords[i] + a.coords[i] for i in range(a.col)])
	
	def __iadd__(self, a) -> typing.Self:
		try:
			return self.__add__(a)
		except:
			raise TypeError(f'unsupported operand type(s) for +=: {type(self).__name__} and {type(a).__name__}')

	def __sub__(self, a) -> typing.Self:
		if not isinstance(a, type(self)):
			raise TypeError(f'unsupported operand type(s) for -: {type(self).__name__} and {type(a).__name__}')
		
		if not self.exist_op(a):
			raise Exception(f'Кол-во строк и столбцов различны:\n\tСтроки: {self.row}, {a.row}\n\tСтолбцы: {self.col}, {a.row}')
		
		if self.type_ == 'v':
			return Vector([[self.coords[i][0] - a.coords[i][0]] for i in range(a.row)])

		return Vector([self.coords[i] - a.coords[i] for i in range(a.col)])

	def __isub__(self, a) -> typing.Self:
		try:
			return self.__sub__(a)
		except:
			raise TypeError(f'unsupported operand type(s) for -=: {type(self).__name__} and {type(a).__name__}')

	def __mul__(self, a) -> typing.Self:
		if isinstance(a, int) or isinstance(a, float):
			return Vector([a * coord for coord in self.coords])
		
		if not isinstance(a, Vector):
			raise TypeError(f'unsupported operand type(s) for *: {type(self).__name__} and {type(a).__name__}')
		
		matrix = [self.coords, a.coords]

		coords = []
		for i in range(self.col):
			minor = []
			for j in range(self.col):
				tmp = []
				for k in range(self.col):
					if i != k and j < len(matrix):
						tmp += [matrix[j][k]]
				
				if tmp != []:
					minor += [tmp]

			coords += [(minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]) * (-1) ** i]
		
		return Vector(coords)

	def __imul__(self, a) -> typing.Self:
		try:
			return self.__mul__(a)
		except:
			raise TypeError(f'unsupported operand type(s) for *=: {type(self).__name__} and {type(a).__name__}')
	
	def __eq__(self, a) -> bool:
		if not self.exist_op(a):
			raise Exception(f'Кол-во строк и столбцов различны:\n\tСтроки: {self.row}, {a.row}\n\tСтолбцы: {self.col}, {a.row}')
		return all([self.coords[i] == a.coords[i] if self.col > self.row else self.coords[i][0] == a.coords[i][0] for i in range(self.col if self.col > self.row else self.row)])

	def __contains__(self, item) -> bool:
		return any([item == coord for coord in self.coords])

	def __getitem__(self, index) -> bool:
		if index >= len(self.coords) or (index < 0 and abs(index) > len(self.coords)):
			raise IndexError('vector index out of range')

		return self.coords[index]
	
	def __setitem__(self, index, item) -> None:
		self.coords[index] = item

	def __str__(self) -> str:
		if self.col > self.row:
			return f'({', '.join(list(map(str, self.coords)))})'
		
		return f'(\n {',\n '.join(list(map(str, self.coords)))}\n)'

			