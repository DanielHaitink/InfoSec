import sys, ast

def encrypt(p, k, pNum = False, kNum = False):
	if not pNum:
		p = ord(p)
	if not kNum:
		k = ord(k)
	return (p ^ k)

def decrypt(c, k, cNum = False, kNum = False):
	if not cNum:
		c = ord(c)
	if not kNum:
		k = ord(k)
	return chr((c ^ k))

def encryptText(c, k):
	encrypted = ""
	for i in range(0, len(c)):
		encrypted += chr(encrypt(c[i], k[i]))
	return encrypted

def decryptText(c, k):
	decrypted = ""
	for i in range(0, len(c)):
		decrypted += decrypt(c[i], k[i])
	return decrypted

def stringToList(string):
	return ast.literal_eval(string)

text = "informationsecurity"
key = "zmxncbvlaksjdhfgqod"
altKey = [120,109, 127, 113, 98, 110, 116, 115, 108, 101, 105, 120, 114, 110, 112, 103, 125, 111, 110]
altKeyC = ""
for i in altKey:
	altKeyC += chr(i)
encrypted = encryptText(text, key)
print(encrypted)
eList = []
for i in encrypted:
	eList.append(ord(i))
print(eList)
decrypted = decryptText(encrypted, altKeyC)

print(decrypted)

text = ""
key = ""
action = ""
encrypted = ""
decrypted = ""
for line in sys.stdin:
	if action == "":
		if line != "-d\n" and line != "-e\n":
			print("NO VALID OPTION GIVEN\n")
			continue;
		action = line
	elif text == "":
		text = line;
	elif key == "":
		key = line
		if key != "" and text != "" and len(key) == len(text):
			if action == "-d\n":
				print(decryptText(text, key))
			else:
				encrypted = encryptText(text,key)
				decrypted = decryptText(encrypted, key)
				print("ENC = " +str(encrypted))
				print("DEC = " + decrypted)
		else:
			print("Something went wrong\n")
		text = ""
		key = ""
		action = ""