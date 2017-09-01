#! /usr/bin/python
import sys

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
		"f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
		"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
		"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
		"x": 8, "z": 10}

def main():
	#Call list_words() function and set the return to words
	words = list_words()
	#set rack to the command line input	
	rack = sys.argv[1]
	#Call testing function set return to correct
	correct = testing(rack, words)
	#For every word in correct iterate and print with word score
	for i in correct:
		print("%s: %s" %(word_count(i), i))

def list_words():
	#Open file with words in and split them into words
	with open("sowpods.txt", "r") as file:
		words = file.read().split()
	#Return words
	return words

def word_count(word):
	#Set count to 0		
	count = 0
	#iterate over word and add letter scores to count
	for i in word.lower():
		count += scores[i]
	return count

def testing(rack, words):
	#Inirialise correct, temper
	correct = []
	temper = []
	#Iterate over the letters in rack and add to temper list
	for i in rack:
		temper.append(i.lower())
	#Iterate over all words given
	for i in words:
		#Assign temper to temps use copy so it creates a new list
		temps = list(temper)
		#Set right to true
		right = True
		#Iterate over the letters in the word	
		for x in range(0, len(i)):
			#If the letter(lowercase) is in temps remove it
			if i[x].lower() in temps:
				temps.remove(i[x].lower())
			#Else set right to false and break
			else:
				right = False
				pass
		#If right is still true add the word to correct
		if right:
			correct.append(i)
	return correct

if __name__ == "__main__":
	if sys.argv > 1:
		main()