import pygame
import sys

# Initialize Pygame
pygame.init()

# Board settings
WIDTH = 700
HEIGHT = 700
LINE_WIDTH = 15
BOARD_SIZE = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Font settings
FONT_SIZE = 40
font = pygame.font.Font(None, FONT_SIZE)

# Game window settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Class representing the board
class Board:
    def __init__(self):
        self.grid = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.current_player = "X"
        self.game_over = False

    def draw_lines(self):
        gap = WIDTH // BOARD_SIZE
        for i in range(1, BOARD_SIZE):
            pygame.draw.line(screen, BLACK, (0, i * gap), (WIDTH, i * gap), LINE_WIDTH)
            pygame.draw.line(screen, BLACK, (i * gap, 0), (i * gap, HEIGHT), LINE_WIDTH)

    def draw_figures(self):
        gap = WIDTH // BOARD_SIZE
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.grid[row][col] == "X":
                    pygame.draw.line(screen, BLACK, (col * gap + gap // 4, row * gap + gap // 4),
                                     (col * gap + gap - gap // 4, row * gap + gap - gap // 4), LINE_WIDTH)
                    pygame.draw.line(screen, BLACK, (col * gap + gap // 4, row * gap + gap - gap // 4),
                                     (col * gap + gap - gap // 4, row * gap + gap // 4), LINE_WIDTH)
                elif self.grid[row][col] == "O":
                    pygame.draw.circle(screen, BLACK, (col * gap + gap // 2, row * gap + gap // 2), gap // 3, LINE_WIDTH)

    def mark_square(self, row, col):
        if not self.game_over and self.grid[row][col] is None:
            self.grid[row][col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"

    def is_winner(self, player):
        # Check horizontal rows
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE - 4):
                if all(self.grid[row][col+i] == player for i in range(5)):
                    return True

        # Check vertical rows
        for col in range(BOARD_SIZE):
            for row in range(BOARD_SIZE - 4):
                if all(self.grid[row+i][col] == player for i in range(5)):
                    return True

        # Check diagonals (\)
        for row in range(BOARD_SIZE - 4):
            for col in range(BOARD_SIZE - 4):
                if all(self.grid[row+i][col+i] == player for i in range(5)):
                    return True

        # Check diagonals (/)
        for row in range(4, BOARD_SIZE):
            for col in range(BOARD_SIZE - 4):
                if all(self.grid[row-i][col+i] == player for i in range(5)):
                    return True

        return False

    def is_full(self):
        for row in self.grid:
            if None in row:
                return False
        return True

    def reset(self):
        self.grid = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.current_player = "X"
        self.game_over = False


# Initialize the board
board = Board()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // (HEIGHT // BOARD_SIZE)
                clicked_col = mouseX // (WIDTH // BOARD_SIZE)
                board.mark_square(clicked_row, clicked_col)
                if board.game_over:
                    board.reset()

    screen.fill(WHITE)
    board.draw_lines()
    board.draw_figures()

    if board.is_winner("X"):
        text = font.render("Player X wins!", True, RED)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        board.game_over = True
    elif board.is_winner("O"):
        text = font.render("Player O wins!", True, RED)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        board.game_over = True
    elif board.is_full():
        text = font.render("Draw!", True, RED)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        board.game_over = True

    pygame.display.update()
