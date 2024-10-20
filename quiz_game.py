import tkinter as tk
import random
import json
from PIL import Image, ImageTk 

with open('questions.json', 'r') as file:
    quiz = json.load(file)

# Initialize global variables
score = 0
question_index = 0
selected_questions = []
fifty_percent_used = False
two_chances_used = False
selected_two_chances = []

# Create main window
root = tk.Tk()
root.title("Quiz Game")
root.geometry("400x500")  # Adjusted size to accommodate images
root.configure(bg="white")  # Set the background color of the main window to white


# Function to start the quiz
def start_quiz():
    global selected_questions, question_index, score
    selected_difficulty = difficulty_var.get()
    selected_questions = random.sample(list(quiz[selected_difficulty].items()), 10)
    question_index = 0
    score = 0
    
    # Reset joker usage for a new game
    global fifty_percent_used, two_chances_used
    fifty_percent_used = False
    two_chances_used = False
    
    difficulty_frame.pack_forget()
    quiz_frame.pack(pady=20)
    display_question()

# Function to eliminate two incorrect options
def fifty_percent_joker():
    global fifty_percent_used
    if not fifty_percent_used:
        question, data = selected_questions[question_index]
        options = data['options']
        correct_answer = data['answer']

        # Randomly select two incorrect options to mark them as non-clickable
        incorrect_options = [opt for opt in options if opt != correct_answer]
        options_to_remove = random.sample(incorrect_options, 2)

        for i, option in enumerate(options):
            if option in options_to_remove:
                option_buttons[i].config(bg="red", state="disabled")  # Change color to red and disable

        fifty_percent_used = True  # Mark the joker as used
        update_joker_buttons()

# Function for the Two Chances Joker
def two_chances_joker():
    global two_chances_used, selected_two_chances
    if not two_chances_used:
        selected_two_chances = []  # Reset selected answers

        # Allow the user to select two answers
        for rb in option_buttons:
            rb.config(command=lambda option=rb: select_two_chances(option))
        
        two_chances_used = True  # Mark the joker as used

# Function to handle selection in Two Chances Joker
def select_two_chances(selected_option):
    global selected_two_chances
    selected_option.config(bg="yellow")  # Change color to yellow
    selected_two_chances.append(selected_option.cget("text"))

    # If two options are selected
    if len(selected_two_chances) == 2:
        check_two_chances_answer()

# Function to check the answer with Two Chances Joker
def check_two_chances_answer():
    global question_index, score, selected_two_chances
    correct_answer = selected_questions[question_index][1]['answer']

    # Check if at least one of the selected options is correct
    if selected_two_chances[0] == correct_answer or selected_two_chances[1] == correct_answer:
        score += 2.5
        result_label.config(text="Correct!")
    else:
        result_label.config(text=f"Wrong! The correct answer was: {correct_answer}")

    question_index += 1
    reset_answer_buttons()  # Reset button states for next question
    display_question()

# Difficulty selection frame
difficulty_frame = tk.Frame(root)
difficulty_frame.pack(pady=20)

intro_label = tk.Label(difficulty_frame, text="Welcome to the Fairy Quiz Game! Choose your difficulty level:", font=('Helvetica', 10))
intro_label.pack(pady=(0, 10))  # Add some padding below the label

intro_paragraph = tk.Label(difficulty_frame, text="Do the test to see which Winx fairy you are.", font=('Arial', 8))
intro_paragraph.pack(pady=(0, 10))

difficulty_var = tk.StringVar(value="easy")  # Default to easy

easy_rb = tk.Radiobutton(difficulty_frame, text="Easy", variable=difficulty_var, value="easy")
easy_rb.pack(anchor="w")
medium_rb = tk.Radiobutton(difficulty_frame, text="Medium", variable=difficulty_var, value="medium")
medium_rb.pack(anchor="w")
hard_rb = tk.Radiobutton(difficulty_frame, text="Hard", variable=difficulty_var, value="hard")
hard_rb.pack(anchor="w")

start_button = tk.Button(difficulty_frame, text="Start Quiz", command=start_quiz)
start_button.pack(pady=10)

# Quiz frame
quiz_frame = tk.Frame(root)

question_label = tk.Label(quiz_frame, text="", wraplength=300)
question_label.pack(pady=10)

selected_answer = tk.StringVar()
option_buttons = []

for i in range(4):
    rb = tk.Radiobutton(quiz_frame, text="", variable=selected_answer, value="", indicatoron=0)
    rb.pack(fill="x", padx=10, pady=5)
    option_buttons.append(rb)

result_label = tk.Label(quiz_frame, text="")
result_label.pack(pady=10)

score_label = tk.Label(quiz_frame, text="Score: 0")
score_label.pack(pady=10)

# Joker buttons (initially hidden)
fifty_percent_button = tk.Button(quiz_frame, text="50% Joker", command=fifty_percent_joker)
fifty_percent_button.pack(side="left", padx=10)
fifty_percent_button.pack_forget()  # Hide initially

two_chances_button = tk.Button(quiz_frame, text="Two Chances Joker", command=two_chances_joker)
two_chances_button.pack(side="left", padx=10)
two_chances_button.pack_forget()  # Hide initially

tk.Button(quiz_frame, text="Submit Answer", command=lambda: check_answer(selected_answer.get())).pack(pady=10)

# Function to display question
def display_question():
    global question_index
    reset_answer_buttons()  # Reset button states for a new question

    if question_index < len(selected_questions):
        question, data = selected_questions[question_index]
        question_label.config(text=question)
        for i, option in enumerate(data['options']):
            option_buttons[i].config(text=option, value=option, bg="white", state="normal")  # Reset button color and state
        score_label.config(text=f"Score: {score}")
        update_joker_buttons()  # Update joker buttons
    else:
        end_quiz()

# Function to reset answer button states for the next question
def reset_answer_buttons():
    for rb in option_buttons:
        rb.config(bg="white", state="normal")  # Reset color and state

# Function to update the joker buttons
def update_joker_buttons():
    if fifty_percent_used:
        fifty_percent_button.pack_forget()  # Hide after use
    else:
        fifty_percent_button.pack(side="left", padx=10)  # Show if not used

    if two_chances_used:
        two_chances_button.pack_forget()  # Hide after use
    else:
        two_chances_button.pack(side="left", padx=10)  # Show if not used

# Function to check answer
def check_answer(selected):
    global score, question_index
    correct_answer = selected_questions[question_index][1]['answer']

    if selected == "":
        result_label.config(text="Please select an answer!")
        return

    if selected == correct_answer:
        score += 2.5
        result_label.config(text="Correct!")
    else:
        result_label.config(text=f"Wrong! The correct answer was: {correct_answer}")

    question_index += 1
    display_question()

# Function to display fairy based on score
def display_fairy():
    global score
    for widget in quiz_frame.winfo_children():
        widget.destroy()  # Clear previous content

    if score >= 25:
        fairy_image = "images/tecna.jpg"
    elif score >= 20:
        fairy_image = "images/bloom.jpg"
    elif score >= 15:
        fairy_image = "images/flora.jpg"
    elif score >= 10:
        fairy_image = "images/stella.jpg"
    else:
        fairy_image = "images/musa.jpg"

    img = Image.open(fairy_image)
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    img_label = tk.Label(quiz_frame, image=img_tk)
    img_label.image = img_tk  # Keep reference
    img_label.pack()

    result_label = tk.Label(quiz_frame, text=f"Your score: {score}\nYou got the fairy!", font=('Helvetica', 12))
    result_label.pack()

# Function to end the quiz
def end_quiz():
    display_fairy()

# Start the GUI loop
root.mainloop()
