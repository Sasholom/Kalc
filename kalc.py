import tkinter as tk

def on_click(event):
    button_text = event.widget.cget("text")
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except SyntaxError or NameError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row_index = 1
col_index = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 12))
    button.grid(row=row_index, column=col_index, padx=5, pady=5)
    button.bind("<Button-1>", on_click)
    
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

root.mainloop()