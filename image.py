import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import mysql.connector

# Connect to the MySQL database
myconn = mysql.connector.connect(
    host="localhost",
    user="Eman",
    password="rosegirl334@",
    database='PIC'
)

my_w = tk.Tk()
my_w.geometry("650x450")
my_w.title("Uploading Image")

font1 = ['Times New Roman', 20, "bold"]
l1 = tk.Label(my_w, text="Upload File", font=24, bg='lightgreen')
l1.grid(row=0, column=0, padx=10, pady=20)

useridEntry = Entry(my_w, width=25, font=('Times New Roman', 10))
useridEntry.place(x=100, y=10)

b1 = tk.Button(my_w, text="Upload", command=lambda: my_upload())
b1.grid(row=3, column=2, padx=5)

b2 = tk.Button(my_w, text="Add Data", command=lambda: my_add())
b2.grid(row=3, column=7)

global filename, img

def my_upload():
    global filename, img
    f_types = [("All files", '*.*'), ('JPG', '*.jpg'), ('PNG', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    b3 = tk.Button(my_w, image=img)
    b3.grid(row=4, column=1, columnspan=3, pady=20)

def my_add():
    global filename
    flag_validation = True
    with open(filename, 'rb') as fob:
        fob = fob.read()
    my_data = (None, fob)
    my_query = "INSERT INTO pictures VALUES(%s,%s)"
    cursor = myconn.cursor()
    cursor.execute(my_query, my_data)
    myconn.commit()
    messagebox.showinfo('Success','Image Uploaded Successfully')
    cursor.close()

my_w.mainloop()
