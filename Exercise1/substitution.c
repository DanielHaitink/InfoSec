#include "substitution.h"

// Allocate size amount of char memory
char* allocateCharArray(uint32_t size)
{
	return malloc(size * sizeof(char));
}

// Free malloced variables in cipher
void freeCipher(cipher *cipher)
{
	free(cipher->alphabet);
	free(cipher->mapping);
}

// Check if char array is number
bool charArrayIsNumber(char* string)
{
	int32_t stringLen = strlen(string), stringLoop;

	for(stringLoop = 0 ; stringLoop < stringLen ; ++stringLoop) {
		if (!isdigit(string[stringLoop]) && string[stringLoop] != '-') {
			return false;
		}
	}

	return true;
}

// convert the given string to capital letters
char* stringToUpper(char* string)
{
	uint32_t stringLoop;
	char *capitalUpper = allocateCharArray(strlen(string));

	for (stringLoop = 0 ; stringLoop < strlen(string) ; ++stringLoop) {
		capitalUpper[stringLoop] = toupper(string[stringLoop]);
	}

	return capitalUpper;
}

// Allocate the correct amount of memory for the char* alphabet and mapping
void allocateMemoryCipher(cipher *cipher)
{
	if (cipher->flags & FLAG_CASING) {
		cipher->alphabet = allocateCharArray(2 * ALPHABET_SIZE);
		cipher->mapping = allocateCharArray(2 * ALPHABET_SIZE);
		return;
	}

	cipher->alphabet = allocateCharArray(ALPHABET_SIZE);
	cipher->mapping = allocateCharArray(ALPHABET_SIZE);
}

// return the correct alphabet char*, with or without capitals
char* setAlphabet(uint8_t flags)
{
	return flags & FLAG_CASING ? ALPHABET_BOTH_CHAR: ALPHABET_CHAR;
}

// Set the cipher to the correct char mapping
void setEncryptionCharMapping(cipher *cipher, char* charMapping)
{
	char* capitalAlphabet = NULL;

	allocateMemoryCipher(cipher);

	strcpy(cipher->alphabet, setAlphabet(cipher->flags));
	if (cipher->flags & FLAG_CASING) {
		// set mapping to capital and add
		capitalAlphabet = stringToUpper(charMapping);
		strcpy(cipher->mapping, strcat(charMapping, capitalAlphabet));
		free(capitalAlphabet);

	} else {
		strcpy(cipher->mapping, charMapping);
	}
}

// Set the cipher to the correct shift mapping
void setEncryptionIntMapping(cipher *cipher, int32_t shift)
{
	uint32_t alphabetLoop;
	allocateMemoryCipher(cipher);
	strcpy(cipher->alphabet, setAlphabet(cipher->flags));

	if (shift < 0) shift = ALPHABET_SIZE + shift;

	for ( alphabetLoop = 0 ; alphabetLoop < ALPHABET_SIZE * 2 ; ++alphabetLoop) {
		if (alphabetLoop < ALPHABET_SIZE){
			cipher->mapping[alphabetLoop] = cipher->alphabet[( alphabetLoop + shift ) % ALPHABET_SIZE];
		} else if (cipher->flags & FLAG_CASING) {
			cipher->mapping[alphabetLoop] = cipher->alphabet[(( alphabetLoop + shift ) % ALPHABET_SIZE ) + ALPHABET_SIZE ];
		}
	}

}

// Read the input args
void readArgs(cipher* cipher, int argCount, char** args)
{
	int32_t countLoop, intMapping;
	char* currentArg;
	bool encryptionSet = false;

	if (argCount <= 1) {
		// if no numver of char mapping is given , nothing can be done
		printf("Please give a number or alphabet mapping as parameter!\n");
		exit(-1);
	}

	for(countLoop = 1 ; countLoop < argCount ; ++countLoop) {
		currentArg = args[countLoop];

		if (strcmp(currentArg, "-o") == 0) {
			// Keep non-letters as is, honor letter casing
			cipher->flags |= FLAG_CASING;
			continue;
		} else if (strcmp(currentArg, "-d") == 0) {
			// Decrypt
			cipher->flags |= FLAG_DECRYPT;
			continue;
		} else if (strlen(currentArg) == ALPHABET_SIZE) {
			// 26 letter char-mapping
			setEncryptionCharMapping(cipher, currentArg);
			encryptionSet = true;
			break;
		} else if(charArrayIsNumber(currentArg)) {
			// Automatic integer mapping
			sscanf(currentArg, "%d", &intMapping);
			setEncryptionIntMapping(cipher, intMapping);
			encryptionSet = true;
			break;
		}
	}

	if (!encryptionSet) {
		printf("ENCRYPTION NOT SET\n");
		exit(-3);
	}
}

// Return the encrypted value of a given char
char findCharMap(cipher cipher, char inputChar) 
{
	uint32_t alphabetLoop;

	for (alphabetLoop = 0 ; alphabetLoop < strlen(cipher.alphabet) ; ++alphabetLoop) {
		if (cipher.alphabet[alphabetLoop] == inputChar) {
			return cipher.mapping[alphabetLoop];
		}
	}

	printf("ERROR: NO MAPPING FOUND FOR %c\n", inputChar);
	return inputChar;
}

char findCharMapDecrypt(cipher cipher, char inputChar)
{
	uint32_t alphabetLoop;

	for (alphabetLoop = 0 ; alphabetLoop < strlen(cipher.mapping) ; ++alphabetLoop) {
		if (cipher.mapping[alphabetLoop] == inputChar) {
			return cipher.alphabet[alphabetLoop];
		}
	}

	printf("ERROR: NO MAPPING FOUND FOR %c\n", inputChar);
	return inputChar;
}

// Encrypt char with the given cipher
char encryptChar(cipher cipher, char inputChar)
{
	if ( (inputChar >= 'A' && inputChar <= 'Z' ) || ( inputChar >= 'a' && inputChar <= 'z' )) {
		if (! ( cipher.flags & FLAG_CASING ) ) {
			inputChar = tolower(inputChar);
		}
		if (cipher.flags & FLAG_DECRYPT) {
			return findCharMapDecrypt(cipher, inputChar);
		}
		return findCharMap(cipher, inputChar);

	}

	return cipher.flags & FLAG_CASING ? inputChar : '\0';
}

// Read, encrypt and print the input until ctrl-D is pressed
void readInput(cipher *cipher)
{
	char currentChar, encryptedChar;

	while(true) {
        
        currentChar = getchar();
        if (feof(stdin)) return;
		encryptedChar = encryptChar(*cipher, currentChar);
        
        if (encryptChar != '\0'){
            putchar(encryptedChar);
        }
#ifdef DEBUG
        putchar(currentChar);
        putchar('\n');
#endif
	}
}


int main(int argc, char** argv)
{
	cipher cipher;
	cipher.flags = 0;

	readArgs(&cipher, argc, argv);
	readInput(&cipher);

	freeCipher(&cipher);
}