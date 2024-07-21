from library import *

def write_content(text: str, title: str) -> None:
	file = open('info.txt', '+a')
	file.write(f'{title}\n\n{text}')