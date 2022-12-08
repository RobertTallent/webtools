#Credentials.py: a program function (primarily for "login") to enter and store credentials

from tkinter import *
from tkinter import messagebox

class Credentials:
    credentialsInstructions = '''Enter your login credentials.

    Click 'Enter' once you have entered them.'''
    root = Tk()
    title = root.title("Login Credentials")
    instructions = Label(root,text=credentialsInstructions)
    usrnm = Entry(root, text="username")
    pw = Entry(root, text="password", show='*')
    
    @classmethod #before init because it must be defined before called
    def ConfirmCredentials(cls):
        cls.response = messagebox.askyesno("Confirm","Are you sure your credentials are correct?")
        if cls.response == True:
            cls.usrnm = cls.usrnm.get()
            cls.pw = cls.pw.get()
            cls.root.destroy()
    
    def __init__(self):
        self.credentials_button = Button(self.root, text="Enter",command=self.ConfirmCredentials)
        self.instructions.pack()
        self.instructions.pack()
        self.usrnm.pack()
        self.pw.pack()
        self.credentials_button.pack()
        self.root.mainloop()
    
    #TODO add padding to edges
    #TODO delete credentials from python variables

if __name__ == "__main__":
    Credentials()