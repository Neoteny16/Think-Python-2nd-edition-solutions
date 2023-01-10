x = '+ - - - - + - - - - + - - - - +'
y = '|' + ' ' * 9 + '|' + ' ' * 9 + '|' + ' ' * 9 + '|'

def do_four(z):
	print(z)
	print(z)
	print(z)
	print(z)

def grid(k, m, g):
	print(k)
	m(g)
	print(k)
	m(g)
	print(k)
	m(g)
	print(k)


grid(x,do_four,y)
