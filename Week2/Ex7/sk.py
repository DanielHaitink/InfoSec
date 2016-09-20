import sys

sk = [8, 30, 39, 88, 221, 388, 812, 1782, 3411, 8731, 15610, 33333, 70123, 154321, 300001, 666666]
sumLi = [8, 38, 77, 165, 386, 774, 1586, 3368, 6779, 15510, 31120, 64453, 134576, 288897, 588898, 1255564] # sums of public key
n = 1434539 # > sumLi last index
m = 352 # multiplication constant
public_key = [2816, 10560, 13728, 30976, 77792, 136576, 285824, 627264, 1200672, 204234, 1191103, 256904, 296133, 1243049, 879005, 836575]
public_keyHex = "0xb000x29400x35a00x79000x12fe00x215800x45c800x992400x1252200x31dca0x122cbf0x3eb880x484c50x12f7a90xd699d0xcc3df"
inv_Mod = 639837

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def initialize(sk, n, m, sumLi, public_key, public_keyHex):
	public_key = []
	sumLi = []
	sum = 0
	for ai in sk:
		ki = m * ai % n 
		sum += ai
		public_key.append(ki)
		public_keyHex += " " + hex(ki)
		sumLi.append(sum)
	
	print(public_key)
	print(sumLi)
	print(public_keyHex)	

def encrypt(char, public_key):
	binaryChar = bin(ord(char)).replace("0b", "")
	c = 0
	index = 0
	for bn in reversed(binaryChar):
		c += int(bn) * public_key[index]
		index += 1
	return c

def solveDecrypt(charNum, sk):
	binary = "0b"
	binary2 = "0b"
	for ai in reversed(sk):
		if len(binary) < 10:
			if ai <= charNum:
				charNum -= ai
				binary += "1"
			else :
				binary += "0"
		else:
			if ai <= charNum:
				charNum -= ai
				binary2 += "1"
			else :
				binary2 += "0"
	return chr(int(binary,2)) + chr(int(binary2,2))

def decrypt(charEnc):
	return solveDecrypt((charEnc* inv_Mod) % n, sk)

def decryptText(text):
	decrypted = ""
	for letter in text:
		decrypted += decrypt(letter)
	return decrypted

def encryptText(text, public_key):
	encrypted = []
	for letter in text:
		encrypted.append(encrypt(letter, public_key))
	return encrypted


#initialize (sk, n, m, sumLi, public_key, public_keyHex)

#print(encrypt("p", public_key))
#print(decrypt(encrypt("p", public_key)))

#text = "DEZE tekst is encrypted!"
#encryptedText = encryptText(text, public_key)
#print(encryptedText)
#decryptedText = decryptText(encryptedText)
#print(decryptedText)
text = ""

for line in open("DanielHaitink.txt", 'r+'):
	decimal = int(line, 16)
	text += decrypt(decimal)
print(text)
print(decrypt(2495324).encode('utf8').decode('utf8'))


for line in sys.stdin:
	encrypted = encryptText(line, public_key)
	print(encrypted)
	print(decryptText(encrypted))


