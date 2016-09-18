import sys, numpy, os

allHist = []
text = ""
stdDev = {}
highestSTD = 0
probableLen = 0
probableKey = ""
decryptedText = ""
keyShift = []
secondBest = ""
A_INT = ord('a')

# Put encrypted file in string text
file = open("./encrypted.txt", "r+")

for line in file:
    text = text + line.rstrip()
file.close()

# loop through the possible string lengths
for i in range(5,16) :

	# Initialize the values
	lettersHist = []
	sumOfStd = 0

	# Fill the 
	for h in range(0,i):
		hList = []
		for w in range (0,26):
			hList.append(0)
		lettersHist.append(hList)

	# Loop trough text
	for letter in range(0, len(text)):

		# TODO : CALCULATE IF THE FOLLOWING CALCULATIONS ARE CORRECT!! 
		letterChar = text[letter]
		letterNumber = ord(letterChar)
		modLetter = letter % i

		letterPos = letterNumber - A_INT

		lettersHist[modLetter][letterPos] += 1

	# Calculate Standard deviation and sum it in sumOfStd
	for j in range(0, len(lettersHist) - 1):
		currentSTD = numpy.std(lettersHist[j])
		sumOfStd += currentSTD

	# Add std sum to dictionary
	stdDev.update({i : sumOfStd})
	allHist.append(lettersHist)

# Print standard deviation sums
for stdPos in stdDev:
	if int(stdDev[stdPos]) > highestSTD:
		highestSTD = stdDev[stdPos]
		probableLen = stdPos
	print("Sum of standard deviation length ", stdPos, " = " ,stdDev[stdPos])

# crack the key
keywordHist = allHist[probableLen-5]
for i in range(0, probableLen):
	probE = 0
	probESize = 0
	secondBest
	probESecond = 0
	probESecondSize = 0
	
	for letter in range(0,26):
		if keywordHist[i][letter] > probESize:
			probESecondSize = probESize
			probESecond = probE

			probESize = keywordHist[i][letter]
			probE = letter + A_INT

	letter = probE - 4
	keyShift.append(26 - (letter - A_INT))
	probableKey += chr(letter)
	secondBest += chr(probESecond)

print("The probable key is: %s" % probableKey)
print("The probable second best key is: %s" % secondBest)
print(keyShift)

# Decrypt
for letter in range(0, len(text)):
	modLetter = letter % probableLen
	decryptLetter = ((ord(text[letter]) - A_INT) + keyShift[modLetter] ) % 26
	decryptedText += chr(decryptLetter + A_INT)
	#print(chr(decryptLetter))

print(decryptedText)





