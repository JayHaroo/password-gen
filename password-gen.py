import tkinter as tk
import random
import string

root = tk.Tk()
root.geometry("400x200")

var1 = tk.IntVar()
var2 = tk.IntVar()

def generate_pass():
    symbols = ['.', '-', '+', '#', '@']
    minNum = 1
    maxNum = 99
    passLen = 12
    password = ""
    
    if (var1.get() == 1) & (var2.get() == 1):
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

    if (var1.get() == 0) & (var2.get() == 1):
            while len(password) < passLen:
                gen_num = str(random.randint(minNum, maxNum))
                gen_str = random.choice(string.ascii_letters)
                
                gen_text = gen_num + gen_str
                
                # Ensure the password does not exceed the desired length
                if len(password) + len(gen_text) > passLen:
                    gen_text = gen_text[:passLen - len(password)]
                
                password += gen_text

            text = tk.Label(root, text=password)
            text.pack()
    
    if (var1.get() == 1) & (var2.get() == 0):
            while len(password) < passLen:
                    gen_sym = random.choice(symbols)
                    gen_str = random.choice(string.ascii_letters)
                    
                    gen_text = gen_str + gen_sym
                    
                    # Ensure the password does not exceed the desired length
                    if len(password) + len(gen_text) > passLen:
                        gen_text = gen_text[:passLen - len(password)]
                    
                    password += gen_text
            text = tk.Label(root, text=password)
            text.pack()
        

c1 = tk.Checkbutton(root, text='Symbols' , variable = var1 , onvalue=1, offvalue=0)
c1.pack()
c2 = tk.Checkbutton(root, text='Numbers', variable = var2 , onvalue=1, offvalue=0)
c2.pack()

button = tk.Button(root, text="Generate Password", command=generate_pass)
button.pack()

clearButton = tk.Button(root, text="Clear Password")
clearButton.pack()

root.mainloop()
