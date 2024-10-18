import random  
import tkinter as tk 

# Dictionary to store the quiz questions, options, and correct answers
# quiz_game.py

# Dictionary to store the quiz questions, options, and correct answers
quiz = {
    "What is the capital of France?": {
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    "Who wrote 'Hamlet'?": {
        "options": ["Shakespeare", "Dickens", "Austen", "Tolkien"],
        "answer": "Shakespeare"
    },
    "What is the square root of 64?": {
        "options": ["6", "7", "8", "9"],
        "answer": "8"
    },
    "Which planet is known as the Red Planet?": {
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars"
    },
    "How many continents are there on Earth?": {
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    "In which year did the Titanic sink?": {
        "options": ["1905", "1912", "1918", "1925"],
        "answer": "1912"
    },
    "What is the chemical symbol for gold?": {
        "options": ["Ag", "Au", "Pb", "Fe"],
        "answer": "Au"
    },
    "Which country is home to the kangaroo?": {
        "options": ["Australia", "South Africa", "Canada", "India"],
        "answer": "Australia"
    },
    "Who painted the Mona Lisa?": {
        "options": ["Michelangelo", "Raphael", "Leonardo da Vinci", "Van Gogh"],
        "answer": "Leonardo da Vinci"
    },
    "Which ocean is the largest?": {
        "options": ["Atlantic", "Pacific", "Indian", "Arctic"],
        "answer": "Pacific"
    },
    "What is the hardest natural substance on Earth?": {
        "options": ["Iron", "Gold", "Diamond", "Silver"],
        "answer": "Diamond"
    },
    "Which planet is closest to the sun?": {
        "options": ["Venus", "Earth", "Mercury", "Mars"],
        "answer": "Mercury"
    },
    "What is the smallest prime number?": {
        "options": ["0", "1", "2", "3"],
        "answer": "2"
    },
    "How many time zones are there in the world?": {
        "options": ["12", "18", "24", "30"],
        "answer": "24"
    },
    "Which language has the most native speakers?": {
        "options": ["English", "Mandarin", "Spanish", "Hindi"],
        "answer": "Mandarin"
    },
    "Which organ in the human body is responsible for pumping blood?": {
        "options": ["Lungs", "Heart", "Liver", "Kidneys"],
        "answer": "Heart"
    },
    "What is the boiling point of water in Celsius?": {
        "options": ["50°C", "75°C", "90°C", "100°C"],
        "answer": "100°C"
    },
    "Who was the first person to walk on the moon?": {
        "options": ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "Michael Collins"],
        "answer": "Neil Armstrong"
    },
    "What is the longest river in the world?": {
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
        "answer": "Nile"
    },
    "How many bones are in the human body?": {
        "options": ["196", "206", "226", "256"],
        "answer": "206"
    },
    "What is the capital of Japan?": {
        "options": ["Kyoto", "Osaka", "Tokyo", "Nagoya"],
        "answer": "Tokyo"
    },
    "Which continents does Turkey is placed between?":{
        "options":["Asia-Africa","Europe-Oceania","Europe-Asia","North America-South America"],
        "answer":"Europe-Asia"
    },
    "Which element is the most abundant in the Earth's atmosphere?": {
        "options": ["Oxygen", "Hydrogen", "Nitrogen", "Carbon Dioxide"],
        "answer": "Nitrogen"
    },
    "Who discovered penicillin?": {
        "options": ["Marie Curie", "Isaac Newton", "Alexander Fleming", "Louis Pasteur"],
        "answer": "Alexander Fleming"
    },
    "Which gas do plants absorb from the atmosphere?": {
        "options": ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"],
        "answer": "Carbon Dioxide"
    },
    "What is the largest mammal in the world?": {
        "options": ["Elephant", "Whale", "Giraffe", "Shark"],
        "answer": "Whale"
    }
}


# Shuffle the questions
questions = list(quiz.items())
random.shuffle(questions)

# Initialize the score and current question index
score = 0
question_index = 0

# Create the main window
root = tk.Tk()
root.title("Quiz Game")

# Set the window size
root.geometry("400x300")

# Define the quiz frame
frame = tk.Frame(root)
frame.pack(pady=20)

# Display the question
question_label = tk.Label(frame, text="", wraplength=300, font=('Helvetica', 12))
question_label.pack(pady=10)

# Define variable to hold the selected answer
selected_answer = tk.StringVar()

# Create radio buttons for options
radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(frame, text="", variable=selected_answer, value="", font=('Helvetica', 10))
    rb.pack(anchor="w")
    radio_buttons.append(rb)

# Create the submit button
submit_button = tk.Button(root, text="Submit Answer", command=lambda: check_answer())
submit_button.pack(pady=10)

# Label to show the result of each question
result_label = tk.Label(root, text="", font=('Helvetica', 10))
result_label.pack(pady=10)

# Label to show the score
score_label = tk.Label(root, text="Score: 0", font=('Helvetica', 12))
score_label.pack(pady=10)

# Function to display the next question
def display_question():
    global question_index
    if question_index < len(questions):
        question, data = questions[question_index]
        question_label.config(text=question)
        selected_answer.set(None)  # Clear the selected answer
        
        # Set the options in the radio buttons
        for i, option in enumerate(data["options"]):
            radio_buttons[i].config(text=option, value=option)
    else:
        # End of quiz
        question_label.config(text="Quiz Completed!")
        submit_button.config(state="disabled")
        result_label.config(text=f"Your final score is {score}/{len(questions)}")

# Function to check the answer and move to the next question
def check_answer():
    global score, question_index
    question, data = questions[question_index]
    correct_answer = data["answer"]
    user_answer = selected_answer.get()
    
    if user_answer == correct_answer:
        result_label.config(text="Correct!")
        score += 1
        score_label.config(text=f"Score: {score}")
    else:
        result_label.config(text=f"Wrong! The correct answer was {correct_answer}.")
    
    question_index += 1
    root.after(1000, display_question)  # Move to the next question after 1 second

# Start the quiz by displaying the first question
display_question()

# Start the tkinter event loop
root.mainloop()
