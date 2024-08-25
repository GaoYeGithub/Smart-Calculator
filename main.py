import tkinter as tk
from tkinter import messagebox

response = [
  'Welcome to smart calculator',
  'My name is Calc',
  'Thanks for using me!',
  'Sorry, this is beyond my ability'
]

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mul(a, b):
  return a * b

def div(a, b):
  return a / b

def mod(a, b):
  return a % b

def lcm(a, b):
  L = a if a > b else b
  while L <= a * b:
      if L % a == 0 and L % b == 0:
          return L
      L += 1

def hcf(a, b):
  H = a if a < b else b
  while H >= 1:
      if a % H == 0 and b % H == 0:
          return H
      H -= 1

commands = {
  'NAME': lambda: print(response[1]),
  'EXIT': lambda: (print(response[2]), exit()),
  'END': lambda: (print(response[2]), exit()),
  'CLOSE': lambda: (print(response[2]), exit())
}


class SmartCalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Smart Calculator")
        master.configure(bg='#2C3E50')

        self.entry_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.master, textvariable=self.entry_var, width=30, font=('Arial', 14), bg='#ECF0F1')
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipady=10)

        self.result_label = tk.Label(self.master, text="", font=('Arial', 14), bg='#2C3E50', fg='#ECF0F1')
        self.result_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        self.create_number_buttons()

        operations = {
        'ADD': add,
        'PLUS': add,
        'SUM': add,
        'ADDITION': add,
        'SUB': sub,
        'SUBTRACT': sub,
        'MINUS': sub,
        'DIFFERENCE': sub,
        'LCM': lcm,
        'HCF': hcf,
        'PRODUCT': mul,
        'MULTIPLY': mul,
        'MULTIPLICATION': mul,
        'DIVISION': div,
        'MOD': mod,
        'REMAINDER': mod,
        'MODULAS': mod
      }
        for i, op in enumerate(operations):
            btn = tk.Button(self.master, text=op, command=lambda x=op: self.add_to_entry(x),
                            bg='#3498DB', fg='white', font=('Arial', 12))
            btn.grid(row=i//4 + 5, column=i%4, padx=2, pady=2, sticky='nsew')

        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate,
                                          bg='#2ECC71', fg='white', font=('Arial', 12))
        self.calculate_button.grid(row=7, column=0, columnspan=2, padx=2, pady=2, sticky='nsew')

        self.clear_button = tk.Button(self.master, text="Clear", command=self.clear_entry,
                                      bg='#E74C3C', fg='white', font=('Arial', 12))
        self.clear_button.grid(row=7, column=2, columnspan=2, padx=2, pady=2, sticky='nsew')

        for i in range(8):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

    def create_number_buttons(self):
        for i in range(9):
            btn = tk.Button(self.master, text=str(i+1), command=lambda x=i+1: self.add_to_entry(x),
                            bg='#34495E', fg='white', font=('Arial', 12))
            btn.grid(row=(i//3)+2, column=i%3, padx=2, pady=2, sticky='nsew')

        zero_btn = tk.Button(self.master, text='0', command=lambda: self.add_to_entry(0),
                             bg='#34495E', fg='white', font=('Arial', 12))
        zero_btn.grid(row=5, column=1, padx=2, pady=2, sticky='nsew')

    def add_to_entry(self, value):
        current = self.entry_var.get()
        self.entry_var.set(f"{current} {value}")

    def clear_entry(self):
        self.entry_var.set("")
        self.result_label.config(text="")

    def calculate(self):
        text = self.entry_var.get().upper()
        for word in text.split():
            if word in operations:
                try:
                    l = extract_from_text(text)
                    r = operations[word](l[0], l[1])
                    self.result_label.config(text=f"Result: {r}")
                    return
                except:
                    messagebox.showerror("Error", "Something went wrong. Please check your input.")
                    return
            elif word in commands:
                if word == "NAME":
                    self.result_label.config(text=response[1])
                    return
                elif word in ["EXIT", "END", "CLOSE"]:
                    self.master.quit()
                    return

        self.result_label.config(text="Invalid input. Please try again.")


root = tk.Tk()
my_gui = SmartCalculatorGUI(root)
root.mainloop()