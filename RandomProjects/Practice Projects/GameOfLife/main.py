#Game Of Life

import os

#Get's the terminal size
column, row = os.get_terminal_size()

#Create an array of Spaces the height and width of the terminal
arrs = [[" "] * column for i in range(row)]

#Define Board as an empty string
Board = ""

#Transform the array into a single string
for i in arrs:
	for charr in i: 
		Board += charr

#Detect the operating system and clears terminal with apropriate command
os.system('cls' if os.name == 'nt' else 'clear')

print(Board)