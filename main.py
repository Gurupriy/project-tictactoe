#! /bin/bash/python3
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
board_dict = {'a1':'1','a2':'2','a3':'3','b1':'4','b2':'5','b3':'6','c1':'7','c2':'8','c3':'9a1'}
def check_function():
	print(board_dict)
	# Checks the winning position
	if( board_dict['a1'] == board_dict['a2'] == board_dict['a3']):
		print('c1')
		return True
	elif( board_dict['b1'] == board_dict['b2'] == board_dict['b3']):
		print('c3')
		return True
	elif( board_dict['c1'] == board_dict['c2'] == board_dict['c3']):
		print('c4')
		return True
	elif( board_dict['a1'] == board_dict['b1'] == board_dict['c1']):
		print('c5')
		return True
	elif( board_dict['a2'] == board_dict['b2'] == board_dict['c2']):
		print('c6')
		return True
	elif( board_dict['a3'] == board_dict['b3'] == board_dict['c3']):
		print('c7')
		return True
	elif( board_dict['a1'] == board_dict['b2'] == board_dict['c3']):
		print('c8')
		return True
	elif( board_dict['a3'] == board_dict['b2'] == board_dict['c1']):
		print('c9')
		return True
	else:
		print('f1')
		return False
print(board_dict)

for no_of_moves in range(9):
	p1_pos = input("Enter the first player position")
	board_dict[p1_pos.lower()] = 'X'
	print(board_dict)
	if True == check_function():
		Winner = 'P1'
		break
	p2_pos = input("Enter the second player position")
	board_dict[p2_pos.lower()] = 'O'
	print(board_dict)
	if True == check_function():
		Winner = 'P2'
		break
print('We have winner' + Winner)