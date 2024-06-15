from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
import login

class SignUp:
    def __init__(self, root):
        # GUI PART
        self.root = root
        self.root.title("Instagram SignUp")
        self.bgImage = ImageTk.PhotoImage(file='instagram.jpg')

        bgLabel = Label(self.root, image=self.bgImage)
        bgLabel.grid(row=0, column=0)

        frame = Frame(self.root, bg="white")
        frame.place(x=500, y=145, width=340, height=450)

        heading = Label(root, text="Instagram SignUp", font=('Script', 30, 'bold'), bg='white', fg='black')
        heading.place(x=580, y=170)

        # FUNCTIONAL PART
        def email_enter(event):
            if self.emailEntry.get() == 'Mobile Number or Email':
                self.emailEntry.delete(0, END)
                
        def name_enter(event):
            if self.nameEntry.get() == 'Full Name':
                self.nameEntry.delete(0, END)
                
        def username_enter(event):
            if self.usernameEntry.get() == 'UserName':
                self.usernameEntry.delete(0, END)

        def password_enter(event):
            if self.passwordentry.get() == 'Password':
                self.passwordentry.delete(0, END)
                
        def conpassword_enter(event):
            if self.conpasswordentry.get() == 'Confirm Password':
                self.conpasswordentry.delete(0, END)
                
        def login_page():
            self.root.destroy()
            login.Login(Tk())
            
        def clear():
            self.emailEntry.delete(0,END)
            self.conpasswordentry.delete(0,END)
            self.usernameEntry.delete(0,END)
            self.passwordentry.delete(0,END)
            self.nameEntry.delete(0,END) 
                 
        #-------DATABASE CONECTIVITY------
        def connect_database():
            if (self.emailEntry.get() == 'Mobile Number or Email' or self.emailEntry.get() == '') or (self.nameEntry.get() == 'Full Name' or self.nameEntry.get() == '') or (self.usernameEntry.get() == 'User Name' or self.usernameEntry.get() == '') or (self.passwordentry.get() == 'Password' or self.passwordentry.get() == '') or (self.conpasswordentry.get() == 'Confirm Password' or self.conpasswordentry.get() == ''):
                messagebox.showerror('Error', 'All fields are required')
            elif self.passwordentry.get() != self.conpasswordentry.get():
                messagebox.showerror('Error', 'Passwords must be the same')
            elif check.get() == 0:
                messagebox.showerror('Error', 'Please accept terms and conditions')
            else:
                try:
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="Eman",
                        password="rosegirl334@",
                        database="UserData"
                    )
                    mycursor = mydb.cursor()
                except :
                        mycursor.execute('CREATE DATABASE UserData')
                        mycursor.execute('USE UserData')
                        mycursor.execute('''CREATE TABLE DATA (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            email VARCHAR(50),
                            username VARCHAR(50),
                            password VARCHAR(50),
                            image LONDBLOB
                        )''')
                
                query = 'SELECT * FROM DATA WHERE username=%s'
                mycursor.execute(query, (self.usernameEntry.get(),))
                row = mycursor.fetchone()
                if row is not None:
                    messagebox.showerror('Error', 'Username already exists')
                else:
                    query = 'INSERT INTO DATA (email, username, password) VALUES (%s, %s, %s)'
                    mycursor.execute(query, (self.emailEntry.get(), self.usernameEntry.get(), self.conpasswordentry.get()))
                    mydb.commit()
                    mydb.close()
                    messagebox.showinfo('Success', 'Registration Successful')
                    clear()
                    self.root.destroy()
                    login.Login(Tk())
               
        #-----------------------------------------------------------         
        self.textButton2 = Button(root, text='Login with facebook', font=('Times New Roman', 10), bd=0, bg='Blue', fg='White', cursor='hand2')
        self.textButton2.place(x=530, y=240, width=290)
        
        self.orLabel = Label(self.root, text='OR', font=('Times New Roman', 10), bd=0, bg='white', fg='Black')
        self.orLabel.place(x=650, y=270)
        
        # ENTRY FIELD
        self.emailEntry = Entry(root, font=('Times New Roman', 10))
        self.emailEntry.place(x=530, y=300, width=250)
        self.emailEntry.insert(0, 'Mobile Number or Email')
        self.emailEntry.bind('<FocusIn>', email_enter)
        
        self.nameEntry = Entry(root, font=('Times New Roman', 10))
        self.nameEntry.place(x=530, y=330, width=250)
        self.nameEntry.insert(0, 'Full Name')
        self.nameEntry.bind('<FocusIn>', name_enter)
        
        self.usernameEntry = Entry(root, font=('Times New Roman', 10))
        self.usernameEntry.place(x=530, y=360, width=250)
        self.usernameEntry.insert(0, 'UserName')
        self.usernameEntry.bind('<FocusIn>', username_enter)

        self.passwordentry = Entry(root, font=('Times New Roman', 10))
        self.passwordentry.place(x=530, y=400, width=250)
        self.passwordentry.insert(0, 'Password')
        self.passwordentry.bind('<FocusIn>', password_enter)
        
        self.conpasswordentry = Entry(root, font=('Times New Roman', 10))
        self.conpasswordentry.place(x=530, y=440, width=250)
        self.conpasswordentry.insert(0, 'Confirm Password')
        self.conpasswordentry.bind('<FocusIn>', conpassword_enter)
        
        
        check = IntVar()
        self.checkbutton = Checkbutton(self.root, text="I agree to the Terms & Conditions", bd=0, fg='Dark Blue', bg='white', font=('Times New Roman', 10), variable=check)
        self.checkbutton.place(x=550, y=490)
        
        self.signupButton = Button(self.root, text='Sign Up', font=('Times New Roman', 10), bd=0, bg='Blue', fg='white', command=connect_database)
        self.signupButton.place(x=550, y=530, width=230, height=25)
        
        self.account = Label(text="Already have an account?", font=('Arial', 8), bd=0, bg='white')
        self.account.place(x=560, y=565)
        
        self.logButton = Button(text="Log In", bd=0, font=('Arial', 8), fg='Dark Blue', bg='white', command=login_page)
        self.logButton.place(x=690, y=563)
        
        
if __name__ == "__main__":
    from im import fun
    root = Tk()
    log = SignUp(root)
    root.mainloop()
