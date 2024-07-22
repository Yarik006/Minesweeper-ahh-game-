import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
GRID_SIZE = 10
CELL_SIZE = 40
BOMB_COUNT = 10
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Сапер')

font = pygame.font.Font(None, 36)


bomb_image = pygame.image.load('bomb.jpg') 
flag_image = pygame.image.load('flag.jpg') 


bomb_sound = pygame.mixer.Sound('bomb_sound.mp3')  
pygame.mixer.init()
pygame.mixer.music.load('Nujabes - Aruarian Dance.mp3')
pygame.mixer.music.play()
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  
revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  
flags = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  


bombs = random.sample(range(GRID_SIZE * GRID_SIZE), BOMB_COUNT)
for bomb in bombs:
    x, y = bomb % GRID_SIZE, bomb // GRID_SIZE
    grid[x][y] = -1 


for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if grid[i][j] == -1:
            continue
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= i + dx < GRID_SIZE and 0 <= j + dy < GRID_SIZE:
                    count += (grid[i + dx][j + dy] == -1)
        grid[i][j] = count


running = True
game_over = False  

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not game_over: 
                x, y = event.pos
                grid_x, grid_y = x // CELL_SIZE, y // CELL_SIZE
                if grid[grid_x][grid_y] == -1: 
                    bomb_sound.play()  
                    game_over = True  
                revealed[grid_x][grid_y] = True  
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            x, y = event.pos
            grid_x, grid_y = x // CELL_SIZE, y // CELL_SIZE
            flags[grid_x][grid_y] = not flags[grid_x][grid_y]  

    
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            rect = pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)  

            if revealed[i][j]:
                if grid[i][j] == -1:
                 
                    screen.blit(bomb_image, (i * CELL_SIZE + CELL_SIZE // 2 - bomb_image.get_width() // 2,
                                             j * CELL_SIZE + CELL_SIZE // 2 - bomb_image.get_height() // 2))
                else:
                   
                    text = font.render(str(grid[i][j]), True, BLACK)
                    text_rect = text.get_rect(center=(i * CELL_SIZE + CELL_SIZE // 2,
                                                      j * CELL_SIZE + CELL_SIZE // 2))
                    screen.blit(text, text_rect)
            elif flags[i][j]:
               
                screen.blit(flag_image, (i * CELL_SIZE + CELL_SIZE // 2 - flag_image.get_width() // 2,
                                         j * CELL_SIZE + CELL_SIZE // 2 - flag_image.get_height() // 2))

    if game_over:
        
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT), 0)

    pygame.display.flip()  

pygame.quit() 
