from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text="enter info for story",
              ).grid(row=0, column=0, columnspan=2, sticky=W)
        Label(self,
              text="Person: ",
              ).grid(row=1, column=0, sticky=W)

        self.person_ent + Entry(self),
        self.person_ent.grid(row=1, column=1, sticky=W)

        Label(self,
              text="Plural noun"
              ).grid(row=2, column=2, sticky=W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row=2, column=1, sticky=W)