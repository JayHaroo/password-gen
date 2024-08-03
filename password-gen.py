import tkinter as tk
import random
import string

root = tk.Tk()
root.geometry("400x200")

def generate_pass():
    symbols = ['.', '-', '+', '#', '@']
    minNum = 1
    maxNum = 99
    passLen = 12

    password = ""
    while len(password) < passLen:
        gen_num = str(random.randint(minNum, maxNum))
        gen_sym = random.choice(symbols)
        gen_str = random.choice(string.ascii_letters)
        
        gen_text = gen_num + gen_str + gen_sym
        
        # Ensure the password does not exceed the desired length
        if len(password) + len(gen_text) > passLen:
            gen_text = gen_text[:passLen - len(password)]
        
        password += gen_text

    text = tk.Label(root, text=password)
    text.pack()

button = tk.Button(root, text="Generate Password", command=generate_pass)
button.pack()

root.mainloop()
