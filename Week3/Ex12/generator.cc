#include "modulo.h"
#include "generator.h"
#include <random>

using namespace std;

int gcd(int varA, int varB)
{
	int remainder = 0;

	while (varB != 0)
	{
		remainder = varA % varB;
		varA = varB;
		varB = remainder;
	}

	return varA;
}

int[] calcPrimeFactors(long prime)
{
	int[] factorList;

	int divisor = 2;
	int currentFactor = 0;
	while (prime != 1)
	{
		if(prime % divisor == 0)
		{
			prime /= divisor;
			currentFactor = currentFactor == 0 ? divisor : currentFactor * divisor;
		}
		else
		{
			if(currentFactor != 0)
				factorList.insert(currentFactor);
			divisor+=1;
			currentFactor = 0;
		}
	}

	return factorList;
}

bool isGenerator(long prime, int gen, list<int> primeFactors)
{
	for (size_t factorLoop = 0 ; facotrLoop < primeFactors.length() ; ++factorLoop)
	{
		if (bigModulo(gen, (prime - 1) / primeFactors.get(factorLoop), prime) == 1)
			return false;
	}
	return true;
}

std::list<int> primeGenerator(long prime)
{
	list<int> primeFactors = calcPrimeFactors(prime-1);
	list<int> generatorList;
	generatorList.begin();
	int g = rand();

	// Find all generators (how??) or a subset of all 
	while (!isGenerator(prime, g, primeFactors))
	{
		g = rand();
	}
	generatorList.insert(g);
	return generatorList;
}