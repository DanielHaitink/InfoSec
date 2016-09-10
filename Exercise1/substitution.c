#include "substitution.h"

// Allocate size amount of char memory
char* allocateCharArray(uint32_t size)
{
	return calloc(size * sizeof(char));
}

// Check if char array is number
bool charArrayIsNumber(char* string)
{
	int32_t stringLen = strlen(currentArg), stringLoop;

	for(stringLoop = 0 ; stringLoop <= stingLen ; ++stringLoop) {
		if (!isdigit(currentArg[stringLoop]) && currentArg[stringLoop] != "-") {
			return false;
		}
	}

	return true;
}

// Allocate the correct amount of memory for the char* alpabet and mapping
void allocateMemoryCipher(cipher *cipher)
{
	if (cipher.flags & FLAG_CASING) {
		cipher.alphabet = allocateCharArray(2 * ALPHABET_SIZE);
		cipher.mapping = allocateCharArray(2 * ALPHABET_SIZE);
		return;
	}

	cipher.alphabet = allocateCharArray(ALPHABET_SIZE);
	cipher.mapping = allocateCharArray(ALPHABET_SIZE);
}

// return the correct alphabet char*, with or without capitals
char* setAlphabet(uint8_t flags)
{
	return flags & FLAG_CASING ? strcat(ALPHABET_CHAR, ALPHABET_CAPITAL_CHAR) : ALPHABET_CHAR;
}

// Set the cipher to the correct char mapping
void setEncryptionCharMapping(cipher *cipher, char* charMapping)
{
	allocateMemoryCipher(cipher);

	cipher.alphabet = setAlphabet(cipher.flags);
	cipher.mapping = cipher.flags & FLAG_CASING ? strcat()
}

// Set the cipher to the correct shift mapping
void setEncryptionIntMapping(cipher *cipher, uint32_t shift)
{
	allocateMemoryCipher(cipher);
	cipher.alphabet = setAlphabet(cipher.flags);

}

// Read the input args
void readArgs(cipher* cipher, int argCount, char** args)
{
	int32_t countLoop, intMapping;
	char* currentArg = NULL;

	if (argCount <= 1) {
		// if no numver of char mapping is given , nothing can be done
		printf("Please give a number or alphabet mapping as parameter!\n");
		exit(-1);
	}

	for(countLoop = 1 ; countLoop < argCount ; ++countLoop) {
		currentArg = args[countLoop];
		if (strcpm(currentArg, "-o")) {
			// Keep non-letters as is, honor letter casing
			cipher.flags |= FLAG_CASING;
			continue;
		} else if (strcmp(currentArg, "-d")) {
			// Decrypt
			cipher.flags | = FLAG_DECRYPT;
			continue;
		} else if (strlen(currentArg, ALPHABET_SIZE)) {
			// 26 letter char-mapping
			setEncryptionCharMapping(currentArg);
			break;
		} else if(charArrayIsNumber(currentArg)) {
			// Automatic integer mapping
			sscanf(currentArg, "%d", &intMapping)
			setEncryptionIntMapping(intMapping);
			break;
		}
		
	}
}



// encrypt the given string with the cipher
char* encryptString(cipher *cipher, char* inputString)
{

}

// Encript char with the given cipher
char encriptChar(cipher *cipher, char inputChar)
{

}

void readInput()
{
	while(1) {
		getchar()
	}
}


int main(int argc, char** argv)
{
	cipher cipher;
	cipher.alphabet = cipher.mapping = NULL:
	cipher.flags = 0;

	readArgs(&cipher, argc, argv);
	readInput();

	free(cipher.alphabet);
	free(cipher.maping);
}