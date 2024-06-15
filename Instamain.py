from tkinter import *
from PIL import ImageTk
import profilepage
import mysql.connector
mydb = mysql.connector.connect(
                        host="localhost",
                        user="Eman",
                        password="rosegirl334@",
                        database="UserData"
                    )
mycursor = mydb.cursor()

class Instagram:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram")
        
        self.bgImage = ImageTk.PhotoImage(file='images.jpg')
        
        bgLabel = Label(self.root, image=self.bgImage)
        bgLabel.grid(row=0, column=0)
        
        self.frame = Frame(self.root, bg="black")
        self.frame.place(x=15, y=15, width=1240, height=800)
        
        self.menu_bar = Frame(root, bg='black', highlightbackground="white", highlightthickness=1)
        self.menu_bar.place(x=20, y=20, width=50, height=800)
        
        #------FUNCTIONALITY PART-----
        def switch_indication(indication_lb):
            self.home_btn_indicator.config(bg='black')
            self.create_btn_indicator.config(bg='black')
            self.like_btn_indicator.config(bg='black')
            self.message_btn_indicator.config(bg='black')
            self.search_btn_indicator.config(bg='black')
            indication_lb.config(bg='white')

        def profile_page():
            self.root.destroy()
            profilepage.Uploading(Tk())
            
        self.instagram=ImageTk.PhotoImage(file='insta1.jpeg')
        self.instagram_menu_button=Button(root,image=self.instagram,bg='black',bd=0,activebackground='black',fg='white')
        self.instagram_menu_button.place(x=30,y=30,width=30,height=40)
        
        self.homeicon=ImageTk.PhotoImage(file='home_icon.png')
        self.home_icon=Button(root,image=self.homeicon,bd=0,bg='black',activebackground='black',command=lambda:switch_indication(indication_lb=self.home_btn_indicator))
        self.home_icon.place(x=30,y=170,width=30)
        self.home_btn_indicator=Label(root,bg='black')
        self.home_btn_indicator.place(x=25,y=165,height=35,width=2)
        
        self.searchicon=ImageTk.PhotoImage(file='search.jpeg')
        self.search_icon=Button(root,image=self.searchicon,bd=0,bg='black',activebackground='black',command=lambda:switch_indication(indication_lb=self.search_btn_indicator))
        self.search_icon.place(x=35,y=220,width=25,height=30)
        self.search_btn_indicator=Label(root,bg='black')
        self.search_btn_indicator.place(x=25,y=215,height=30,width=2)
        
        self.messageicon=ImageTk.PhotoImage(file='message.jpeg')
        self.message_icon=Button(root,image=self.messageicon,bd=0,fg='white',command=lambda:switch_indication(indication_lb=self.message_btn_indicator))
        self.message_icon.place(x=30,y=330,width=30,height=35)
        self.message_btn_indicator=Label(root,bg='black')
        self.message_btn_indicator.place(x=25,y=330,height=35,width=2)
        
        self.likeicon=ImageTk.PhotoImage(file='h1.jpeg')
        self.like_icon=Button(root,image=self.likeicon,bd=0,fg='white',command=lambda:switch_indication(indication_lb=self.like_btn_indicator))
        self.like_icon.place(x=30,y=270,width=30,height=40)
        self.like_btn_indicator=Label(root,bg='black')
        self.like_btn_indicator.place(x=25,y=270,height=30,width=2)
        
        self.createicon=ImageTk.PhotoImage(file='create1.jpeg')
        self.create_icon=Button(root,image=self.createicon,bd=0,fg='white',command=lambda:switch_indication(indication_lb=self.create_btn_indicator))
        self.create_icon.place(x=30,y=390,width=30,height=35)
        self.create_btn_indicator=Label(root,bg='black')
        self.create_btn_indicator.place(x=25,y=390,height=35,width=2)
        
        self.toggleicon=PhotoImage(file='toggle_btn_icon.png')
        self.toggle_icon=Button(root,image=self.toggleicon,bg='black',bd=0,activebackground='black',fg='white')
        self.toggle_icon.place(x=30,y=600,width=30,height=40)
        
        self.profileicon=ImageTk.PhotoImage(file='prof.jpg')
        self.profile_icon=Button(root,image=self.profileicon,bg='black',bd=0,activebackground='black',fg='white',command=profile_page())
        self.profile_icon.place(x=30,y=540,width=30,height=40)
    
if __name__=="__main__":
    root = Tk()
    insta = Instagram(root)
    root.mainloop()
