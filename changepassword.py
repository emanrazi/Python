from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
import login

class Change:
    def __init__(self, root):
        # GUI PART
        self.root = root
        self.root.title("RESET PASSWORD")
        self.bgImage = ImageTk.PhotoImage(file='instagram.jpg')

        bgLabel = Label(self.root, image=self.bgImage)
        bgLabel.grid(row=0, column=0)

        frame = Frame(self.root, bg="white")
        frame.place(x=500, y=145, width=340, height=450)

        heading = Label(root, text="Reset Password", font=('Script', 30, 'bold'), bg='white', fg='purple')
        heading.place(x=580, y=190)

        # FUNCTIONAL PART
        def user_enter(event):
            if self.usernameEntry.get() == 'Username':
                self.usernameEntry.delete(0, END)

        def password_enter(event):
            if self.passwordentry.get() == 'New Password':
                self.passwordentry.delete(0, END)
                
        def newpassword_enter(event):
            if self.newpasswordEntry.get() == 'Confirm Password':
                self.newpasswordEntry.delete(0, END)
                
        def clear():
            self.usernameEntry.delete(0,END)
            self.passwordentry.delete(0,END)
            self.newpasswordEntry.delete(0,END) 
          
             
        #---------DATABASE CONNECTIVITY-----
        def login_user():
            if((self.usernameEntry.get()==''or self.usernameEntry.get()=='Username') or (self.passwordentry.get()=='' or self.passwordentry.get()=='New Password') or (self.newpasswordEntry.get() == '' or self.newpasswordEntry.get() == 'Confirm Password')):
                messagebox.showerror('Error','Fields must be specified')
                
            elif self.passwordentry.get() != self.newpasswordEntry.get():
                messagebox.showerror('Error', 'Passwords must be the same')
                
            else:
                try:
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="Eman",
                        password="rosegirl334@"
                    )
                    mycursor = mydb.cursor()
                except:
                    messagebox.showerror('Error','Connection Error')
                    return
                try:
                    mycursor.execute('USE UserData')
                    query = 'SELECT * FROM DATA WHERE username=%s'
                    mycursor.execute(query, (self.usernameEntry.get(),))
                    row = mycursor.fetchone()
                    if row:
                        update_query = 'UPDATE DATA SET password=%s WHERE username=%s'
                        mycursor.execute(update_query, (self.newpasswordEntry.get(), self.usernameEntry.get()))
                        mydb.commit()
                        messagebox.showinfo('Success', 'Password Changed Successfully')
                        clear()
                    else:
                        messagebox.showinfo('Error','Incorrect Username')
                except :
                    messagebox.showerror('Error','Query error')
                finally:
                    mydb.close()
                    self.root.destroy()
                    login.Login(Tk())
                    
                    
        #----------------------------------------------
             
        # ENTRY FIELD
        self.usernameEntry = Entry(root, width=25, font=('Times New Roman', 10))
        self.usernameEntry.place(x=570, y=280)
        self.usernameEntry.insert(0, 'Username')
        self.usernameEntry.bind('<FocusIn>', user_enter)

        self.passwordentry = Entry(root, width=25, font=('Times New Roman', 10))
        self.passwordentry.place(x=570, y=330)
        self.passwordentry.insert(0, 'New Password')
        self.passwordentry.bind('<FocusIn>', password_enter)
        
        self.newpasswordEntry = Entry(root, width=25, font=('Times New Roman', 10))
        self.newpasswordEntry.place(x=570, y=380)
        self.newpasswordEntry.insert(0, 'Confirm Password')
        self.newpasswordEntry.bind('<FocusIn>', newpassword_enter)
        
        self.forgetButton = Button(self.root, text='Submit', font=('Times New Roman', 10), bd=0, bg='Blue', fg='white', command=login_user)
        self.forgetButton.place(x=550, y=450, width=230, height=25)
        
if __name__ == "__main__":
    root = Tk()
    log = Change(root)
    root.mainloop()
