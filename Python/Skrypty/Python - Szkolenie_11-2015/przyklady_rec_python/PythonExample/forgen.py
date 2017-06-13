table = [
	[ 1, 1, 0 ],
	[ 0, 0, 1 ],
	[ 1, 0, 0 ]
]
# Mnozenie kazdej wartosci przez 2
print [ [ row[i]*2 for i in range(3) ]
	for row in table ]
