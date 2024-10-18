
import tkinter as tk 
import random
from PIL import Image, ImageTk 

# Dictionary to store the quiz questions, options, and correct answers
# quiz_game.py

# Dictionary to store the quiz questions, options, and correct answers
quiz = {
    "easy": {
        "What is the capital of France?": {
            "options": ["Paris", "London", "Berlin", "Rome"],
            "answer": "Paris"
        },
        "What is 2 + 2?": {
            "options": ["3", "4", "5", "6"],
            "answer": "4"
        },
        "What color do you get when you mix red and white?": {
            "options": ["Pink", "Purple", "Orange", "Brown"],
            "answer": "Pink"
        },
        "What is the largest ocean on Earth?": {
            "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
            "answer": "Pacific"
        },
        "Which animal is known as the King of the Jungle?": {
            "options": ["Elephant", "Lion", "Tiger", "Gorilla"],
            "answer": "Lion"
        },
        "What is the freezing point of water?": {
            "options": ["0 degrees Celsius", "100 degrees Celsius", "32 degrees Fahrenheit", "50 degrees Fahrenheit"],
            "answer": "0 degrees Celsius"
        },
        "Which planet is known as the Red Planet?": {
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        "What is the sum of angles in a triangle?": {
            "options": ["90 degrees", "180 degrees", "360 degrees", "270 degrees"],
            "answer": "180 degrees"
        },
        "How many continents are there?": {
            "options": ["5", "6", "7", "8"],
            "answer": "7"
        },
        "What is the capital of Japan?": {
            "options": ["Seoul", "Beijing", "Tokyo", "Bangkok"],
            "answer": "Tokyo"
        },
        "Which gas do plants absorb from the atmosphere?": {
            "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"],
            "answer": "Carbon Dioxide"
        },
        "What is the boiling point of water?": {
            "options": ["0 degrees Celsius", "100 degrees Celsius", "50 degrees Celsius", "25 degrees Celsius"],
            "answer": "100 degrees Celsius"
        },
        "Which month has Valentine's Day?": {
            "options": ["January", "February", "March", "April"],
            "answer": "February"
        },
        "What is the name of the fairy in Peter Pan?": {
            "options": ["Tinkerbell", "Cinderella", "Snow White", "Belle"],
            "answer": "Tinkerbell"
        },
        "What is the largest land animal?": {
            "options": ["Elephant", "Rhino", "Giraffe", "Hippo"],
            "answer": "Elephant"
        },
        "Which is the smallest prime number?": {
            "options": ["1", "2", "3", "5"],
            "answer": "2"
        },
        "What do you call a baby cat?": {
            "options": ["Kitten", "Puppy", "Cub", "Foal"],
            "answer": "Kitten"
        },
        "Which country is known as the Land of the Rising Sun?": {
            "options": ["China", "Japan", "Korea", "Thailand"],
            "answer": "Japan"
        },
        "What is 10 + 5?": {
            "options": ["12", "15", "17", "10"],
            "answer": "15"
        },
        "Which is the largest planet in our solar system?": {
            "options": ["Earth", "Jupiter", "Saturn", "Mars"],
            "answer": "Jupiter"
        },
        "What is the capital of Italy?": {
            "options": ["Rome", "Paris", "Madrid", "Berlin"],
            "answer": "Rome"
        }
    },
    "medium": {
        "Who wrote 'Romeo and Juliet'?": {
            "options": ["Shakespeare", "Dickens", "Austen", "Hemingway"],
            "answer": "Shakespeare"
        },
        "What is the square root of 144?": {
            "options": ["10", "11", "12", "13"],
            "answer": "12"
        },
        "Which element has the chemical symbol 'O'?": {
            "options": ["Oxygen", "Gold", "Osmium", "Oganesson"],
            "answer": "Oxygen"
        },
        "In which year did the Titanic sink?": {
            "options": ["1910", "1912", "1914", "1916"],
            "answer": "1912"
        },
        "Who painted the Mona Lisa?": {
            "options": ["Van Gogh", "Da Vinci", "Picasso", "Monet"],
            "answer": "Da Vinci"
        },
        "What is the hardest natural substance on Earth?": {
            "options": ["Gold", "Iron", "Diamond", "Graphite"],
            "answer": "Diamond"
        },
        "What is the main ingredient in guacamole?": {
            "options": ["Tomato", "Avocado", "Onion", "Pepper"],
            "answer": "Avocado"
        },
        "Which planet is known for its rings?": {
            "options": ["Earth", "Mars", "Saturn", "Jupiter"],
            "answer": "Saturn"
        },
        "What is the capital city of Australia?": {
            "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
            "answer": "Canberra"
        },
        "Which gas is most abundant in the Earth's atmosphere?": {
            "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"],
            "answer": "Nitrogen"
        },
        "What is the chemical formula for water?": {
            "options": ["H2O", "O2", "CO2", "NaCl"],
            "answer": "H2O"
        },
        "Who discovered penicillin?": {
            "options": ["Fleming", "Pasteur", "Lister", "Curie"],
            "answer": "Fleming"
        },
        "What is the longest river in the world?": {
            "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
            "answer": "Nile"
        },
        "Who was the first person to walk on the Moon?": {
            "options": ["Armstrong", "Aldrin", "Gagarin", "Glenn"],
            "answer": "Armstrong"
        },
        "What is the capital of Egypt?": {
            "options": ["Cairo", "Alexandria", "Giza", "Luxor"],
            "answer": "Cairo"
        },
        "What is the currency of Japan?": {
            "options": ["Yen", "Won", "Dollar", "Euro"],
            "answer": "Yen"
        },
        "What is the largest mammal in the world?": {
            "options": ["Elephant", "Blue Whale", "Giraffe", "Great White Shark"],
            "answer": "Blue Whale"
        },
        "Which continent is known as the Dark Continent?": {
            "options": ["Asia", "Africa", "Australia", "South America"],
            "answer": "Africa"
        },
        "Which country is famous for the Great Wall?": {
            "options": ["India", "Japan", "China", "Korea"],
            "answer": "China"
        },
        "Who is known as the father of modern physics?": {
            "options": ["Einstein", "Newton", "Galileo", "Tesla"],
            "answer": "Einstein"
        },
        "What is the largest desert in the world?": {
            "options": ["Sahara", "Arabian", "Gobi", "Kalahari"],
            "answer": "Sahara"
        },
        "What is the process by which plants make food called?": {
            "options": ["Respiration", "Photosynthesis", "Transpiration", "Digestion"],
            "answer": "Photosynthesis"
        }
    },
    "hard": {
    "What is the capital of Bhutan?": {
        "options": ["Thimphu", "Kathmandu", "Lhasa", "Dhaka"],
        "answer": "Thimphu"
    },
    "What is the speed of light?": {
        "options": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "900,000 km/s"],
        "answer": "300,000 km/s"
    },
    "Which physicist developed the theory of relativity?": {
        "options": ["Newton", "Einstein", "Hawking", "Bohr"],
        "answer": "Einstein"
    },
    "What is the main language spoken in Brazil?": {
        "options": ["Spanish", "Portuguese", "English", "French"],
        "answer": "Portuguese"
    },
    "In what year did World War I begin?": {
        "options": ["1914", "1916", "1918", "1910"],
        "answer": "1914"
    },
    "What is the highest mountain in North America?": {
        "options": ["Denali", "Mount Rainier", "Mount St. Helens", "Mount Logan"],
        "answer": "Denali"
    },
    "Which chemical element has the symbol 'Fe'?": {
        "options": ["Fluorine", "Francium", "Iron", "Fermium"],
        "answer": "Iron"
    },
    "What is the capital of Turkey?": {
        "options": ["Istanbul", "Ankara", "Izmir", "Antalya"],
        "answer": "Ankara"
    },
    "Which planet has the most moons?": {
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Saturn"
    },
    "Who was the first female Prime Minister of the United Kingdom?": {
        "options": ["Margaret Thatcher", "Theresa May", "Angela Merkel", "Indira Gandhi"],
        "answer": "Margaret Thatcher"
    },
    "What is the hardest natural substance on Earth?": {
        "options": ["Diamond", "Iron", "Gold", "Quartz"],
        "answer": "Diamond"
    },
    "What is the longest river in South America?": {
        "options": ["Amazon", "Nile", "Paraná", "Orinoco"],
        "answer": "Amazon"
    },
    "Who wrote 'The Iliad' and 'The Odyssey'?": {
        "options": ["Homer", "Virgil", "Ovid", "Sophocles"],
        "answer": "Homer"
    },
    "What is the capital of Iceland?": {
        "options": ["Reykjavik", "Oslo", "Helsinki", "Copenhagen"],
        "answer": "Reykjavik"
    },
    "What is the largest desert in the world?": {
        "options": ["Sahara", "Arabian", "Gobi", "Antarctic"],
        "answer": "Antarctic"
    },
    "In which year did the Berlin Wall fall?": {
        "options": ["1987", "1988", "1989", "1990"],
        "answer": "1989"
    },
    "Which artist painted the Sistine Chapel ceiling?": {
        "options": ["Michelangelo", "Da Vinci", "Raphael", "Botticelli"],
        "answer": "Michelangelo"
    },
    "What is the capital city of Australia?": {
        "options": ["Sydney", "Canberra", "Melbourne", "Brisbane"],
        "answer": "Canberra"
    },
    "Which gas is most abundant in the Earth's atmosphere?": {
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"],
        "answer": "Nitrogen"
    },
    "What year did the Chernobyl disaster occur?": {
        "options": ["1986", "1991", "1989", "1978"],
        "answer": "1986"
    },
    "What is the main ingredient in traditional hummus?": {
        "options": ["Chickpeas", "Lentils", "Beans", "Peas"],
        "answer": "Chickpeas"
    },
    "Who discovered the law of gravity?": {
        "options": ["Einstein", "Newton", "Galileo", "Kepler"],
        "answer": "Newton"
    },
    "What is the name of the longest river in Africa?": {
        "options": ["Nile", "Congo", "Niger", "Zambezi"],
        "answer": "Nile"
    },
    "What is the largest planet in our solar system?": {
        "options": ["Jupiter", "Saturn", "Earth", "Mars"],
        "answer": "Jupiter"
    },
    "What is the most spoken language in the world?": {
        "options": ["Mandarin", "Spanish", "English", "Hindi"],
        "answer": "Mandarin"
    },
    "In which country is the Great Pyramid of Giza located?": {
        "options": ["Egypt", "Greece", "Turkey", "Mexico"],
        "answer": "Egypt"
    },
    "What is the capital of Greece?": {
        "options": ["Athens", "Rome", "Paris", "Berlin"],
        "answer": "Athens"
    },
    "Which famous scientist introduced the concept of natural selection?": {
        "options": ["Darwin", "Lamarck", "Mendel", "Huxley"],
        "answer": "Darwin"
    },
    "What is the chemical symbol for gold?": {
        "options": ["Ag", "Au", "Pb", "Fe"],
        "answer": "Au"
    },
    "Which city is known as the City of Love?": {
        "options": ["Rome", "Paris", "Venice", "New York"],
        "answer": "Paris"
    },
    "What year did World War II end?": {
        "options": ["1945", "1944", "1946", "1943"],
        "answer": "1945"
    },
    "What is the name of the largest ocean on Earth?": {
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    "Who wrote 'The Catcher in the Rye'?": {
        "options": ["Salinger", "Hemingway", "Fitzgerald", "Orwell"],
        "answer": "Salinger"
    },
    "What is the chemical formula for table salt?": {
        "options": ["NaCl", "KCl", "CaCl2", "MgCl2"],
        "answer": "NaCl"
    },
    "Which country is known as the Land of the Rising Sun?": {
        "options": ["China", "Japan", "Korea", "Vietnam"],
        "answer": "Japan"
    },
    "Which country has the longest coastline in the world?": {
        "options": ["Canada", "Australia", "Russia", "United States"],
        "answer": "Canada"
    },
}
}



# Initialize global variables
score = 0
question_index = 0
selected_questions = []

# Create main window
root = tk.Tk()
root.title("Quiz Game")
root.geometry("400x500")# Adjusted size to accommodate images
root.configure(bg="white")  # Set the background color of the main window to white


# Function to start the quiz
def start_quiz():
    global selected_questions, question_index, score
    selected_difficulty = difficulty_var.get()
    selected_questions = random.sample(list(quiz[selected_difficulty].items()), 10)
    question_index = 0
    score = 0
    difficulty_frame.pack_forget()
    quiz_frame.pack(pady=20)
    display_question()

# Difficulty selection frame
difficulty_frame = tk.Frame(root)
difficulty_frame.pack(pady=20)

intro_label = tk.Label(difficulty_frame, text="Welcome to the Fairy Quiz Game! Choose your difficulty level:", font=('Helvetica', 10))
intro_label.pack(pady=(0, 10))  # Add some padding below the label

intro_paragraph = tk.Label(difficulty_frame,text="Do the test to see which Winx fairy you are.", font=('Arial',8))
intro_paragraph.pack(pady= (0,10))

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

tk.Button(quiz_frame, text="Submit Answer", command=lambda: check_answer()).pack(pady=10)

# Function to display question
def display_question():
    global question_index
    if question_index < len(selected_questions):
        question, data = selected_questions[question_index]
        question_label.config(text=question)
        for i, option in enumerate(data['options']):
            option_buttons[i].config(text=option, value=option)
        score_label.config(text=f"Score: {score}")
    else:
        end_quiz()

# Function to check answer
def check_answer():
    global score, question_index
    correct_answer = selected_questions[question_index][1]['answer']

    if selected_answer.get() == "":
        result_label.config(text="Please select an answer!")
        return

    if selected_answer.get() == correct_answer:
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