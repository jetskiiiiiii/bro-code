import tkinter as tk
from tkinter import ttk

def usd_to_idr(usd):
    return usd*16000

def submit():
    random_textbox.config(state="normal")
    random_textbox.delete("0.0", tk.END)
    entered_text = usd_input.get()
    converted_num = usd_to_idr(int(entered_text))
    random_textbox.insert(index=0.0, chars=converted_num)
    random_textbox.config(state="disabled")

root = tk.Tk()
frame = ttk.Frame(root)
frame.grid()

welcome_label = ttk.Label(frame, text="Hello World!", font=("Verdana", 20, "bold"), background="black", foreground="white")
exit_button = ttk.Button(frame, text="Exit", command=root.destroy)
exit_button.grid(row=1, column=0)
welcome_label.grid(row=0, column=0)

random_textbox = tk.Text(frame, width=20, height=1)
random_textbox.config(state="disabled")
random_textbox.grid(row=3, column=0)

usd_input = tk.Entry(frame, width=20)
usd_input.grid(row=2, column=0)

submit_button = tk.Button(frame, text="Submit", command=submit)
submit_button.grid(row=4, column=0)

root.mainloop()