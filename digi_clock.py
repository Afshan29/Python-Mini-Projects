import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

# Create the label once, outside the time() function
label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center')

def time():
    string = strftime('%H:%M:%S %p\n%D')  # Fixed spacing and format
    label.config(text=string)
    label.after(1000, time)  # Call this function again after 1 second

time()  # Start the clock
root.mainloop()  # Run the GUI
