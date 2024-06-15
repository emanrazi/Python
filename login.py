from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
import Instamain
import signup
import images
import changepassword
class Login:
    def __init__(self, root):
        # GUI PART
        self.root = root
        self.root.title("Instagram Login")
        self.bgImage = ImageTk.PhotoImage(file='instagram.jpg')

        bgLabel = Label(self.root, image=self.bgImage)
        bgLabel.grid(row=0, column=0)

        frame = Frame(self.root, bg="white")
        frame.place(x=500, y=145, width=340, height=450)

        heading = Label(root, text="Instagram Login", font=('Script', 30, 'bold'), bg='white', fg='purple')
        heading.place(x=580, y=190)

        # FUNCTIONAL PART
        def user_enter(event):
            if self.usernameEntry.get() == 'Username':
                self.usernameEntry.delete(0, END)

        def password_enter(event):
            if self.passwordentry.get() == 'Password':
                self.passwordentry.delete(0, END)
          
        def Open():
             self.eyeButton.config(image=self.openeye)
             self.passwordentry.config(show='')
             self.eyeButton.config(command=hide)
                  
        def hide():
             self.eyeButton.config(image=self.closeeye)
             self.passwordentry.config(show='*')
             self.eyeButton.config(command=Open)
             
        def create_account():
            self.root.destroy()
            signup.SignUp(Tk())
             
        def reset_pass():
            self.root.destroy()
            changepassword.Change(Tk())
             
        #---------DATABASE CONNECTIVITY-----
        def login_user():
            if((self.usernameEntry.get()==''or self.usernameEntry.get()=='Username') or (self.passwordentry.get()=='' or self.passwordentry.get()=='Password')):
                messagebox.showerror('Error','Fields must be specified')
            else:
                try:
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="Eman",
                        password="rosegirl334@"
                    )
                    mycursor = mydb.cursor()
                except:
                    messagebox.showerror('Error','Connection is not established,Try Again')
                    return
                mycursor.execute('USE UserData')
                query='SELECT *from DATA where username=%s AND password=%s'
                mycursor.execute(query,(self.usernameEntry.get(),self.passwordentry.get()))
                row=mycursor.fetchone()
                if row == None:
                    messagebox.showerror('Error',"Invalid username or password")
                else:
                    messagebox.showinfo('Success','Login Successfull')
                    self.root.destroy()
                    images.Uploading(Tk())
                                
        #----------------------------------------------
             
        # ENTRY FIELD
        self.usernameEntry = Entry(root, width=25,font=('Times New Roman',10))
        self.usernameEntry.place(x=570, y=280)
        self.usernameEntry.insert(0, 'Username')
        self.usernameEntry.bind('<FocusIn>', user_enter)

        self.passwordentry = Entry(root, width=25,font=('Times New Roman',10))
        self.passwordentry.place(x=570, y=330)
        self.passwordentry.insert(0, 'Password')
        self.passwordentry.bind('<FocusIn>', password_enter)

        self.openeye = ImageTk.PhotoImage(file='open.jpeg')
        self.closeeye = ImageTk.PhotoImage(file='close.jpeg')
        self.eyeButton = Button(self.root, image=self.openeye,bd=0,bg='white',cursor='hand2',command=hide)
        self.eyeButton.place(x=750, y=325, width=25, height=25)
        
        self.forgetButton = Button(self.root, text='Forgot Password?',command=reset_pass,font=('Times New Roman',10),bd=0,bg='white',fg='Dark Blue',cursor='hand2')
        self.forgetButton.place(x=515, y=370, width=200, height=25)
        
        self.forgetButton = Button(self.root, text='Login',font=('Times New Roman',10),bd=0,bg='Blue',fg='white',command=login_user)
        self.forgetButton.place(x=550, y=400, width=230, height=25)
        
        self.orLabel=Label(self.root,text='__________OR___________',font=('Times New Roman',13),bd=0,bg='white',fg='Black')
        self.orLabel.place(x=565,y=440)
        
        self.textButton=Button(self.root,text="Continue with facebook",font=('Times New Roman',10),bd=0,cursor='hand2',bg='white',fg='Dark Blue')
        self.textButton.place(x=600,y=470)
        
        self.textLabel=Label(root,text='do not have an account?',font=('Times New Roman',10),bd=0,bg='white',fg='Black')
        self.textLabel.place(x=550,y=550)
        
        self.textButton2=Button(root,text='Sign Up',font=('Times New Roman',10),bd=0,bg='white',fg='Dark Blue',cursor='hand2',command=create_account)
        self.textButton2.place(x=685,y=550)
        
if __name__ == "__main__":
    root = Tk()
    log = Login(root)
    root.mainloop()
