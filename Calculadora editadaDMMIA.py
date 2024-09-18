from tkinter import Tk, Label, Button, Entry


class Root(Tk):

    def __init__(self):
        super().__init__()
        self.title_label = Label(self, text=" Olá eu sou uma simples \n calculadora que vai ajudar\n você no teus calcúlos \nchamam-me DMMIA :)")
        self.title_label.pack()
        self.entry = Entry(self)
        self.entry.pack()
        self.entry.insert(0, "2+2")
        self.label = Label(self, text="Diamantino")
        self.label.pack()
        self.button = Button(self, text="Ok", command=self.onclick)
        self.button.pack()

    def onclick(self):
        self.label.configure(text=str(eval(self.entry.get())))
root = Root()
root.mainloop()
