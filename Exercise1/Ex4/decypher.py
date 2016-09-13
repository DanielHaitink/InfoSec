import sys, numpy, os

hist = []
text = ""
stdDev = []

A_INT = ord('a')

#for line in sys.stdin:
#	text += line.rstrip()

file = open("./encrypted.txt", "r+")

print(file)

for line in file:
    text = text + line.rstrip()

file.close()

for i in range(5,15) :

	print(i)

	hist = []
	sumOfStd = 0
	#alphabetHist = [0] * 26
	lettersHist = [[0 for x in range(26)] for y in range(i)] 

	print(lettersHist)

	for letter in range(0, len(text)):

		#print(letter)

		letterChar = text[letter]
		letterNumber = ord(letterChar)

		#print(letterChar)
		modLetter = (letterNumber + 1) % i

		#print(letterNumber - A_INT)
		#print(i)
		print(letterNumber - A_INT)
		lettersHist[modLetter][letterNumber - A_INT] += 1

	lettersHist
	for j in range(0, len(lettersHist) - 1):
		currentSTD = numpy.std(lettersHist[j])
		print(lettersHist[j])
		print(currentSTD)
		sumOfStd += currentSTD

	stdDev.append(sumOfStd)

for i in range(0, len(stdDev) - 1):
	print("SUM OF STD " + str(i + 5) + "= " + str(stdDev[i]))



