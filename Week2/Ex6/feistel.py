import sys, hashlib

def listToString(list):
	string = ""
	for item in list:
		string += str(item)
	return string

def generateSHA2Sums(key, size):
	SHA2Keys = []
	prevKey = key
	for i in range(0,size):
		prevKey = hashlib.sha256(prevKey.encode('utf-8')).hexdigest()
		SHA2Keys.append(prevKey)
	return SHA2Keys

def getKey(keyComb, loop):
	index = loop * 8
	return keyComb[index:index+8]

def hexToInt(hexa, count):
	retList = []
	for i in range(0,count,2):
		retList.append(int(hexa[i:i+1], 16))
	#print(retList)
	return retList

def xorFour(string, key):
	returnString = ""
	#print("LENGTH XOR = " + str(string))
	for i in range(0,4):
		returnString += chr(ord(string[i]) ^ key[i])
	return returnString

def feistel8Bytes(str8Bytes, key):
	if len(str8Bytes) != 8:
		print("NOT 8\n")

	#print(str8Bytes[4:8])
	L1 = str8Bytes[0:4]
	R1 = str8Bytes[4:8]
	L2 = R1
	R2 = xorFour(L1, hexToInt(key,8))
	return L2+R2

def feistel8BytesDecrypt(str8Bytes, key):
	if len(str8Bytes) != 8:
		print("NOT 8\n")

	L2 = str8Bytes[0:4]
	R2 = str8Bytes[4:8]
	R1 = L2
	L1 = xorFour(R2, hexToInt(key,8))
	return L1+R1

def feistelEncrypt(text, loops, key):
	text = text.encode('utf8').decode("utf8")
	#print(text)
	numKeys = int(loops / 8)

	if loops % 8 :
		numKeys += 1

	keys = listToString(generateSHA2Sums(key, numKeys))

	if (len(text)) % 8:
		print("text not dividable by 8!\n")

	for i in range(0, loops):
		print("LOOP " + str(i))
		currentKey = getKey(keys, i)
		encryptedText = ""
		for startIndex in range(0, len(text), 8):
			encryptedText += feistel8Bytes(text[startIndex:startIndex+8], currentKey)
		print(text)
		text = encryptedText
	return text

def feistelDecrypt(text, loops, key):
	numKeys = int(loops / 8)

	if loops % 8 :
		numKeys += 1

	keys = listToString(generateSHA2Sums(key, numKeys))
	for i in range(loops, 0, -1):
		decryptedText = ""
		currentKey = getKey(keys, i)
		for startIndex in range(0, len(text), 8):
			decryptedText += feistel8BytesDecrypt(text[startIndex:startIndex+8], currentKey)
		print(text)
		text = decryptedText
	return text


print("abcdefghijklmnop")
encrypt = feistelEncrypt("abcdefghijklmnop", 3, "disf39fq")
print(encrypt)
decrypt = feistelDecrypt(encrypt, 3, "disf39fq")
print(decrypt)
#print(generateSHA2Sums("test", 6))
#print(len("bd11fd28eabd0b87f2ff4595a50041bfb882bbf8ae058ea5d677c7da07d43786"))