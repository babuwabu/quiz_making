# Welcome message
print("Lulu's Quiz Maker")    
print("Please input your questions!")

# Initialize the loop
add_question = "yes"

# Ask for file name before the loop so all questions go into the same file
name = input("Enter your text file name (e.g. quiz.txt): ")

while add_question.lower() == "yes":
    # User inputs the question and choices
    q = input("Question: ")
    a = input("a) ")
    b = input("b) ")
    c = input("c) ")
    d = input("d) ")

    # Input the correct answer
    ans = input("Choose the correct answer from (a/b/c/d): ")

    # Validate answer and convert to lowercase
    if ans.lower() in ['a', 'b', 'c', 'd']:
        correct_answer = ans.lower()

        # Save to file
        with open(name, "a") as file:
            file.write("_..--''``---....__   ...    __\n")
            file.write(" /// //_.-'    .-/\";          ``<._  ``.''_ . / // /\n")
            file.write("///_.-' ..--.'    \\       LOU          `( ) ) // //\n")
            file.write("/ (..-' // (< _     ;..__               ; `' / ///\n")
            file.write(" / // // //  `-._,_)' // / ``--...____..-' /// / //\n")
            
            file.write("::QUESTION::\n")
            file.write(q + "\n")
            file.write("a) " + a + "\n")
            file.write("b) " + b + "\n")
            file.write("c) " + c + "\n")
            file.write("d) " + d + "\n")
            file.write("ANSWER: " + correct_answer + "\n")
            file.write("::END::\n\n")
    else:
        print("Invalid input! Please choose a valid option (a/b/c/d).")
        continue  # Skip saving and repeat the loop

    # Ask if the user wants to add another question
    add_question = input("Add another question? (yes/no): ")

print("Done. Your questions have been saved to", name)

# Make it into a pygame
import pygame
import sys

pygame.init()

# Initialize Pygame window and font
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lulu's Quiz Maker")

font = pygame.font.SysFont(None, 30)
large_font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)

# Ask user for the file name using text input
# While the user wants to add questions:
# Show input fields for: Question, Choice a,b,c, and d, and Correct answer (a/b/c/d)
# Let the user navigate between fields (e.g. Tab key)
# Validate correct answer is one of a/b/c/d
# Save question and choices to the file
# Ask if user wants to add another question
# If user says no, quit