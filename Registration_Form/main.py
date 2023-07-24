from tkinter import *
import tkinter.messagebox as msg

#built-in function of Tkinter which is allowing you to create a window for our application.  we are giving the window name root
root = Tk() 
# built-in attribute of tkinter to provide fix w*h
root.geometry('400x400') 
root.title("Registration Form")

# to make changes in the window
#root.config(bg="cadetblue") 

def register_data():
    import mysql.connector as cnct
    mydb = cnct.connect(host='localhost',user='root',password='pakhi',database='registration_form')

    # it is used to check whether all this configuration passed is correct or not. 
    # or it is used to use all the sql command in python
    cur = mydb.cursor()
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    query = "insert into registration values('{}','{}','{}')".format(username,password,email)
    cur.execute(query)
    mydb.commit()
    #to show the message
    msg.showinfo("Registraion","Registered Successfully")

# to insert any text in the window we use Label attribute.
username_label = Label(root,text="Username:",bg="white",font=("italic",'15'))
username_label.place(x=20,y=50) #place for the text

password_label = Label(root,text = "Password:", bg = "white", font = ('italic',15))
password_label.place(x=20,y=150)

email_label = Label(root,text = "Email:", bg = "white", font = ('italic',15))
email_label.place(x=20,y=250)

username_entry = Entry()
username_entry.place(x=220,y=55)

password_entry = Entry()
password_entry.place(x=220,y=155)

email_entry = Entry()
email_entry.place(x=220,y=255)

register_button = Button(root,text="Register", command=register_data)
register_button.place(x=150,y=320)

root.mainloop() # we are using it to access that particular window on our screen.