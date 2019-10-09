def multiples(num):
	for num  in range(1,100):
		if num % 3 == 0:
			print("fizz")
		elif num % 5 == 0:
			print("buzz")
		elif num % 15 == 0:
			print("fizzbuzz")
multiples(75)
