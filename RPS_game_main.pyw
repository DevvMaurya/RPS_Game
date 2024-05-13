import tkinter as tk
import random

player_score = 0
computer_score = 0
total_rounds = 0

# GUI setup
root = tk.Tk()
root.geometry("400x300")
root.title("RCP")
root.configure(bg="#D05228")
def reset():
    global player_score, computer_score, total_rounds
    player_score = 0
    computer_score = 0
    total_rounds = 0
    update_scores()
    result_label.config(text="")

def update_scores():
    player_score_label.config(text=f"Player Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    total_rounds_label.config(text=f"Total Rounds: {total_rounds}")

def button_clicked(btn_text):
    global player_score, computer_score, total_rounds

    moves = ["Rock", "Paper", "Scissors"]
    computer_move = random.choice(moves)
    player_move = btn_text
    result = "It's a tie!"

    if player_move == computer_move:
        result = "It's a tie!"
    elif (player_move == "Rock" and computer_move == "Scissors") or \
         (player_move == "Paper" and computer_move == "Rock") or \
         (player_move == "Scissors" and computer_move == "Paper"):
        result = "🎉 You win! 🎊"
        player_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    result_label.config(text=f"{result} . Computer chose {computer_move}")
    total_rounds += 1
    update_scores()
# Title label
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 20),bg="#D05228", fg="white")
title_label.pack(pady=10)

# label = tk.Label(root, text="Select one of them: Rock, Paper, Scissors", fg="white")
# label.pack()

btn_frame = tk.Frame(root, bg="#D05228")
btn_frame.pack(pady=10)


rock_btn = tk.Button(btn_frame, text="🪨", font=("Arial", 12), bg="lightblue", command=lambda: button_clicked("Rock"), bd=6, relief="flat")
rock_btn.grid(row=0, column=0, padx=20)

Paper_btn = tk.Button(btn_frame, text="📃", font=("Arial", 12), bg="lightblue", command=lambda: button_clicked("Paper"), bd=6, relief="flat")
Paper_btn.grid(row=0, column=1, padx=20)

scissors_btn = tk.Button(btn_frame, text="✂️", font=("Arial", 12), bg="lightblue", command=lambda: button_clicked("Scissors"), bd=6, relief="flat")
scissors_btn.grid(row=0, column=2, padx=20)

result_label = tk.Label(root, text="", font=("Arial", 9))
result_label.pack(pady=10)

score_frame = tk.Frame(root, bg="#2c3e50")
score_frame.pack(pady=10)

player_score_label = tk.Label(score_frame, text="Player Score: 0", fg="#ecf0f1", bg="#2c3e50", font=("Helvetica", 12))
player_score_label.grid(row=0, column=0, padx=20)

computer_score_label = tk.Label(score_frame, text="Computer Score: 0", fg="#ecf0f1", bg="#2c3e50", font=("Helvetica", 12))
computer_score_label.grid(row=0, column=1, padx=20)

total_rounds_label = tk.Label(root, text="Total Rounds: 0", fg="#ecf0f1", bg="#D05228" ,font=("Helvetica", 14))
total_rounds_label.pack(pady=10)

reset_btn = tk.Button(root, text="Reset", command=lambda: reset(), bg="red", fg="white",font=("times new roman", 12,'bold'))
reset_btn.pack(pady=10)

root.mainloop()