import tkinter as tk
from tkinter import ttk
import json

# Initialize main window
root = tk.Tk()
root.title('Simple To-Do List')

canvas = tk.Canvas(root, height=400, width=540, bg='black')
canvas.pack()

frame = tk.Frame(root, bg='black')
frame.place(relwidth=0.6, relheight=0.8, relx=0.1, rely=0.1)

y1 = 90
va = []
checkboxes = []
TASK_FILE = "tasks.json"

def save_tasks():
    with open(TASK_FILE, "w") as f:
        json.dump(va, f)

def load_tasks():
    global y1
    try:
        with open(TASK_FILE, "r") as f:
            tasks = json.load(f)
            for task in tasks:
                add_task(task)
    except FileNotFoundError:
        pass

def exitb():
    save_tasks()
    root.destroy()

def add_task(task=None):
    global y1
    v = ta.get() if task is None else task
    if not v.strip():
        return
    
    va.append(v)
    ta.delete(0, tk.END)

    custom_style = ttk.Style()
    custom_style.configure("Custom.TCheckbutton", background="black", foreground="white", font=('Arial', 16, 'bold'))
    cb_var = tk.BooleanVar()
    cb = ttk.Checkbutton(frame, text=v, style="Custom.TCheckbutton", variable=cb_var)
    cb.place(x=20, y=y1)
    cb.state(['!alternate'])

    checkboxes.append((cb, cb_var, v))
    y1 += 30

def delete_selected():
    global y1
    for cb, cb_var, task in checkboxes[:]:
        if cb_var.get():
            cb.destroy()
            va.remove(task)
            checkboxes.remove((cb, cb_var, task))
    save_tasks()

# UI Elements
ta = tk.Entry(font=('Arial', 16, 'bold'))
ta.place(x=160, y=25)

t = tk.Label(text='Enter Task: ', anchor='w', font=('Arial', 14, 'bold'), background='black', foreground='white')
t.place(x=40, y=25)

retrieveb = tk.Button(root, text="Add", fg='black', bg="yellow", command=add_task, font=('Arial', 14, 'bold'), height=1, width=6)
retrieveb.place(x=215, y=70)

delete_button = tk.Button(root, text="Delete", fg='black', bg="yellow", command=delete_selected, font=('Arial', 14, 'bold'), height=1, width=6)
delete_button.place(x=150, y=350)

exit_button = tk.Button(root, text="Exit", fg='black', bg="yellow", command=exitb, font=('Arial', 14, 'bold'), height=1, width=6)
exit_button.place(x=280, y=350)

load_tasks()
root.mainloop()
