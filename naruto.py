from tkinter import *
from tkinter.ttk import Combobox
window = Tk()


photo = PhotoImage(file="")
characters = Combobox(window) # Создаем комбобокс
characters["values"] = characters["values"] + "Нагато", "Саске", "Сакура", "Наруто" # заполняем персонажами

def picture(event): # функция для определения выбранного персонажа
    global photo
    global panel
    curr = characters.get()
    if curr == "Нагато":
        photo = PhotoImage(file="nagato.png")
        panel.config(image=photo)
    elif curr == "Саске":
        photo = PhotoImage(file="sasuke.png")
        panel.config(image=photo)
    elif curr == "Сакура":
        photo = PhotoImage(file="sakura.png")
        panel.config(image=photo)
    elif curr == "Наруто":
        photo = PhotoImage(file="naruto.png")
        panel.config(image=photo)
characters.grid(column=0,row=0)




panel = Label(window,image=photo, width=500,height=500)
panel.grid(column=1,row=1)

characters.bind("<<ComboboxSelected>>",picture)



window.mainloop()
