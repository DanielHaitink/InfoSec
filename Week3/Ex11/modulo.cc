#include <iostream>
#include <cmath>

using namespace std;

long bigModuloRecursive(long base, long exponent, long modulus)
{
	if (exponent == 1)
		return base;
	long returnValue  = bigModuloRecursive(base, exponent >> 1, modulus);
	returnValue = (returnValue * returnValue) % modulus;
	return exponent % 2 ? (returnValue * base) % modulus : returnValue;
}

int main(int argc, char *argv[])
{
	long base, exponent, modulus;
	cin >> base;
	cin >> exponent;
	cin >> modulus;

	cout << ( (long)pow(base, exponent) % modulus ) << '\n';
	cout << bigModuloRecursive(base, exponent, modulus) << '\n';
}