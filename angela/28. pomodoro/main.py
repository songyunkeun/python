from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
reps = 0
timer = None
# -------------------------TIMER RESET----------------------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    my_label.config(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
    global reps
    reps = 0

#---------- TIMER MECHANISM -----------#
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        # If it's the 8th rep:
        count_down(long_break_sec)
        my_label.config(text="long break",  fg=RED)
    elif reps % 2 == 0:
        # If it's the 2th/4th/6th rep:
        count_down(short_break_sec)
        my_label.config(text="short break", fg=PINK)
    else:
        # If it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        my_label.config(text="working",  fg=GREEN)

#--------------- COUNTDOWN MECHANISM --#
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min   }"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    #timer_text.config(text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "+"
        check_marks.config(text=marks)


window = Tk()
window.wm_title("pomodoro")
window.config(padx=100, pady=50)

my_label = Label(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
my_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=223, bg=YELLOW)
myimg = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=myimg)
timer_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 30, 'bold'), fill='white')
canvas.grid(column=1, row=1)
# timer_text = Label(text='00:00', font=(FONT_NAME, 30, 'bold'))
# timer_text.grid(column=1, row=1)

my_button_start = Button(text="start", command=start_timer)
my_button_start.grid(column=0, row=2)

check_marks = Label(font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)

my_button_reset = Button(text="reset", command=reset_timer)
my_button_reset.grid(column=2, row=2)
window.mainloop()

