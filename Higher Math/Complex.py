from math import *

class Complex:


	def __init__(self, Re: int, Im: int, step: float=None) -> None:
		self.Re: float = Re
		self.Im: float = Im
		self.plos: int = (1 if Im > 0 else 4) if Re > 0 else (2 if Im > 0 else 3)
		self.step: float = step


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
			Re: float = (self.Re * a.Re) - (self.Im * a.Im)
			Im: float = (self.Re * a.Im) + (self.Im * a.Re)
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
			num: float = self.__mul__(a)
			denom: float = a.Re ** 2 + a.Im ** 2
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


	def arg(self):
		if self.Re == 0:
			return pi / 2 if self.Im > 0 else 3 * (pi / 2)
		return atan(self.Im / self.Re) + pi if self.plos in [2, 3] else atan(self.Im / self.Re)


	def __neg__(self):
		if self.Im > 0:
			self.conjugate()

		return self


	def __pos__(self):
		if self.Im < 0:
			self.conjugate()

		return self


	def euler(self):
		Re: float = self.mod() * cos(self.arg())
		Im: float = self.mod() * sin(self.arg())
		return Complex(Re, Im)


	def euler_mul(self, a):
		mod: float = self.mod() * a.mod()
		Re: float = mod * cos(self.arg() + a.arg())
		Im: float = mod * sin(self.arg() + a.arg())
		return Complex(Re, Im)


	def euler_div(self, a):
		mod: float = self.mod() / a.mod()
		Re: float = mod * cos(self.arg() - a.arg())
		Im: float = mod * sin(self.arg() - a.arg())
		return Complex(Re, Im)


	def moivre(self):
		if self.step:
			if self.step > 1:
				mod: float = self.mod() ** self.step
				arg: float = self.arg() * self.step
				Re: float = mod * cos(arg)
				Im: float = mod * sin(arg)
				return Complex(Re, Im)

			else:
				mod: float = self.mod() ** self.step
				arg: float = self.arg()

				
				n = max([i for i in range(100_000) if i * self.step <= 1])
				Complex_list = []
				for k in range(n):
					Re: float = mod * cos((arg + (2 * pi) * k) / n)
					Im: float = mod * sin((arg + (2 * pi) * k) / n)
					Complex_list.append(str(Complex(Re, Im)))

				return Complex_list
		else:
			return self.euler()
		

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

