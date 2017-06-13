def moj_dekorator(function):
	def wew():
		print("Przed funkcja")
		function()
		print("Po funkcji")
	return wew

@moj_dekorator
def fun():
	print("Siema")

fun()
