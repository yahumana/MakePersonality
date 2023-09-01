import customtkinter as ctk
from tkinter import StringVar

from logics.makePersonality import MakePersonality
from logics.makePassword import make_password


class App(ctk.CTk):
    """
        Main app ctk window class
    """

    def __init__(self, mp: MakePersonality):
        super().__init__()
        self.geometry("550x175")
        self.title("Make personality")

        self.country_text = StringVar(self)
        self.sex = StringVar(self)
        self.name = StringVar(self)
        self.lastname = StringVar(self)
        self.dob = StringVar(self)
        self.password = StringVar(self)
        self.username = StringVar(self)

        self.mp = mp

        self.label_country = ctk.CTkLabel(self, text="Country code")
        self.label_country.grid(row=0, column=0, padx=5, pady=10)
        self.country_entry = ctk.CTkEntry(self, placeholder_text="Country code",
                                          textvariable=self.country_text)
        self.country_entry.grid(row=0, column=1, padx=5, pady=10)
        self.label_sex = ctk.CTkLabel(self, text="Sex")
        self.label_sex.grid(row=0, column=2, padx=10, pady=10)
        self.sex_entry = ctk.CTkEntry(self, placeholder_text="Sex",
                                      textvariable=self.sex)
        self.sex_entry.grid(row=0, column=3, padx=5, pady=10)

        self.label_name = ctk.CTkLabel(self, text="Name")
        self.label_name.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = ctk.CTkEntry(self, textvariable=self.name)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.label_lastname = ctk.CTkLabel(self, text="Lastname")
        self.label_lastname.grid(row=1, column=2, padx=10, pady=5)
        self.lastname_entry = ctk.CTkEntry(self, textvariable=self.lastname)
        self.lastname_entry.grid(row=1, column=3, padx=5, pady=5)

        self.label_dob = ctk.CTkLabel(self, text="Date of birth")
        self.label_dob.grid(row=2, column=0, padx=5, pady=5)
        self.dob_entry = ctk.CTkEntry(self, textvariable=self.dob)
        self.dob_entry.grid(row=2, column=1, padx=5, pady=5)
        self.label_username = ctk.CTkLabel(self, text="Username")
        self.label_username.grid(row=2, column=2, padx=10, pady=5)
        self.username_entry = ctk.CTkEntry(self, textvariable=self.username)
        self.username_entry.grid(row=2, column=3, padx=5, pady=5)

        self.label_password = ctk.CTkLabel(self, text="Password")
        self.label_password.grid(row=3, column=0, padx=5, pady=5)
        self.entry_password = ctk.CTkEntry(self, textvariable=self.password)
        self.entry_password.grid(row=3, column=1, padx=5, pady=5)
        self.password_button = ctk.CTkButton(self, text="Gen password", command=self.change_password)
        self.password_button.grid(row=3, column=2, padx=5, pady=5)
        self.button_create = ctk.CTkButton(self, text="Make new", command=self.create)
        self.button_create.grid(row=3, column=3, padx=10, pady=10)

        self.view_personality()
        self.change_password()

    def view_personality(self):
        mp_list = self.mp.get_personality()

        self.country_text.set(mp_list['country'])
        self.dob.set(mp_list['dob'])
        self.username.set(mp_list['username'])
        self.sex.set(mp_list['sex'])
        self.name.set(mp_list['name'])
        self.lastname.set(mp_list['lastname'])

    def create(self):
        self.mp.set_country(self.country_text.get())
        self.mp.set_gender(self.sex.get())
        self.mp.gen_personality()
        self.view_personality()

    def change_password(self):
        self.password.set(make_password())


if __name__ == '__main__':
    mp = MakePersonality(country="RU")

    app = App(mp)
    app.mainloop()
