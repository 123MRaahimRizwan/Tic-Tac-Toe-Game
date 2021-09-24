"""
Project : Tic Tac Toe Game
@author : M.Raahim Rizwan
This project is made with the help of a youtube video. Below is the link:
https://www.youtube.com/playlist?list=PLr-iRXN7HiJgJzMX22AVw4IU8ZOR4JS97
"""

# Importing the libraries
import pygame
import sys
import numpy as np
# Initializing pygame
pygame.init()
# Game constants
HEIGHT = 600
WIDTH = 600
LINE_WIDTH = 15
RED = (255,0,0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23,145,135)
BOARD_ROWS = 3
BOARD_COLUMNS = 3
CIRCLE_WIDTH = 15
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
CROSS_WIDTH = 25
SQUARE_SIZE = WIDTH//BOARD_COLUMNS
CIRCLE_RADIUS = SQUARE_SIZE//3
SPACE = SQUARE_SIZE//4
# Setting up the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
# Setting the title
pygame.display.set_caption("Tic Tac Toe")
# Setting up the icon
icon = pygame.image.load('Asset/icon.ico')
pygame.display.set_icon(icon)
# Filling background color
window.fill(BG_COLOR)

# Board
board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))

def draw_lines():
    """
    Drawing board lines.
    """
    # 1st horizontal line
    pygame.draw.line(window, LINE_COLOR, (0,SQUARE_SIZE), (WIDTH,SQUARE_SIZE), LINE_WIDTH)
    # 2nd horizontal line
    pygame.draw.line(window, LINE_COLOR, (0,SQUARE_SIZE*2), (WIDTH,SQUARE_SIZE*2), LINE_WIDTH)
    # 1st vertical line
    pygame.draw.line(window, LINE_COLOR, (SQUARE_SIZE,0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # 2nd vertical line
    pygame.draw.line(window, LINE_COLOR, (SQUARE_SIZE*2,0), (SQUARE_SIZE*2, HEIGHT), LINE_WIDTH)

def draw_figures():
    """
    Drawing circles and crosses (O, X).
    """
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 1:
                pygame.draw.circle(window, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), int(row * SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(window, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(window, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)


def mark_square(row, col, player):
    """
    Marking the square to be player.
    """
    board[row][col] = player

def available_square(row, col):
    """
    Setting the boards' rows and columns to be 0.
    """
    return board[row][col] == 0

def board_full():
    """
    Determining whether the board is full or not.
    """
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    """
    Checking Win Event.
    """
    # Checking vertical win
    for col in range(BOARD_COLUMNS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    # Checking horizontal win 
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    # Checking ascending diagonal win
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_ascending_diagonal(player)
        return True
    # Checking descending diagonal win 
    if board[0][0] == player and board[1][1] == player and board [2][2] == player:
        draw_descending_diagonal(player)
        return True
    return False

def draw_vertical_winning_line(col, player):
    """
    Drawing vertical winning line.
    """
    pos_x = col * SQUARE_SIZE + SQUARE_SIZE//2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(window, color, (pos_x, 15), (pos_x, HEIGHT - 15), 15)

def draw_horizontal_winning_line(row, player):
    """
    Drawing horizontal winning line.
    """
    pos_y = row * SQUARE_SIZE + SQUARE_SIZE//2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(window, color, (15,pos_y), (WIDTH - 15, pos_y), 15)

def draw_ascending_diagonal(player):
    """
    Drawing ascending diagonal line (\).
    """
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(window, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)
def draw_descending_diagonal(player):
    """
    Drawing descending diagonal line (/).
    """
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(window, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

def restart():
    """
    Restarting the game.
    """
    window.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            board[row][col] = 0

draw_lines()

player = 1
game_over = False

# Main game loop
run = True
while run:
    # Checking for the events in the whole game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        # Checking for the keys pressed by the mouse
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            clicked_row = int(mouse_y // SQUARE_SIZE)
            clicked_column = int(mouse_x // SQUARE_SIZE)

            if available_square(clicked_row, clicked_column):
                mark_square(clicked_row, clicked_column, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1
 
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                restart()
                player = 1
                game_over = False
    # Updating the screen
    pygame.display.update()


