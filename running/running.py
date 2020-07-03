import tkinter as tk
import webbrowser

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def run ():    
    webbrowser.open_new_tab("https://www.google.com.br")
    
button1 = tk.Button(text='Open the Google',command=run, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()