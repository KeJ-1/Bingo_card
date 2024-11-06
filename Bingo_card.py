import tkinter as tk
import random

def Bingo_card():
    card = []
    for i in range(5):
        start = i * 15 + 1
        column = random.sample(range(start, start + 15), 5)
        card.extend(column)
    card[12] = "FREE"
    return card

def Checker():
    for line in bingo_lines:
        if all(selected_cells[i] for i in line):
            status_label.config(text="Bingo!")
            return

def Click(index):
    if not selected_cells[index]:
        selected_cells[index] = True
        buttons[index].config(state="disabled", bg="lightgreen")
        Checker()

root = tk.Tk()
root.title("ビンゴカード")

bingo_card = Bingo_card()
selected_cells = [False] * 25
buttons = []

bingo_lines = [
    [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24],  # 横
    [0, 5, 10, 15, 20], [1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24],  # 縦
    [0, 6, 12, 18, 24], [4, 8, 12, 16, 20] 
]

for index, number in enumerate(bingo_card):
    button = tk.Button(root, text=number, width=15, height=5,
                       command=lambda idx=index: Click(idx))
    button.grid(row=index // 5, column=index % 5)
    buttons.append(button)

status_label = tk.Label(root, text="", font=("Helvetica", 16))
status_label.grid(row=5, column=0, columnspan=5)

root.mainloop()
