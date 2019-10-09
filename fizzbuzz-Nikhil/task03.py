def multiples(num):
	for num  in range(1,100):
		if num % 3 == 0:  #number multiple of 3
			print("Fizz")
		elif num % 5 == 0:  #number multiple of 5
			print("Buzz")
		elif num % 15 == 0:  #number multiple of 3 and 5
			print("FizzBuzz")
multiples(75)
