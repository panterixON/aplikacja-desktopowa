import tkinter as tk
root = tk.Tk()
label = tk.Label(text="Oblicz swoje bmi")
label = tk.Label(text="Wzrost")
entry1 = tk.Entry()
label = tk.Label(text="Waga")
entry2 = tk.Entry()
label.pack()
entry1.pack()
label.pack()
entry2.pack()



root.geometry("300x300")
root.title("Oblicz swoje bmi")
root.iconbitmap("")
root.mainloop()
