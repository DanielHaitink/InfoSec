#include <cmath>
#include "modulo.h"

long bigModulo(long base, long exponent, long modulus)
{
	if (exponent == 1)
		return base;
	long returnValue  = bigModulo(base, exponent >> 1, modulus);
	returnValue = (returnValue * returnValue) % modulus;
	return exponent % 2 ? (returnValue * base) % modulus : returnValue;
}