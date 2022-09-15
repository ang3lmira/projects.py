from tkinter import *
import math
timer = None

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_label, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text=" ")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=YELLOW)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    minute = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = (f"0{seconds}")

    canvas.itemconfig(timer_text, text=f"{minute}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


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

reset_button = Button(text="Reset", command=reset, highlightthickness=0)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=PINK)
check_marks.grid(row=3, column=1)
window.mainloop()
