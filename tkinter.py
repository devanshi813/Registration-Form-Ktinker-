from tkinter import *
class Login(Frame):
    def init(self,master):
        super().init()
        self.l1=Label(self,text='User Name',bg='lime',fg='magenta',font=('olephant',15),justify="center")
        self.l2=Label(self,text='Password',bg='lime',fg='magenta',font=('olephant',15),justify="center")
        self.t1=Entry(self,bg='lime',fg='magenta',font=('olephant',15),justify="center",bd=6)
        self.t2=Entry(self,show='*',bg='lime',fg='magenta',font=('olephant',15),justify="center",bd=6)
        self.b1=Button(self,text="Login",bg='lime',fg='magenta',font=('olephant',15),justify="center",bd=6)
        self.rowconfigure(index=0,pad=15)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)
        self.l1.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)

        self.l2.grid(row=1,column=0)
        self.t2.grid(row=1,column=1)

        self.b1.grid(columnspan=2)

        self.pack()
root=Tk()
ob=Login(root)
root.title('Login')
root.geometry('450x200')
root.mainloop()