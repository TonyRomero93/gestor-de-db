from cProfile import label
from ctypes import resize
from tkinter import *
from turtle import bgcolor, width
from PIL import Image, ImageTk
import get_info
import main
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import io

BG = "#404040"
BGLabel = "#505050"

class MainPanel(Tk):
    def __init__(self, user_name, user_pass):
        super().__init__()
        self.title(f"CPanel-{user_name}")
        self.config(background=BG)
        self.geometry("800x500")
        self.minsize(width=300, height=300)
        self.resizable(width=False, height=True)

        inf = get_info.Get(user_name, user_pass)
        income = get_info.income(user_name)
        expenses = get_info.expenses(user_name)
        print(inf[0][6])

        self.header = Frame(self, width=self.winfo_screenwidth(), height=100,background=BGLabel, border="0")
        self.header.pack(pady=(5,5), padx=(15,15))

        pil_img = Image.open(io.BytesIO(inf[0][6]))
        pil_img = pil_img.resize((70, 70))
        img = ImageTk.PhotoImage(pil_img)

        l_img= Label(self.header, image=img)
        l_img.place(x=10, y=10)

        name = Label(self.header, text="First name:      " + inf[0][3], background=BGLabel, foreground="white")
        name.place(x=100, y=10)

        last_name = Label(self.header, text="Last name:       " + inf[0][4], background=BGLabel, foreground="white")
        last_name.place(x=100, y=30)

        age = Label(self.header, text="Age:                   " + str(inf[0][5]) + " years", background=BGLabel, foreground="white")
        age.place(x=100, y=50)

        btn_config = Button(self, text="Config", relief="flat", foreground="white", background="red", width=10)
        btn_config.place(x=int(self.winfo_screenwidth()/2), y=20)

        btn_out = Button(self, text="Logout", relief="flat", foreground="white", background="red", width=10, command=self.logout)
        btn_out.place(x=int(self.winfo_screenwidth()/2), y=60)

        self.body = Frame(self, width=self.winfo_screenwidth(), height=400, background=BG)
        self.body.pack(pady=(0,5), padx=(15,15))

        labels = ["January","February","March", "April", "May", "June", "July", "August", "September", "Octover","November", "December"]
        income_list = [income[0][2], income[0][3], income[0][4], income[0][5], income[0][6], income[0][7], income[0][8], income[0][9], income[0][10], income[0][11], income[0][12], income[0][13]]
        expenses_list = [expenses[0][2], expenses[0][3], expenses[0][4], expenses[0][5], expenses[0][6], expenses[0][7], expenses[0][8], expenses[0][9], expenses[0][10], expenses[0][11], expenses[0][12], expenses[0][13]]

        fig = plt.Figure(figsize=(13,6), dpi=60)
        ax = fig.add_subplot(111)
        ax.plot(labels, income_list, marker='o', linestyle='--', label='Income')
        ax.set_xlabel("Months")
        ax.set_ylabel("Income")
        fig.set_facecolor("#A0A0A0")
        ax.set_facecolor(BGLabel)

        ax.plot(labels, expenses_list, marker='o', linestyle='--', color='w', label='expenses')

        ax.legend()

        canva = FigureCanvasTkAgg(fig, self.body)
        canva.draw()
        canva.get_tk_widget().place(x=0, y=5)

        self.mainloop()

    def logout(self):
        self.destroy()
        main.Main().mainloop()

def init(user_name, user_pass):
    main = MainPanel(user_name, user_pass)
