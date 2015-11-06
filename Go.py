import pygame
from pygame.locals import *



def player_move(turn):

	if turn % 2 == 0: # turn is incremented once per turn. By evaluating odd or even we can determine whose turn it is to play.
		player = 1
	else:
		player = 2
	# the below code is temporary until I can figure out a GUI to play on
	#play_pass = raw_input("Play or pass: ").lower()
	#if play_pass != "pass":
	return player

def make_board():
	# this makes our board. each index holds a piece with 3 (so far) values. Piece value. Vertical Index. Horizontal Index.
	board = [[[0, y, x] for x in range(0,19)]for y in range(0,19)]
	# y is vertical (index[1]) x is horizontal (index[2]).
	return board

def print_board(board):
	# this function prints the board out
	for row in board:
		print row
   
   
def gameplay_logic(board, player):
	temp_dict = {} # temporary dictionary that is used for our search algorithm. HOLD ON. WHY DO WE NEED TO USE A DICTIONARY? LIST IS OK NO?
	count = 0 # counter is used to create unique dictionary keys.
	
	if player == 1:
		enemy_piece = 2
	else:
		enemy_piece = 1
		
	for row in board:
		for index in row:
			if index[0] == enemy_piece: # if an enemy piece is found in any index.
				print "ENEMY PIECE FOUND"
				temp_dict[count] = [index[0], index[1], index[2]]
				print temp_dict # add it to the temp_dict with the key being the current increment value of count.
				count += 1 # add one to the increment value so that next time there is a new key.
				search_all(count, enemy_piece, board, index[1], index[2], temp_dict) # run search_all() with the required arguments.
			else:
				pass
	       	
def search_all(count, enemy_piece, board, vertical_index, horizontal_index, temp_dict):
	found = True
	while found: # while found is true
		found = False # set it to false by default
		for key in range(0, count):

			# searches for enemy pieces directly to the right of all items in the dictionary.
			found_right_piece = search_right(enemy_piece, board, temp_dict[key][1], temp_dict[key][2])

			if found_right_piece: # if the value is real, not empty
				print "PIECE TO THE RIGHT OF THIS ONE"
				temp_dict[count] = [found_right_piece[0], found_right_piece[1], found_right_piece[2]] # add it to our dictionary
				count += 1
				found = True # set found to True so the program knows to loop again to make sure everything is covered.

		for key in range(0, count):
			found_down_piece = search_down(enemy_piece, board, temp_dict[key][1], temp_dict[key][2])
			if found_down_piece:
				temp_dict[count] = [found_down_piece[0], found_down_piece[1], found_down_piece[2]]
				count += 1
  				found = True

  		for key in range(0, count):
			found_left_piece = search_left(enemy_piece, board, temp_dict[key][1], temp_dict[key][2])
    		if found_left_piece:
    			temp_dict[count] = [found_left_piece[0], found_left_piece[1], found_left_piece[2]]
    			count += 1
    			found = True

		for key in range(0, count):
			found_up_piece = search_up(enemy_piece, board, temp_dict[key][1], temp_dict[key][2])
			if found_up_piece:
				temp_dict[count] = [found_up_piece[0], found_up_piece[1], found_up_piece[2]]
				count += 1
				found = True

def search_right(enemy_piece, board, vertical_index, horizontal_index):
	found_piece = board[vertical_index][horizontal_index+1]
    	if found_piece == enemy_piece:
      		return found_piece # THIS WILL BE ADDED TO OUR DICTIONARY
      
def search_down(enemy_piece, board, vertical_index, horizontal_index):
  	found_piece = board[vertical_index-1][horizontal_index]
    	if found_piece == enemy_piece:
      		return found_piece # THIS WILL BE ADDED TO OUR DICTIONARY

def search_left(enemy_piece, board, vertical_index, horizontal_index):
  	found_piece = board[vertical_index][horizontal_index-1]
    	if found_piece == enemy_piece:
      		return found_piece # THIS WILL BE ADDED TO OUR DICTIONARY

def search_up(enemy_piece, board, vertical_index, horizontal_index):
  	found_piece = board[vertical_index+1][horizontal_index]
    	if found_piece == enemy_piece:
      		return found_piece # THIS WILL BE ADDED TO OUR DICTIONARY
      		
      		
      		
def mouse_processing():
    board_position_x = "no click"
    board_position_y = "no click"
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            board_position_x = mouse_position[0] / 50
            board_position_y = mouse_position[1] / 50
            print "\nHORIZONTAL" + str(board_position_x)
            print "VERTICAL" + str(board_position_y)
            break
      	else:
      	    pass
    return board_position_x, board_position_y    
      		
def circle_generate(screen, position_x, position_y, player, board):
    if player == 1:
        colour = (0,0,0)
    else:
    	colour = (255,255,255)

    for row in board
        for i in row
    	    if i[0] = 1 or i[0] = 2:
    	    	pygame.draw.circle(screen, colour, (25 + position_x * 50, 25 + position_y * 50), 25, 0) 
    	    	
    
    
    #if player == 1:
    #    colour = (0,0,0)
    #else:
    #	colour = (255,255,255)
    #pygame.draw.circle(screen, colour, (25 + position_x * 50, 25 + position_y * 50), 25, 0) 


def main():
	pygame.init()
	screen = pygame.display.set_mode((950,950))
	go_graph_board = pygame.image.load('Blank_Go_board.png')
	stop_play = False
	board = make_board()
	turn = 0
	screen.blit(go_graph_board, (0, 0))
	
	while not stop_play:
	    pygame.display.update()
	    player = player_move(turn)
	    
	    position_x, position_y = mouse_processing()
	    if position_x == "no click":
		continue
	    else:
		circle_generate(screen, position_x, position_y, player, board)

		   
	        
	        board[position_y][position_x][0] = player
	        
	        #print "TURN: {}".format(turn)
	        pygame.display.update()
	        gameplay_logic(board, player)
		
		print_board(board)
	        print "\n\n"
	        turn += 1
	        print turn
	        print player

main()


