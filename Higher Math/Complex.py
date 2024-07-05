class Complex:


	def __init__(self, Re: int, Im: int) -> None:
		self.Re = Re
		self.Im = Im


	# Сопряжение комплексного числа
	def conjugate(self):
		self.Im *= (- 1)


	def __add__(self, a):
		if isinstance(a, type(self)):
			return Complex(self.Re + a.Re, self.Im + a.Im)

		else:
			raise TypeError(f'unsupported operand type(s) for +: {type(self).__name__} and {type(a).__name__}')


	def __sub__(self, a):
		if isinstance(a, type(self)):
			return Complex(self.Re - a.Re, self.Im - a.Im)

		else:
			raise TypeError(f'unsupported operand type(s) for -: {type(self).__name__} and {type(a).__name__}')


	def __iadd__(self, a):
		try:
			return self.__add__(a)
		except:
			raise TypeError(f'unsupported operand type(s) for +=: {type(self).__name__} and {type(a).__name__}')


	def __isub__(self, a):
		try:
			return self.__sub__(a)
		except:
			raise TypeError(f'unsupported operand type(s) for -=: {type(self).__name__} and {type(a).__name__}')


	def __mul__(self, a):
		if isinstance(a, type(self)):
			Re: int = (self.Re * a.Re) - (self.Im * a.Im)
			Im: int = (self.Re * a.Im) + (self.Im * a.Re)
			return Complex(Re, Im)

		else:
			raise TypeError(f'unsupported operand type(s) for *: {type(self).__name__} and {type(a).__name__}')


	def __imul__(self, a):
		try:
			return self.__mul__(a)
		except:
			raise TypeError(f'unsupported operand type(s) for *=: {type(self).__name__} and {type(a).__name__}')


	def __truediv__(self, a):
		if isinstance(a, type(self)):
			if abs(a.Re) + abs(a.Im) == 0:
				raise ZeroDivisionError('division by zero')

			a.Im *= (- 1)
			num: int = self.__mul__(a)
			denom: int = a.Re ** 2 + a.Im ** 2
			return Complex(num.Re / denom, num.Im / denom)

		else:
			raise TypeError(f'unsupported operand type(s) for /: {type(self).__name__} and {type(a).__name__}')


	def __itruediv__(self, a):
		try:
			return self.__truediv__(a)
		except:
			raise TypeError(f'unsupported operand type(s) for /=: {type(self).__name__} and {type(a).__name__}')


	def mod(self):
		return (self.Re ** 2 + self.Im ** 2) ** .5



	def __str__(self) -> str:
		return f'{self.Re} + {self.Im}j' if self.Im > 0 else f'{self.Re} - {str(self.Im)[1:]}j'
