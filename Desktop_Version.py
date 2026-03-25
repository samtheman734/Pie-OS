import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

root = tk.Tk()
root.title("PIE OS")
root.geometry("600x400")
root.configure(bg="white")

def open_terminal():
    terminal_window = tk.Toplevel()
    terminal_window.title("Terminal")
    terminal_window.geometry("600x400")
    
    output_text = tk.Text(terminal_window)
    output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    input_frame = tk.Frame(terminal_window)
    input_frame.pack(fill=tk.X, padx=10, pady=5)
    
    command_entry = tk.Entry(input_frame)
    command_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def run_command(event=None):
        cmd = command_entry.get()
        try:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            output = e.output
        output_text.insert(tk.END, f"> {cmd}\n{output}\n")
        output_text.see(tk.END)
        command_entry.delete(0, tk.END)

    command_entry.bind("<Return>", run_command)

    run_btn = tk.Button(input_frame, text="Run", command=run_command)
    run_btn.pack(side=tk.LEFT, padx=5)

def open_calculator():
    calc_win = tk.Toplevel()
    calc_win.title("Calculator")
    calc_win.geometry("300x250")
    calc_win.configure(bg="light green")
    expr = ""

    def press(key):
        nonlocal expr
        expr += str(key)
        display.set(expr)

    def equal():
        nonlocal expr
        try:
            result = str(eval(expr))
            display.set(result)
            expr = ""
        except:
            display.set("error")
            expr = ""

    def clear():
        nonlocal expr
        expr = ""
        display.set("")

    display = tk.StringVar()
    tk.Entry(calc_win, textvariable=display, font=("Arial", 14)).grid(row=0, column=0, columnspan=4, ipadx=70, pady=10)

    buttons = [
        ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
        ('7', 4, 0), ('8', 4, 1), ('9', 4, 2),
        ('0', 5, 0), ('.', 5, 1)
    ]
    for (text, row, col) in buttons:
        tk.Button(calc_win, text=text, width=7, command=lambda t=text: press(t)).grid(row=row, column=col)

    ops = [
        ('+', 2, 3), ('-', 3, 3),
        ('*', 4, 3), ('/', 5, 3)
    ]
    for (op, row, col) in ops:
        tk.Button(calc_win, text=op, width=7, command=lambda t=op: press(t)).grid(row=row, column=col)

    tk.Button(calc_win, text='=', width=7, command=equal).grid(row=5, column=2)
    tk.Button(calc_win, text='Clear', width=7, command=clear).grid(row=5, column=1)

# Notepad
def open_notepad():
    notepad_win = tk.Toplevel()
    notepad_win.title("Notepad")
    notepad_win.geometry("600x400")
    text_area = tk.Text(notepad_win, undo=True)
    text_area.pack(fill=tk.BOTH, expand=True)

    # Menu for Save and Open
    menu = tk.Menu(notepad_win)
    notepad_win.config(menu=menu)

    def save_file():
        filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filename:
            try:
                with open(filename, 'w') as f:
                    f.write(text_area.get(1.0, tk.END))
            except Exception as e:
                messagebox.showerror("Save Error", str(e))

    def open_file():
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filename:
            try:
                with open(filename, 'r') as f:
                    content = f.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Open Error", str(e))

    file_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save As...", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=notepad_win.destroy)

def add_start_menu():
    import tkinter.font as tkFont
    big_font = tkFont.Font(family="Helvetica", size=8, weight="bold")
    try:
        start_image = tk.PhotoImage(file=r"C:\Users\sam44\OneDrive\Desktop\PIE OS\menuicon.jpg")
    except:
        start_image = None

    taskbar = tk.Frame(root, bg='gray', height=50)
    taskbar.pack(side=tk.BOTTOM, fill=tk.X)

    def show_menu(event):
        menu = tk.Menu(root, tearoff=0)
        menu.add_command(label="Calculator", command=open_calculator)
        menu.add_command(label="Terminal", command=open_terminal)
        menu.add_command(label="Open File", command=lambda: filedialog.askopenfilename())
        menu.add_separator()
        menu.add_command(label="Notepad", command=open_notepad)
        menu.add_separator()
        menu.add_command(label="Exit", command=root.quit)
        menu.tk_popup(event.x_root, event.y_root)

    start_button = tk.Button(taskbar, text="Start", font=big_font, padx=20, pady=10,
                             image=start_image, compound=tk.LEFT)
    start_button.pack(side=tk.LEFT, padx=5, pady=5)
    start_button.bind("<Button-1>", show_menu)
    start_button.image = start_image

app_frame = tk.Frame(root)
app_frame.pack(padx=10, pady=10, anchor='nw')

try:
    term_icon = tk.PhotoImage(file=r"C:\Users\sam44\OneDrive\Desktop\PIE OS\TermIcon.png").subsample(3,3)
except:
    term_icon = None
if term_icon:
    tk.Button(app_frame, text="Terminal", image=term_icon, compound=tk.TOP, command=open_terminal).pack(side=tk.LEFT, padx=5)
else:
    tk.Button(app_frame, text="Terminal", command=open_terminal).pack(side=tk.LEFT, padx=5)

try:
    files_icon = tk.PhotoImage(file=r"C:\Users\sam44\OneDrive\Desktop\PIE OS\fileexplorericon.png").subsample(5,5)
except:
    files_icon = None
if files_icon:
    tk.Button(app_frame, text="Files", image=files_icon, compound=tk.TOP, command=lambda: filedialog.askopenfilename()).pack(side=tk.LEFT, padx=5)
else:
    tk.Button(app_frame, text="Files", command=lambda: filedialog.askopenfilename()).pack(side=tk.LEFT, padx=5)

add_start_menu()

root.mainloop()
