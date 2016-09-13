import sys, numpy, os

text = ""
stdDev = {}
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
		modLetter = (letter + 1) % i

		letterPos = letterNumber - A_INT

		lettersHist[modLetter][letterPos] += 1

	# Calculate Standard deviation and sum it in sumOfStd
	for j in range(0, len(lettersHist) - 1):
		currentSTD = numpy.std(lettersHist[j])
		sumOfStd += currentSTD

	# Add std sum to dictionary
	stdDev.update({i : sumOfStd})

# Print standard deviation sums
for stdPos in stdDev:
	print("Sum of standard deviation length ", stdPos, " = " ,stdDev[stdPos])



