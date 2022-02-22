from tkinter import *
import conexion
import cpanel

class Main(Tk):
    def __init__(self) -> None:
        Tk.__init__(self)
        self.title("Login")
        self.config(background="#303030")
        self.geometry("300x300+500+100")
        self.resizable(width=False, height=False)

        self.name = Entry(self, relief="flat", width=30)
        self.name.insert(END, "(User name)")
        self.name.pack(pady=(100,0))
        self.name.bind('<Button-1>', self.select_name)

        self.pas = Entry(self, relief="flat", width=30)
        self.pas.insert(END, "(Password)")
        self.pas.pack(pady=(15,0))
        self.pas.bind('<Button-1>', self.select_pas)

        self.btn = Button(self, text="Ingresar", width=25, background="grey",
        foreground="white", relief="flat", command=self.entrar)
        self.btn.pack(pady=(15,0))
        self.btn.bind('<Enter>',lambda e: e.widget.config(fg="#7FB3D5"))
        self.btn.bind('<Leave>',lambda e: e.widget.config(fg="white"))

    def select_name(self, event):
        txt_name = self.name.get()
        txt_pas = self.pas.get()
        if txt_name == "(User name)":
            self.name.delete('0','end')

    def select_pas(self, event):
        txt_name = self.name.get()
        txt_pas = self.pas.get()

        if txt_pas == "(Password)":
            self.pas.delete('0','end')
            self.pas.config(show="*")

        if txt_name == "":
            self.name.insert(END,"(User name)")

    def entrar(self):
        txt_name = self.name.get()
        txt_pas = self.pas.get()
        con = conexion.Connect(txt_name, txt_pas)
        if con:
            self.destroy()
            cpanel.init(txt_name, txt_pas)
        else:
            print("Usuario o contraseña incorrectos")


if __name__ == '__main__':
    main = Main()
    main.mainloop()