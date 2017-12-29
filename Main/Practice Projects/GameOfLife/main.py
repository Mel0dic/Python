#Game Of Life

#Get's the terminal size
column, row = os.get_terminal_size()

#Create an array of Spaces the height and width of the terminal
arrs = [[" "] * column for i in range(row)]

