#! /bin/bash/python3
global no_of_moves
no_of_moves = 0
print("Welcome to the blindfold tic-tac-toe game!!")

print("The game will not have a graphic display and the tic-tac-toe board has to be simulated in the mind")
print("The board representation is same as the chess board. The horizontal rows are represented by 1,2,3")
print("The vertical columns are represented by alphabets A,B,C")
print('''
			3 _ | _ | _
			2 _ | _ | _
			1   |   | 
			  A   B   C
     ''')
print("The move is played by mentioning the position on the board ex:A1")
print("The first player starts with cross \'X\' and the next player is \'O\' ")
print("Let's begin the game")
board_dict = {'a1':'','a2':'','a3':'','b1':'','b2':'','b3':'','c1':'','c2':'','c3':''}
def check_function():
	print(board_dict)
	if no_of_moves > 9:
		return -1
	# Checks the winning position
	if( board_dict['a1'] == board_dict['a2'] == board_dict['a3']):
		return True
	elif( board_dict['a1'] == board_dict['a2'] == board_dict['a3']):
		return True
	elif( board_dict['b1'] == board_dict['b2'] == board_dict['b3']):
		return True
	elif( board_dict['c1'] == board_dict['c2'] == board_dict['c3']):
		return True
	elif( board_dict['a1'] == board_dict['b1'] == board_dict['c1']):
		return True
	elif( board_dict['a2'] == board_dict['b2'] == board_dict['c2']):
		return True
	elif( board_dict['a3'] == board_dict['b3'] == board_dict['c3']):
		return True
	elif( board_dict['a1'] == board_dict['b2'] == board_dict['c3']):
		return True
	elif( board_dict['a3'] == board_dict['b2'] == board_dict['c1']):
		return True
	else:
		return False
print(board_dict)
while(check_function() != False):
	print("Entered loop")
	p1_pos = input("Enter the first player position")
	board_dict[p1_pos.lower()] = 'X'
	no_of_moves = no_of_moves + 1
	p2_pos = input("Enter the second player position")
	board_dict[p2_pos.lower()] = 'O'
	no_of_moves = no_of_moves + 1
print("We have a winner")	
