import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 30

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# Clock
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 55)
small_font = pygame.font.SysFont(None, 35)

# Buttons setup
button_width = 200
button_height = 100
rock_button = pygame.Rect((50, SCREEN_HEIGHT - 150), (button_width, button_height))
paper_button = pygame.Rect((300, SCREEN_HEIGHT - 150), (button_width, button_height))
scissors_button = pygame.Rect((550, SCREEN_HEIGHT - 150), (button_width, button_height))

# Choices
choices = ["rock", "paper", "scissors"]
computer_choice = None
human_choice = None
result = ""
round_number = 1
human_win = 0
computer_win = 0
draw = 0
game_over = False

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def display_result():
    global human_choice, computer_choice, result
    draw_text(f"Human: {human_choice}", small_font, BLACK, screen, SCREEN_WIDTH // 2, 200)
    draw_text(f"Computer: {computer_choice}", small_font, BLACK, screen, SCREEN_WIDTH // 2, 250)
    draw_text(result, small_font, BLACK, screen, SCREEN_WIDTH // 2, 300)
    pygame.display.flip()
    time.sleep(2)  # Delay to show result
    human_choice = None  # Reset human choice after displaying result

def main():
    global computer_choice, human_choice, result, round_number, human_win, computer_win, draw, game_over
    running = True

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if rock_button.collidepoint(event.pos):
                    human_choice = "rock"
                elif paper_button.collidepoint(event.pos):
                    human_choice = "paper"
                elif scissors_button.collidepoint(event.pos):
                    human_choice = "scissors"
                
                if human_choice:
                    computer_choice = random.choice(choices)
                    if computer_choice == human_choice:
                        result = "Draw!!!"
                        draw += 1
                    elif (computer_choice == "rock" and human_choice == "scissors") or \
                         (computer_choice == "paper" and human_choice == "rock") or \
                         (computer_choice == "scissors" and human_choice == "paper"):
                        result = "Computer wins!!!"
                        computer_win += 1
                    else:
                        result = "Human wins!!!"
                        human_win += 1
                    round_number += 1
                    display_result()

        draw_text("Rock Paper Scissors", font, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text(f"Round: {round_number}", small_font, BLACK, screen, SCREEN_WIDTH // 2, 100)

        if round_number <= 3:
            pygame.draw.rect(screen, RED, rock_button)
            draw_text("Rock", small_font, WHITE, screen, rock_button.centerx, rock_button.centery)
            pygame.draw.rect(screen, GREEN, paper_button)
            draw_text("Paper", small_font, WHITE, screen, paper_button.centerx, paper_button.centery)
            pygame.draw.rect(screen, BLUE, scissors_button)
            draw_text("Scissors", small_font, WHITE, screen, scissors_button.centerx, scissors_button.centery)
        else:
            game_over = True
            draw_text("Match Completed!!!", font, BLACK, screen, SCREEN_WIDTH // 2, 400)
            draw_text(f"Human points: {human_win}", small_font, BLACK, screen, SCREEN_WIDTH // 2, 450)
            draw_text(f"Computer points: {computer_win}", small_font, BLACK, screen, SCREEN_WIDTH // 2, 500)
            draw_text(f"Draws: {draw}", small_font, BLACK, screen, SCREEN_WIDTH // 2, 550)
            pygame.display.flip()
            time.sleep(3)  # Display final scores for 3 seconds
            running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
