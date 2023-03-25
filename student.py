from tkinter import *

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("EKS School Managenent")
        self.root.geometry("1350x700+0+0")


root=Tk()
ob=Student(root)
root.mainloop()