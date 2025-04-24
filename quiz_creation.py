# Make it into a pygame
import pygame
import sys

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("02. Title Theme.mp3") 
pygame.mixer.music.set_volume(0.3)      
pygame.mixer.music.play(-1)     

# Initialize Pygame window and font
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lulu's Quiz Maker")

# Load pixel background and scale to screen
bg_image = pygame.image.load("pixel forest.jpg")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# Load pixel font
font = pygame.font.Font("PressStart2P-Regular.ttf", 18)
large_font = pygame.font.Font("PressStart2P-Regular.ttf", 24)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 150, 255)

# Ask user for the file name using text input
labels = ["Question", "a)", "b)", "c)", "d)", "Correct Answer (a/b/c/d)"] # Labels
inputs = [""] * len(labels)
current_input = 0
name = ""

# App states
file_named = False
adding_question = True
show_saved_message = False

def draw_text(text, x, y, font, color=BLACK):
    text_surf = font.render(text, True, color)
    screen.blit(text_surf, (x, y))

def save_question_to_file(name, data):
    with open(name, "a") as file:
        file.write("_..--''``---....__   ...    __\n")
        file.write(" /// //_.-'    .-/\";          ``<._  ``.''_ . / // /\n")
        file.write("///_.-' ..--.'    \\       LOU          `( ) ) // //\n")
        file.write("/ (..-' // (< _     ;..__               ; `' / ///\n")
        file.write(" / // // //  `-._,_)' // / ``--...____..-' /// / //\n")
        file.write("::QUESTION::\n")
        file.write(data[0] + "\n")
        file.write("a) " + data[1] + "\n")
        file.write("b) " + data[2] + "\n")
        file.write("c) " + data[3] + "\n")
        file.write("d) " + data[4] + "\n")
        file.write("ANSWER: " + data[5].lower() + "\n")
        file.write("::END::\n\n")

# While the user wants to add questions:
running = True
while running:
    screen.blit(bg_image, (0, 0))

    if not file_named:
        draw_text("Enter filename (e.g. quiz.txt):", 40, 50, large_font, WHITE)
        draw_text(name, 40, 100, font, BLUE)
    # Show input fields for: Question, Choice a,b,c, and d, and Correct answer (a/b/c/d)
    elif adding_question:
        draw_text("Enter your question and answers:", 40, 30, large_font, WHITE)
        for i, label in enumerate(labels):
            draw_text(f"{label} {inputs[i]}", 40, 80 + i * 50, font, BLUE if i == current_input else WHITE)
        draw_text("ENTER = Save | TAB = Next | ESC = Quit", 40, 440, font, WHITE)
    elif show_saved_message:
        draw_text("Saved! Add another? (y/n)", 40, 500, large_font, WHITE)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Let the user navigate between fields (e.g. Tab key)
        elif event.type == pygame.KEYDOWN:
            if not file_named:
                if event.key == pygame.K_RETURN and name.strip():
                    file_named = True
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
            # Ask if user wants to add another question
            elif adding_question:
                if event.key == pygame.K_RETURN:
                    if all(inputs) and inputs[5].lower() in ['a', 'b', 'c', 'd']:
                        save_question_to_file(name, inputs) # Save question and choices to the file
                        show_saved_message = True
                        adding_question = False
                    else:
                        print("Please fill all fields and enter a valid correct answer (a/b/c/d).") # Validate correct answer is one of a/b/c/d
                elif event.key == pygame.K_TAB:
                    current_input = (current_input + 1) % len(inputs)
                elif event.key == pygame.K_BACKSPACE:
                    inputs[current_input] = inputs[current_input][:-1]
                elif event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    inputs[current_input] += event.unicode

            elif show_saved_message:
                if event.key == pygame.K_y:
                    inputs = [""] * len(labels)
                    current_input = 0
                    adding_question = True
                    show_saved_message = False
                elif event.key == pygame.K_n: # If user says no, quit
                    running = False

    clock.tick(30)

pygame.quit()
sys.exit()