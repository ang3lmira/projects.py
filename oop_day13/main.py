from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    countdown(5*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    minute = math.floor(count / 60)
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minute}:{seconds}")
    if count > 0:
        window.after(1000, countdown, count-1)

# ---------------------------- UI SETUP ------------------------------- #


def start_count():
    pass


def reset_count():
    pass


window = Tk()
window.title("m's pomodoro")
window.config(padx=100, pady=50, bg=PINK)


canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)


timer_label = Label(font=(FONT_NAME, 50), text="Timer", bg=PINK, fg=GREEN)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_count, highlightthickness=0)
reset_button.grid(row=2, column=2)

check_marks = Label(text="✓", fg=GREEN, bg=PINK)
check_marks.grid(row=3, column=1)
window.mainloop()
