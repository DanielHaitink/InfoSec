import sys

moduloSize = 127
flag = 0
FLAG_ENCRYPT = 0x01
FLAG_DECRYPT = 0x02
FLAG_KEYINT = 0x04
key =  "zmxncbvlaksjdhfgqod"
text = "informationsecurity"
encryptedText = "hzcbtnveiyfbhjzxyhb"
encryptedText = "rbsdtnvyiefbhfrxydb"
encryptedText = "tdebrpxyiedzbltvybd"
#encryptedText = "tlonfzhqukrntvljktn"
#encryptedText = "tlqrfzhoaqnjvddjstr"
encryptedText = "tdbrpxyie~zbltvy|~"
#encryptedText = "tdebrpxyiedzbltvybd"
#text = "knapsackdatasecrets"
keyInt = [120, 109, 127, 113, 98, 110, 116, 115, 108, 101, 105, 120, 114, 110, 112, 103, 125, 111, 110]
returnText = ""
CHAR_A = ord('a')

def listToString(list):
	string = ""
	for item in list:
		string += chr(item)
	return string

def alpOrd(letter):
	return ord(letter) #- CHAR_A

def encrypt(plainChar, keyChar):
	charNumber = (alpOrd(plainChar) ^ alpOrd(keyChar))
	print(charNumber)
	return charNumber + CHAR_A # % 26 #+ CHAR_A

def decrypt(encryptedChar, keyChar):
	print(ord(keyChar))
	#charNumber = (moduloSize + (alpOrd(encryptedChar) ^ alpOrd(keyChar))) % moduloSize 
	charNumber = (moduloSize - (alpOrd(encryptedChar) ^ alpOrd(keyChar))) % moduloSize 
	#charNumber = alpOrd(encryptedChar) ^ alpOrd(keyChar)
	print(charNumber)
	return charNumber# + CHAR_A

for arg in sys.argv:
	if arg == "-e":
		flag |= FLAG_ENCRYPT
	elif arg == "-d":
		flag |= FLAG_DECRYPT
	elif arg == "-ki":
		flag |= FLAG_KEYINT


if (flag & FLAG_ENCRYPT and flag & FLAG_DECRYPT):
	sys.exit("can't encrypt and decrypt\n")
if (flag == 0):
	sys.exit("nothing specified")


if flag & FLAG_KEYINT:
	key = listToString(keyInt);
if flag & FLAG_DECRYPT:
	text = encryptedText

print(text)
print(key)

i = 0
for letter in text:
	if (flag & FLAG_ENCRYPT):
		returnText += chr(encrypt(letter, key[i]))
	else:
		returnText += chr(decrypt(letter, key[i]))
	i += 1

print(returnText)
