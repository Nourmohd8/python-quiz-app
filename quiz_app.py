import random
import tkinter as tk
from tkinter import messagebox

# Predefined quiz questions
questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 0  # Position in the options array
    },
    {
        "topic": "Lists",
        "question": "What will be the output of this Python code?",
        "code": "nums = [1, 2, 3]\nnums.append([4, 5])\nprint(len(nums))",
        "options": ["3", "4", "5", "6"],
        "answer": 1
    },
    {
        "topic": "Strings",
        "question": "What does this Python code print?",
        "code": "print('Hello'[::-1])",
        "options": ["olleH", "Hello", "error", "None"],
        "answer": 0
    }
]

# Initialize Tkinter window
root = tk.Tk()
root.title("Python Quiz Generator")
root.geometry("500x400")

# Create input field for topic
topic_label = tk.Label(root, text="Enter Python Topic:")
topic_label.pack()

topic_entry = tk.Entry(root)
topic_entry.pack()

# Function to fetch and display a question
def generate_question():
    selected_topic = topic_entry.get().strip().capitalize()
    filtered_questions = [q for q in questions if q["topic"] == selected_topic]

    if not filtered_questions:
        messagebox.showerror("Error", "No questions found for this topic.")
        return

    global current_question
    current_question = random.choice(filtered_questions)
    
    # Update the question display
    question_label.config(text=f"Topic: {current_question['topic']}\n{current_question['question']}")
    code_label.config(text=current_question["code"])

    # Update radio buttons with new options
    for i in range(4):
        radio_buttons[i].config(text=current_question["options"][i], value=i)

# Button to generate a quiz question
generate_button = tk.Button(root, text="Generate Python Question", command=generate_question)
generate_button.pack()

# Label to display the question
question_label = tk.Label(root, text="Question will appear here", wraplength=400, justify="left")
question_label.pack()

# Label to display the code snippet
code_label = tk.Label(root, text="", font=("Courier", 10), wraplength=400, justify="left")
code_label.pack()

# Create radio buttons for answer choices
selected_answer = tk.IntVar()
radio_buttons = []

for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=selected_answer, value=i)
    rb.pack()
    radio_buttons.append(rb)

# Function to check the answer
def check_answer():
    if current_question is None:
        messagebox.showerror("Error", "Please generate a question first.")
        return

    user_answer = selected_answer.get()
    correct_answer = current_question["answer"]

    if user_answer == correct_answer:
        messagebox.showinfo("Result", "Correct! Well done!")
    else:
        messagebox.showerror("Result", "Incorrect. Try again.")

# Button to submit answer
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack()

# Start the Tkinter main loop
root.mainloop()