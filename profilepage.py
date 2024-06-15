from tkinter import *
from tkinter import filedialog, messagebox
import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import Instamain

myconn = mysql.connector.connect(
    host="localhost",
    user="Eman",
    password="rosegirl334@",
    database='UserData'
)

class Uploading:
    def __init__(self, root):
        self.my_w = root
        self.filename = None
        
        self.image1=ImageTk.PhotoImage(file="instagram.jpg")
        self.imglabel=Label(self.my_w,image=self.image1)
        self.imglabel.grid(row=0,column=0)
        
        frame = Frame(self.my_w, bg="white")
        frame.place(x=500, y=145, width=340, height=450)
        
        self.l1 = Label(self.my_w, text="Add Profile", font=('Times New Roman', 20, 'bold'), bg='Deep Pink')
        self.l1.place(x=620, y=200)
        
        self.profile_logo=ImageTk.PhotoImage(file='profile.jpg')
        self.image_label=Label(self.my_w,image=self.profile_logo)
        self.image_label.place(x=580,y=260 ,width=200,height=200)
        
        self.b1 = Button(self.my_w, text="Upload", command=self.my_upload)
        self.b1.place(x=600, y=500)

        self.b2 = Button(self.my_w, text="Add Data", command=self.my_add)
        self.b2.place(x=700, y=500)
        
    def my_upload(self):
        f_types = [("All files", '*.*'), ('JPG', '*.jpg'), ('PNG', '*.png')]
        self.filename = filedialog.askopenfilename(filetypes=f_types)
        self.img = Image.open(self.filename)
        self.img.thumbnail((100, 100))  # Resize image to fit the label
        self.img = ImageTk.PhotoImage(self.img)
        self.image_label.config(image=self.img)
         
    def my_add(self):
        if self.filename:
            with open(self.filename, 'rb') as fob:
                data = fob.read()
                cursor = myconn.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS PIC (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            image LONGBLOB,
                            FOREIGN KEY (id) REFERENCES DATA(id)
                        )''')
                
                my_query = "INSERT INTO PIC (image) VALUES(%s)"
                cursor.execute(my_query, (data,))
                myconn.commit()
                messagebox.showinfo('Success', 'Image Uploaded Successfully')
                cursor.close()
                #self.my_w.destroy()
                #Instamain.Instagram(Tk())
        else:
            messagebox.showerror('Error', 'Please upload an image first')
            self.my_add()

if __name__ == "__main__":
    my_w = Tk()
    obj = Uploading(my_w)
    my_w.mainloop()
    
