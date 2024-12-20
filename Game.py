import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Rock-Paper-Scissors")
if getattr(sys, 'frozen', False):
    # If we're running from a packaged executable, get the path to the executable
    base_path = sys._MEIPASS
else:
    # Otherwise, use the script's directory
    base_path = os.path.dirname(__file__)

# Construct the path to your image
rock_img_path = os.path.join(base_path, "fist.png")
paper_img_path = os.path.join(base_path, "hand-paper.png")
scissors_img_path = os.path.join(base_path, "scissors.png")

# Load the images
rock_img = pygame.image.load(rock_img_path)
paper_img = pygame.image.load(paper_img_path)
scissors_img = pygame.image.load(scissors_img_path)

# Resize images
rock_img = pygame.transform.scale(rock_img, (100, 100))
paper_img = pygame.transform.scale(paper_img, (100, 100))
scissors_img = pygame.transform.scale(scissors_img, (100, 100))

# Font setup
font = pygame.font.Font(None, 36)

# Game variables
choices = ["Rock", "Paper", "Scissors"]
player_choice = None
computer_choice = None
result = None

# Function to display text on the screen
def display_text(text, x, y, color=(0, 0, 0)):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# Function to get the image corresponding to the choice
def get_image(choice):
    if choice == "Rock":
        return rock_img
    elif choice == "Paper":
        return paper_img
    elif choice == "Scissors":
        return scissors_img
    return None

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))  # White background
    
    # Display player options
    display_text("Choose Your Move:", 200, 50)
    screen.blit(rock_img, (50, 100))  # Rock button
    screen.blit(paper_img, (250, 100))  # Paper button
    screen.blit(scissors_img, (450, 100))  # Scissors button

    # Display opponent's choice
    if computer_choice:
        display_text("Opponent's Choice:", 200, 230)
        opponent_image = get_image(computer_choice)
        if opponent_image:
            screen.blit(opponent_image, (250, 250))  # Display opponent choice image below text

    # Display the result
    if result:
        display_text(f"Result: {result}", 200, 360)  # Move Result text further down below opponent image

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            
            # Detect player's choice
            if 50 <= mouse_x <= 150 and 100 <= mouse_y <= 200:
                player_choice = "Rock"
            elif 250 <= mouse_x <= 350 and 100 <= mouse_y <= 200:
                player_choice = "Paper"
            elif 450 <= mouse_x <= 550 and 100 <= mouse_y <= 200:
                player_choice = "Scissors"
            
            if player_choice:
                # Determine computer's choice and the result
                computer_choice = random.choice(choices)
                if player_choice == computer_choice:
                    result = "It's a Draw!"
                elif (player_choice == "Rock" and computer_choice == "Scissors") or \
                     (player_choice == "Paper" and computer_choice == "Rock") or \
                     (player_choice == "Scissors" and computer_choice == "Paper"):
                    result = "You Win!"
                else:
                    result = "You Lose!"
    
    pygame.display.flip()

pygame.quit()
sys.exit()