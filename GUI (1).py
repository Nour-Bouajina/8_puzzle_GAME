import pygame
import sys
from DFS import *
import time
from LDFS import *
from BFS import *
from A_star import *

# Define constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
CELL_SIZE = 100
GRID_WIDTH = 3
GRID_HEIGHT = 3
BUTTON_WIDTH = 80
BUTTON_HEIGHT = 30
FONT_SIZE = 18

# Define colors
WHITE = (241, 247, 237)
BLACK = (0, 0, 0)
PINK = (179, 57, 81)
GREEN = (204, 0, 153)
YELLOW = (227, 208, 129)
ORANGE =(243, 172, 234)

# Initialize Pygame
pygame.init()

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Grid")

# Load the font
font = pygame.font.Font(None, FONT_SIZE)

# Define the buttons
reset_button = pygame.Rect((WINDOW_WIDTH - BUTTON_WIDTH) / 2, 320, BUTTON_WIDTH, BUTTON_HEIGHT)
dfs_button = pygame.Rect(30, 360, BUTTON_WIDTH, BUTTON_HEIGHT)
bfs_button = pygame.Rect(120, 360, BUTTON_WIDTH, BUTTON_HEIGHT)
dfsl_button = pygame.Rect(210, 360, BUTTON_WIDTH, BUTTON_HEIGHT)
a_star_button = pygame.Rect(300, 360, BUTTON_WIDTH, BUTTON_HEIGHT)

# Define the text variables
closed_count_text = "Closed Nodes: "
all_count_text = "Explored Nodes: "
closed_count = 0
all_count = 0


init_grid = [[1, 2, 3], [' ', 4, 5], [8, 7, 6]]

# Define the grid values
grid_values = init_grid

# Define the grid update function
def update_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            cell_value = str(grid_values[y][x])
            cell_text = font.render(cell_value, True, BLACK)
            cell_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(window, GREEN, cell_rect)
            pygame.draw.rect(window, BLACK, cell_rect, 1)
            cell_text_rect = cell_text.get_rect(center=cell_rect.center)
            window.blit(cell_text, cell_text_rect)

# Define the button update function
def update_buttons():
    reset_text = font.render("Reset", True, PINK)
    dfs_text = font.render("DFS", True, BLACK)
    bfs_text = font.render("BFS", True, BLACK)
    dfsl_text = font.render("DFSL", True, BLACK)
    a_star_text = font.render("A*", True, BLACK)
    reset_text_rect = reset_text.get_rect(center=reset_button.center)
    dfs_text_rect = dfs_text.get_rect(center=dfs_button.center)
    bfs_text_rect = bfs_text.get_rect(center=bfs_button.center)
    dfsl_text_rect = dfsl_text.get_rect(center=dfsl_button.center)
    a_star_text_rect = a_star_text.get_rect(center=a_star_button.center)
    pygame.draw.rect(window, PINK, reset_button, 1)
    pygame.draw.rect(window, GREEN, dfs_button)
    pygame.draw.rect(window, GREEN, bfs_button)
    pygame.draw.rect(window, GREEN, dfsl_button)
    pygame.draw.rect(window, GREEN, a_star_button)
    pygame.draw.rect(window, BLACK, dfs_button, 1)
    pygame.draw.rect(window, BLACK, bfs_button, 1)
    pygame.draw.rect(window, BLACK, dfsl_button, 1)
    pygame.draw.rect(window, BLACK, a_star_button, 1)
    window.blit(reset_text, reset_text_rect)
    window.blit(dfs_text, dfs_text_rect)
    window.blit(bfs_text, bfs_text_rect)
    window.blit(dfsl_text, dfsl_text_rect)
    window.blit(a_star_text, a_star_text_rect)

# Define the text update function
def update_text():
    closed_count_text_obj = font.render(closed_count_text + str(closed_count),True, PINK)
    all_count_text_obj = font.render(all_count_text + str(all_count), True, PINK)
    closed_count_text_rect = closed_count_text_obj.get_rect(topleft=(10, 320))
    all_count_text_rect = all_count_text_obj.get_rect(topright=(WINDOW_WIDTH - 10, 320))
    window.blit(closed_count_text_obj, closed_count_text_rect)
    window.blit(all_count_text_obj, all_count_text_rect)


solver = None
curr_time = time.time()
while True:
# Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the buttons were clicked
            if reset_button.collidepoint(event.pos):
                grid_values = init_grid
                solver = None
            elif dfs_button.collidepoint(event.pos):
                solver = dfs(grid_values)
            elif bfs_button.collidepoint(event.pos):
                solver = bfs(grid_values)
            elif dfsl_button.collidepoint(event.pos):
                solver = dfsl(grid_values)
            elif a_star_button.collidepoint(event.pos):
                solver = A_star(grid_values)
    if solver is not None and time.time() - curr_time > 1 :
        curr_time = time.time()
        solver.inc()
        grid_values = solver.show
        
        if solver.sucess or len(solver.freeNodes) == 0:            
            closed_count = len(solver.closedNondes) 
            all_count = solver.states_explored
            solver = None
    
    window.fill(ORANGE)
    update_grid()
    update_buttons()
    update_text()
    
    pygame.display.update()
