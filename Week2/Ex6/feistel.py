import sys, hashlib

## How to use:
## Use -d or -e as argument to en or decrypt
## First give the key
## Then the program will en/decrypt the input stream

# Convert a list containing objects to a string
def listToString(list):
	string = ""
	for item in list:
		string += str(item)
	return string

# Generate size amount of SHA256 sum keys, generated from the original key
def generateSHA2Sums(key, size):
	SHA2Keys = []
	prevKey = key
	for i in range(0,size):
		prevKey = hashlib.sha256(prevKey.encode('utf-8')).hexdigest()
		SHA2Keys.append(prevKey)
	return SHA2Keys

# Get the right hexadecimal numbers from the key for the curent loop
def getKey(keyComb, loop):
	index = loop * 8
	return keyComb[index:index+8]

# Calculate count amount of dubbel digit sized heximal numbers
def hexToInt(hexa, count):
	retList = []
	for i in range(0,count,2):
		retList.append(int("0x" + hexa[i:i+1], 16))
	return retList

# XOR over four chars in string and four hexadecimal numbers in key
def xorFour(string, key):
	returnString = ""
	#print(string)
	for i in range(0,4):
		returnString += chr(ord(string[i]) ^ key[i])
	return returnString

# Do the basic feistel encryptuon over 8 bytes
def feistel8Bytes(str8Bytes, key):
	if len(str8Bytes) != 8:
		print("NOT 8\n")

	L1 = str8Bytes[0:4]
	R1 = str8Bytes[4:8]
	L2 = R1
	R2 = xorFour(L1, hexToInt(key,8))
	return L2+R2

def bytesToChar(bytes):
	returnString = ""
	for i in bytes:
		returnString += chr(int.from_bytes(i, byteorder='big'))
	return returnString

# Do the basic feistel decryption over 8 bytes
def feistel8BytesDecrypt(str8Bytes, key):
	if len(str8Bytes) != 8:
		print("NOT 8\n")

	L2 = (str8Bytes[0:4])
	R2 = (str8Bytes[4:8])
	R1 = L2
	L1 = xorFour(R2, hexToInt(key,8))
	return L1+R1

# Add padding to text
def addPadding(text, amount, char = 'n'):
	for i in range(0,amount):
		text += char
	return text

# Check if the text is dividable b 8, else add padding
def sizeCheck(text, size = 8):
	rest = 8 - (len(text) % 8)
	if rest:
		text = addPadding(text, rest)
	return text

# Encrypt a complete string with a certain amount of loops and a key
def feistelEncrypt(text, loops, key):
	numKeys = int(loops / 8)
	if loops % 8 :
		numKeys += 1
	# Check for padding
	text = sizeCheck(text)
	# Generate keys
	keys = listToString(generateSHA2Sums(key, numKeys))

	# Encrypt loop
	for i in range(0, loops):
		currentKey = getKey(keys, i)
		encryptedText = ""
		# Encrypt every 8 bytes
		for startIndex in range(0, len(text), 8):
			encryptedText += feistel8Bytes(text[startIndex:startIndex+8], currentKey)
		text = encryptedText
	return text

# Decrypt a complete encrypted string with a certain amount of loops and a key
def feistelDecrypt(text, loops, key):
	numKeys = int(loops / 8)
	if loops % 8 :
		numKeys += 1
	# Generate keys
	keys = listToString(generateSHA2Sums(key, numKeys))
	print(keys)

	# Check if text is dividable by 8
	if (len(text)) % 8:
		print("text not dividable by 8!\n")

	# Reverse loop the loop count
	for i in range(loops-1, -1, -1):
		decryptedText = ""
		currentKey = getKey(keys, i)
		# Decrypt every 8 bytes
		for startIndex in range(0, len(text), 8):
			decryptedText += feistel8BytesDecrypt(text[startIndex:startIndex+8], currentKey)
		text = decryptedText
	return text

def xorFourBytes(string, key):
	returnString = []
	#print(string)
	for i in range(0,4):
		print(string[i])
		returnString.append((int.from_bytes(string[i], byteorder = "big")  ^ key[i]).to_bytes(2, byteorder='big'))
	print((returnString))
	return returnString

def feistel8BytesDecryptBytes(str8Bytes, key):
	if len(str8Bytes) != 8:
		print("NOT 8\n")

	L2 = (str8Bytes[0:4])
	R2 = (str8Bytes[4:8])
	R1 = L2
	L1 = xorFourBytes(R2, hexToInt(key,8))
	return L1+R1

def feistelDecryptBytes(text, loops, key):
	numKeys = int(loops / 8)
	if loops % 8 :
		numKeys += 1
	# Generate keys
	keys = listToString(generateSHA2Sums(key, numKeys))
	print(keys)

	# Check if text is dividable by 8
	if (len(text)) % 8:
		print("text not dividable by 8!\n")

	# Reverse loop the loop count
	for i in range(loops-1, -1, -1):
		decryptedText = []
		currentKey = getKey(keys, i)
		# Decrypt every 8 bytes
		for startIndex in range(0, len(text), 8):
			retList = feistel8BytesDecryptBytes(text[startIndex:startIndex+8], currentKey)
			for item in retList:
				decryptedText.append(item)
		text = decryptedText
	return text


byteList = []
encryptedText = ""
with open("feistel.enc.Feistel", 'rb') as f:
	byte = f.read(1)
	while byte:
		byteList.append(byte)
		#encryptedText += chr(int.from_bytes(byte, byteorder='big'))
		#encryptedText += byteChr(byte)
		#encryptedText += chr(int(byte.encode('hex'), 16))
		byte = f.read(1)
print(byteList)
print(encryptedText)

key = "The Feistel Algorithm"
print("Decrypted:")
decrypted = (feistelDecryptBytes(byteList, 16, key))
print(decrypted)
for item in decrypted:
	print(item.decode(encoding='UTF-8',errors='ignore'))


flag = 0
FLAG_ENCRYPT = 0x01
FLAG_DECRYPT = 0x02

for arg in sys.argv:
	if arg == "-e":
		flag |= FLAG_ENCRYPT
	elif arg == "-d":
		flag |= FLAG_DECRYPT

key = input().rstrip()
for line in sys.stdin:
	line = line.rstrip()
	if flag & FLAG_ENCRYPT:
		print(feistelEncrypt(line, 16, key))
	else:
		print(feistelDecrypt(line, 16, key))


