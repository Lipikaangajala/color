from tkinter import *
import random
root=Tk()
root.geometry("600x600")
root.title("Encapsulation")



list1=["red","blue","purple","green"]
label=Label(root)
label.place(relx=0.5,rely=0.5,anchor=CENTER)
list2=["RED","BLUE","PURPLE","GREEN"]

class color:

    def __init__(self):
        self.score=0
     
    def updateGame(self):
        
        self.text=list2
        self.random_number_for_text=random.randint(0,3)
        self.color=list1
        self.random_number_for_color=random.randint(0,3)
        label["text"]=self.text[self.random_number_for_text]
        label["fg"]=self.color[self.random_number_for_color]
       
        
        
obj=color()       
btn=Button(root,text="Start",bg="green",fg="white",command=obj.updateGame)
btn.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()