from tkinter import *
class Demo(Frame):
    def __init__(self):
        super().__init__()
        self.b1=Button(self,text="click")
        self.b1.grid(row=0, column=0)
        
obj = Tk()
abc = Demo(obj)
obj.title("Ducat")
obj.geometry("300*350")
obj.state("zoomed")
obj.config(bg = 'pink')
obj.mainloop()
