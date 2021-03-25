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
        #create a label and entry for a verb
        Label(self,
              text = "Verb: "
              ).grid(row = 3, column = 0, sticky= W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column= 0, sticky =W)
        #create a label for adjectoves check buttons
        Label(self,
              text = "Adjective(s): "
              ).grid(row = 4, column = 0, sticky = W)
        self.is_icthy = BooleanVar()
        Checkbutton(self,
                    text = "icthy",
                    variable = self.is_icthy
                    ).grid(row = 4, column = 1, sticky = W)
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text="joyous",
                    variable=self.is_joyous
                    ).grid(row=4, column=2, sticky=W)
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text="electric",
                    variable=self.is_electric
                    ).grid(row=4, column=3, sticky=W)
        Label(self,
              text = "Body Part:"
              ).grid(row = 5, column = 0, sticky = W)
        self.body_part = StringVar()
        self.body_part.set(None)
        body_parts = ["belly button", "big toe", "medulla oblongata"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part
                        ).grid(row = 5, column = column, sticky = W)
            self.story_txt = Text(self, width = 75, height= 10, wrap = WORD)
            self.story_txt.grid(row = 7, column = 0, columnspan = 4)
            
