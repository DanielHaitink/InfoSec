#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

#define ALPHABET_CHAR          "abcdefghijklmnopqrstuvwxyz"
#define ALPHABET_CAPITAL_CHAR  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#define ALPHABET_SIZE          26

enum flagsEnum
{
	FLAG_DECRYPT =  0x1,
	FLAG_CASING  =  0x2
};

typedef struct cipher {
	char* alphabet;
	char* encryptedAlphabet;
	uint8_t flags;
} cipher;