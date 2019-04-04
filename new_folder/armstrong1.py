for i in range(10000):
	l= list(map(lambda x: int(x)**len(str(i)), list(str(i))))
	if sum(l)==i:
		print('armstrong', i)