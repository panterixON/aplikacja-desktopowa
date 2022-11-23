from tkinter import *
from tkinter import messagebox


def reset_entry():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    
    if bmi:
        messagebox.showinfo('bmi-pythonguides', f'Twoje bmi to {bmi}')
    else:
        messagebox.showerror('bmi-pythonguides', 'something went wrong!')   

root = Tk()
root.title('Kalkulator bmi')
root.geometry('400x300')
root.config(bg='blue')
root.resizable(False,False)

var = IntVar()

frame = Frame(
    root,
    padx=10, 
    pady=10
)
frame.pack(expand=True)


age_lb = Label(
    frame,
    text="Wpisz wiek"
)
age_lb.grid(row=1, column=1)

age_tf = Entry(
    frame, 
)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Wybierz płeć'
)
gen_lb.grid(row=2, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(
    frame2,
    text = 'M',
    variable = var,
    value = 1
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text = 'K',
    variable = var,
    value = 2
)
female_rb.pack(side=RIGHT)

height_lb = Label(
    frame,
    text="wpisz wysokość(cm)  "
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="wpisz wagę(kg)  ",

)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Oblicz',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Usuń',
    command=reset_entry
)
reset_btn.pack(side=LEFT)
root.mainloop()
# olaf karaś kompany pozdrawia c:
