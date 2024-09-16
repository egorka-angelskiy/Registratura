from utils import *

class Complex:

	def __init__(self, Re: int | float=None, Im: int | float=None, step: float=None) -> None:
		self.Re: float = Re if not isinstance(Re, type(None)) else random.randint(-10, 10)
		self.Im: float = Im if not isinstance(Im, type(None)) else random.randint(-10, 10)
		self.plos: int = (1 if self.Im > 0 else 4) if self.Re > 0 else (2 if self.Im > 0 else 3)
		self.step: float = step
		self.mod = (self.Re ** 2 + self.Im ** 2) ** .5
		self.arg = pi / 2 if self.Im > 0 else 3 * (pi / 2) if self.Re == 0 else atan(self.Im / self.Re) + pi if self.plos in [2, 3] else atan(self.Im / self.Re)

	# Сопряжение комплексного числа
	def conjugate(self) -> typing.Self:
		self.Im *= (- 1)
		return Complex(self.Re, self.Im, self.step)

	def __add__(self, a) -> typing.Self:
		if self.step or a.step:
			raise

		if isinstance(a, Complex):
			return Complex(self.Re + a.Re, self.Im + a.Im)
		else:
			raise TypeError(f'unsupported operand type(s) for +: {type(self).__name__} and {type(a).__name__}')
	
	def __radd__(self, a) -> typing.Self:
		return self.__add__(a)

	def __sub__(self, a) -> typing.Self:
		if isinstance(a, Complex):
			return Complex(self.Re - a.Re, self.Im - a.Im)

		else:
			raise TypeError(f'unsupported operand type(s) for -: {type(self).__name__} and {type(a).__name__}')

	def __iadd__(self, a) -> typing.Self:
		try:
			return self.__add__(a)
		except:
			raise TypeError(f'unsupported operand type(s) for +=: {type(self).__name__} and {type(a).__name__}')

	def __isub__(self, a) -> typing.Self:
		try:
			return self.__sub__(a)
		except:
			raise TypeError(f'unsupported operand type(s) for -=: {type(self).__name__} and {type(a).__name__}')

	def __mul__(self, a) -> typing.Self:
		if isinstance(a, Complex):
			Re: float = (self.Re * a.Re) - (self.Im * a.Im)
			Im: float = (self.Re * a.Im) + (self.Im * a.Re)
			return Complex(Re, Im)

		if isinstance(a, int) or isinstance(a, float):
			Re: float = (self.Re * a)
			Im: float = (self.Im * a)
			return Complex(Re, Im)
		
		raise TypeError(f'unsupported operand type(s) for *: {type(self).__name__} and {type(a).__name__}')

	def __imul__(self, a) -> typing.Self:
		try:
			return self.__mul__(a)
		except:
			raise TypeError(f'unsupported operand type(s) for *=: {type(self).__name__} and {type(a).__name__}')

	def __truediv__(self, a) -> typing.Self:
		if isinstance(a, Complex):
			if abs(a.Re) + abs(a.Im) == 0:
				raise ZeroDivisionError('division by zero')

			a.conjugate()
			num: float = self.__mul__(a)
			denom: float = a.Re ** 2 + a.Im ** 2
			return Complex(num.Re / denom, num.Im / denom)

		raise TypeError(f'unsupported operand type(s) for /: {type(self).__name__} and {type(a).__name__}')

	def __itruediv__(self, a) -> typing.Self:
		try:
			return self.__truediv__(a)
		except:
			raise TypeError(f'unsupported operand type(s) for /=: {type(self).__name__} and {type(a).__name__}')

	#def mod(self) -> float:
	#	return (self.Re ** 2 + self.Im ** 2) ** .5

	#def arg(self) -> float:
	#	if self.Re == 0:
	#		return pi / 2 if self.Im > 0 else 3 * (pi / 2)
	#	return atan(self.Im / self.Re) + pi if self.plos in [2, 3] else atan(self.Im / self.Re)

	def __neg__(self) -> typing.Self:
		if self.Im > 0:
			self.conjugate()

		return self

	def __pos__(self) -> typing.Self:
		if self.Im < 0:
			self.conjugate()

		return self

	def euler(self) -> typing.Self:
		Re: float = self.mod * cos(self.arg)
		Im: float = self.mod * sin(self.arg)
		return Complex(Re, Im)

	def euler_mul(self, a) -> typing.Self:
		mod: float = self.mod * a.mod
		Re: float = mod * cos(self.arg + a.arg)
		Im: float = mod * sin(self.arg + a.arg)
		return Complex(Re, Im)

	def euler_div(self, a) -> typing.Self:
		mod: float = self.mod / a.mod
		Re: float = mod * cos(self.arg - a.arg)
		Im: float = mod * sin(self.arg - a.arg)
		return Complex(Re, Im)

	def moivre(self) -> typing.Self:
		if self.step:
			if self.step > 1:
				mod: float = self.mod ** self.step
				arg: float = self.arg * self.step
				Re: float = mod * cos(arg)
				Im: float = mod * sin(arg)
				return Complex(Re, Im)

			mod: float = self.mod ** self.step
			arg: float = self.arg

				
			n = max([i for i in range(100_000) if i * self.step <= 1])
			Complex_list = []
			for k in range(n):
				Re: float = mod * cos((arg + (2 * pi) * k) / n)
				Im: float = mod * sin((arg + (2 * pi) * k) / n)
				Complex_list.append(str(Complex(Re, Im)))

			return Complex_list
		
		return self.euler()
		
	def log(self) -> typing.Self:
		mod: float = self.mod
		arg: float = self.arg

		Re: float = log10(mod)
		Im: float = arg
		return Complex(Re, Im)
		
	def __getitem__(self, index) -> int | float:
		if index < 0 or index > 1:
			raise IndexError('complex index out of range')
		
		return self.Re if index == 0 else self.Im

	def __setitem__(self, index, value) -> None:
		self.Re = value if index == 0 else self.Re
		self.Im = value if index == 1 else self.Im

	def __str__(self) -> str:
		return 	(
					f'({self.Re} + {self.Im}j) ^ {self.step}\tРасположенно в {self.plos} четверти' if self.Im > 0 \
					else f'({self.Re} + {str(self.Im)}j) ^ {self.step}\tРасположенно в {self.plos} четверти' if self.Im == 0 \
					else f'({self.Re} - {str(self.Im)[1:]}j) ^ {self.step}\tРасположенно в {self.plos} четверти'
				) if self.step \
				else (
					f'{self.Re} + {self.Im}j\tРасположенно в {self.plos} четверти' if self.Im > 0 \
					else f'{self.Re} + {str(self.Im)}j\tРасположенно в {self.plos} четверти' if self.Im == 0 \
					else f'{self.Re} - {str(self.Im)[1:]}j\tРасположенно в {self.plos} четверти'
				)

