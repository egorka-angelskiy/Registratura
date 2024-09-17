from utils import *

class Matrix:

	def __init__(
			self, 
			rows: int=None, 
			columns: int=None, 
			values: list[int | float | list[int | float]]=None
		) -> None:

		if values:
			...
		
		self.__rows = 3 if not rows else (3 if rows <= 0 else rows)
		self.__columns = 3 if not columns else (3 if columns <= 0 else columns)
		self.__values = [
							[
								random.randint(-10, 10) 
								for _ in range(self.__columns)
							]
							for _ in range(self.__rows)
						] if not values and self.__rows != 1 \
						else [
							random.randint(-10, 10)
							for _ in range(self.get_columns)
						] if self.__rows == 1 and not values else values		

	@property
	def get_rows(self) -> int:
		return self.__rows

	@property
	def get_columns(self) -> int:
		return self.__columns
	
	@property
	def get_values(self) -> list[int | float | list[int | float]]:
		return self.__values
	
	def __add(self, matrix: typing.Self) -> bool:
		if not isinstance(matrix, Matrix):
			raise TypeError(f'Нельзя проверить сложение с {matrix.__type__}')
		
		return self.__rows == matrix.__rows and self.__columns == matrix.__columns
	
	def __mul(self, matrix: typing.Self) -> bool:
		if not isinstance(matrix, Matrix):
			raise TypeError(f'Нельзя проверить умножение с {matrix.__type__}')
		
		return self.__rows == matrix.__columns

	def __add__(self, matrix: typing.Self) -> typing.Self:
		if not self.__add(matrix):
			...
		
		if self.__rows == 1:
			...
		
		if self.__columns == 1:
			...

		return Matrix(
			self.__rows,
			self.__columns,
			[
				[
					self.__values[i][j] + matrix.__values[i][j]
					for j in range(self.__columns)
				]
				for i in range(self.__rows)
			]
		)
	
	def __iadd__(self, matrix: typing.Self) -> typing.Self:
		return self.__add__(matrix)
	
	def __sub__(self, matrix: typing.Self) -> typing.Self:
		if not self.__add(matrix):
			...
		
		if self.__rows == 1:
			...
		
		if self.__columns == 1:
			...
		
		return Matrix(
			self.__rows,
			self.__columns,
			[
				[
					self.__values[i][j] - matrix.__values[i][j]
					for j in range(self.__columns)
				]
				for i in range(self.__rows)
			]
		)
	
	def __isub__(self, matrix: typing.Self) -> typing.Self:
		return self.__sub__(matrix)

	def __eq__(self, matrix: typing.Self) -> bool:
		if not isinstance(matrix, Matrix):
			raise TypeError("")
		
		if not self.__add(matrix):
			raise Exception("")
		
		if self.__rows == 1:
			return all(
				[
					self.__values[i] == matrix.__values[i] 
					for i in range(self.__rows)
				]
			)
		
		if self.__columns == 1:
			return all(
				[
					self.__values[i][0] == matrix.__values[i][0]
					for i in range(self.__columns)
				]
			)
		
		return all(
			all(
				[
					self.__values[i][j] == matrix.__values[i][j]
					for j in range(self.__columns)
				]
			)
			for i in range(self.__rows)
		)

	def __mul__(self, matrix: typing.Self | int | float) -> typing.Self:
		if isinstance(matrix, int) or isinstance(matrix, float):
			if self.__rows == 1:
				return Matrix(
					self.__rows,
					self.__columns,
					[
						self.__values[i] * matrix
						for i in range(self.__columns)
					]
				)
			
			if self.__columns == 1:
				return Matrix(
					self.__rows,
					self.__columns,
					[
						[self.__values[i][0] * matrix]
						for i in range(self.__rows)
					]
				)

			return Matrix(
				self.__rows,
				self.__columns,
				[	
					[
						self.__values[i][j] * matrix
						for j in range(self.__columns)
					]
					for i in range(self.__rows)
				]
			)

		if not isinstance(matrix, Matrix):
			...
		
		if not self.__mul(matrix):
			...
		
		return
	
	def __rmul__(self, matrix: typing.Self | int | float) -> typing.Self:
		return self.__mul__(matrix)

	@property
	def T(self) -> typing.Self:
		return Matrix(
			self.__columns, 
			self.__rows, 
			[
				[
					self.__values[j][i] 
					for j in range(self.__rows)
				] 
				for i in range(self.__columns)
			]
		)

	def __getitem__(self, index_rows: int, index_columns: int=None) -> int | float | list[int | float]:
		if self.__rows == 1:
			if (index_rows > self.__columns) or (index_rows < 0 and abs(index_rows) > self.__columns):
				raise IndexError('list out of the range')
			
			return self.__values[index_rows]

		if self.__columns == 1:
			if (index_rows > self.__rows) and (index_rows < 0 and abs(index_rows) > self.__rows):
				raise IndexError('list out of the range')
			
			return self.__values[index_rows][0]
		
		return self.__values[index_rows] if not index_columns else self.__values[index_rows][index_columns]

	# operator in
	def __contains__(self, value: int | float | list[int | float | list[int | float]]) -> bool:
		if self.__rows == 1:
			...
		
		if self.__columns == 1:
			...
		
		

	def __format_values(self) -> str:
		output = '[\n'
		if self.__rows == 1:
			output += f'{'\t' * 4}{', '.join(list(map(str, self.__values)))}\n'
			output += f'{'\t' * 3}  ]'
			return output
		
		for values in self.__values:
			if self.__columns == 1:
				output += f'{'\t' * 4}{',\t'.join(list(map(str, values)))}\n'
			
			else:
				output += f'{'\t' * 4}{values}\n'
		
		output += f'{'\t' * 3}  ]'
		return output

	def __str__(self) -> str:
		return f"""
		Кол-во строк: {self.__rows}
		Кол-во столбцов: {self.__columns}
		Значения: {self.__format_values()}
		"""


if __name__ == '__main__':
	a = Matrix(
		columns=1 
	)

	print(a, a * 2, sep='\n')