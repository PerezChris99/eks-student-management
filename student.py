from tkinter import *

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("EKS Student Managenent")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="EKS Student Managenent", font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP)


root=Tk()
ob=Student(root)
root.mainloop()