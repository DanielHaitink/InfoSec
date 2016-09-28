def modulo(base, exponent, modulus):
	if exponent == 1:
		return base
	returnVal = modulo(base, int(exponent) >> 1, modulus)
	returnVal = (returnVal * returnVal) % modulus
	if exponent % 2:
		return (returnVal * base) % modulus
	return returnVal

def calcPrimeFactors(prime):
	divisor = 2
	currentFactor = 0
	facList = []

	while prime != 1:
		if (prime%divisor) == 0:
			prime = int(prime/divisor) 
			if currentFactor == 0:
				currentFactor = divisor
			else:
				currentFactor *= divisor
		else:
			if currentFactor != 0:
				facList.append(currentFactor)
			divisor += 1
			currentFactor = 0
	if currentFactor != 0:
		facList.append(currentFactor)

	return facList

def isGenerator(prime, gen, primeFac):
	for fac in primeFac:
		if modulo(gen, (prime - 1) / fac, prime) == 1:
			return False
	return True

def primeGenerator(prime):
	primeFac = calcPrimeFactors(prime - 1)
	generators = []
	print(primeFac)

	for i in range(0, prime):
		if (isGenerator(prime, i, primeFac)):
			generators.append(i)
	return generators

primeNumber = int(input("Input prime number\n"))

print(primeGenerator(primeNumber))
