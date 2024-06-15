import os
import time
import random
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def ClearScreen():
     os.system('cls' if os.name == 'nt' else 'clear')
  
def pause():
    input("Press Enter to continue...")
       
class LMS:
    
    def Login(self):
        print("Login")
        self.username = input("Enter user name: ")
        self.user_type=(input("Enter user type: "))
        self.password = input("Enter password: ")
        
        if(self.user_type.casefold()=="Staff".casefold()):
         with open("files/Staff.txt",'r') as f:
            found = False
            for line in f:
                stored_id,stored_password,stored_username,stored_type,stored_email = line.strip().split("\t")
                if  stored_type.casefold()==self.user_type.casefold()  and stored_username == self.username and stored_password == self.password:
                    found = True
                    print("Login successful!")
                    self.Menu()
            if not found:
                print("Inalid username or type.")
                
        if(self.user_type.casefold()=="Student".casefold()):
         with open("files/Student.txt",'r') as f:
            found = False
            for line in f:
                stored_id,stored_password,stored_username,stored_type,stored_email = line.strip().split("\t")
                if  stored_type.casefold()==self.user_type.casefold()  and stored_username == self.username and stored_password == self.password:
                    found = True
                    print("Login successful!")
                    self.Main_Menu()
            if not found:
                print("Inalid username or type.")
                
        if(self.user_type.casefold()=="Librarian".casefold()):
         with open("files/Librarian.txt",'r') as f:
            found = False
            for line in f:
                stored_id,stored_password,stored_username,stored_type,stored_email = line.strip().split("\t")
                if  stored_type.casefold()==self.user_type.casefold()  and stored_username == self.username and stored_password == self.password:
                    found = True
                    print("Login successful!")  
                    self.Menu()
            if not found:
                print("Inalid username or type.")
 
    def Register(self):
        print("Registeration")
        while True:
         self.userid=int(input("Enter user id: "))
         self.username=input("Enter user name: ")
         self.usertype=input("Enter user type Student/Staff/Librarian: ")
         self.user_email=input("Enter user email: ")
         self.password=input("Enter password: ")
         
         if(self.usertype.casefold()=="Staff".casefold()):
          with open("files/Staff.txt",'a') as f:
            f.write(str(self.userid))
            f.write("\t")
            f.write(self.password )
            f.write("\t")
            f.write(self.username)
            f.write("\t")
            f.write(self.usertype)
            f.write("\t")
            f.write(self.user_email)
            f.write("\n")
            choice=int(input("Press 1 to continue and 0 to stop: "))
            if(choice==0):
                break
            
         if(self.usertype.casefold()=="Student".casefold()):
          with open("files/Student.txt",'a') as f:
            f.write(str(self.userid))
            f.write("\t")
            f.write(self.password )
            f.write("\t")
            f.write(self.username)
            f.write("\t")
            f.write(self.usertype)
            f.write("\t")
            f.write(self.user_email)
            f.write("\n")
            choice=int(input("Press 1 to continue and 0 to stop: "))
            if(choice==0):
                break
        
         if(self.usertype.casefold()=="Librarian".casefold()):
          with open("files/Librarian.txt",'a') as f:
            f.write(str(self.userid))
            f.write("\t")
            f.write(self.password )
            f.write("\t")
            f.write(self.username)
            f.write("\t")
            f.write(self.usertype)
            f.write("\t")
            f.write(self.user_email)
            f.write("\n")
            choice=int(input("Press 1 to continue and 0 to stop: "))
            if(choice==0):
                break     
         else:
             print("Invalid Type")
            
    def Logout(self):
        print("Logged out Successfully")   
    
            
    @staticmethod
    def Main_Menu(): 
        print("        1. User         ")
        print("        2. Account       ")
        print("        3. Librarian     ")
        print("        4. Book          ")
        print("        5. Library Database")
        print("        6. Exiting ")
        
        choice=int(input("Enter your choice: "))  
        if(choice==1):
            user=User()
            user.Menu()
                             
        elif(choice==2):
            acc=Account()
            acc.Menu()
            
        elif(choice==3):
            lib=Librarian()
            lib.Menu()
                    
        elif choice==4:
            book=Book()
            book.Menu()
        
        elif choice==5:
             libdata=Librarydatabase()
             libdata.Main()
                
        else:
            print("Invalid chhoice")
                
class User:
    def Verify(self):
        print("verification of your account")
        self.user_email=input("Enter your login email for verification: ")
        self.user_type=input("Enter usertype Staff/Student: ")
        
        if self.user_type.casefold()=="Staff".casefold() or self.user_type.casefold()=="Student".casefold():
         if(self.user_type.casefold()=="Staff".casefold()):
          with open("files/Staff.txt",'r') as f:
            found = False
            for line in f:
                stored_id,stored_password,stored_username,stored_type,stored_email = line.strip().split("\t")
                if stored_email==self.user_email:
                    found = True
                    number=random.randint(5000,100000)
                    print(" your verification code is ", number)
                    code=int(input("Enter your verification code: "))
                    if(code==number):
                     print("Your account is verified")
                     break
                    else:
                        print("Verification code is incorrect")
            if not found:
                print("Email not found.")    
             
         if(self.user_type.casefold()=="Student".casefold()):
            with open("files/Student.txt",'r') as f:
             found = False
             for line in f:
              stored_id,stored_password,stored_username,stored_type,stored_email = line.strip().split("\t")
              if stored_email==self.user_email:
                    found = True
                    number=random.randint(5000,100000)
                    print(" your verification code is ", number)
                    code=int(input("Enter your verification code: "))
                    if(code==number):
                     print("Your account is verified")
                     break
                    else:
                        print("Verification code is incorrect")
             if not found:
                print("Email not found.")           
        else:
            print("Type not found")  
                
    def CheckAccount(self):
        self.id=int(input("Enter user_id: "))
        self.days=int(input("Enter the no. of days u did not open your account: "))
        self.type=(input("Enter the user_type: "))
        if self.type.casefold()=="staff".casefold():
        
         with open("files/BookInfo.txt",'r')as f:
            found = False  
            for line in f:
                stored_id,stored_type,stored_borrowed,stored_reserved,stored_returned,stored_lost,stored_fine= line.strip().split("\t")
                if  stored_id == str(self.id) and stored_type.casefold()==self.type.casefold():
                    found = True
                    if self.days>=7:
                     self.status='Inactive'
                     print("Your account is Inactive")
                     with open("files/Account.txt",'a') as f:
                         f.write(str(self.id))
                         f.write("\t")
                         f.write(stored_type)
                         f.write("\t")
                         f.write(str(self.days))
                         f.write("\t")
                         f.write(self.status)
                         f.write("\n")
                    elif self.days == 0 and self.days<7:
                     self.status='Active'
                     print("Your account is Active")
                     with open("files/Account.txt",'a') as f:
                         f.write(str(self.id))
                         f.write("\t")
                         f.write(stored_type)
                         f.write("\t")
                         f.write(str(self.days))
                         f.write("\t")
                         f.write(self.status)
                         f.write("\n")
            if not found:
                print("User id or Type not found.")  
                
        pause()
        self.Menu()   
                
    def Get_Book_Info(self):
        with open ("files/BookInfo.txt",'r') as f:
            print("=============================================================")
            print(f"ID{"\t"}User-Type{"\t"}Borow{"\t"}Reserv{"\t"}Retrn{"\t"}Lost{"\t"}Fine")
            print("=============================================================")
            for line in f:
             stored_id,stored_type,stored_borrowed,stored_reserved,stored_returned,stored_lost,stored_fine=line.strip().split('\t')
             print(stored_id+"\t",stored_type+"\t",stored_borrowed+"\t",stored_reserved+"\t",stored_returned+"\t",stored_lost+"\t",stored_fine+"\n")
             print("------------------------------------------------------------") 
        pause()
        self.Menu()
    
    def Menu(self):
            print("    1.  To verify user")
            print("    2.  To Check Account Status")
            print("    3.  To get Book Info")
            print("    4.  Return to main")
            userchoice=int(input("Enter your choice: "))
            while True:
             match userchoice:
                case 1:
                    self.Verify()
                case 2:
                    self.CheckAccount()    
                case 3:
                    self.Get_Book_Info() 
                case 4:
                    lms=LMS()
                    lms.Main_Menu()
                case __:
                    print("Invalid choice")         

class Account:
    def Calculate_fine(self):
        self.fine_amount=0    
        self.id=int(input("Enter your id for calculating your fine: "))
        self.usertype=input("Enter usertype: ")
        self.found1=False
        if self.usertype.casefold()=="Librarian".casefold():
            self.found1=True
            with open("files/Librarian.txt",'r') as f:
                found = False
                for line in f:
                    stored_id,stored_password,stored_username,stored_type,stored_email = line.strip().split("\t")
                    if stored_id==self.id:
                        found=True
                        with open("files/BookInfo.txt",'a') as f:
                            borrowed_books=int(input("Enter the no. of borrowed books: "))
                            borrowed_bookdays=int(input("enter the no. of days u borrowed book: "))
                            reserved_books=int(input("Enter the no. of reserved books: "))
                            reserved_bookdays=int(input("enter the no. of days u reserved book: "))
                            returned_books=int(input("Enter the no. of returned books: "))
                            lost_books=int(input("Enter the no. of lost books: "))
                            f.write(str(self.id))
                            f.write('\t')
                            f.write(self.usertype)
                            f.write('\t')
                            f.write(str(borrowed_books))
                            f.write('\t')
                            f.write(str(reserved_books))
                            f.write('\t')
                            f.write(str(returned_books))
                            f.write('\t')
                            f.write(str(lost_books))
                            f.write('\t')
                            if(lost_books>0):
                                lost_books=lost_books*500
                            if borrowed_bookdays>3:
                                borrowed_bookdays=borrowed_bookdays*200*borrowed_books
                            if reserved_bookdays>3:
                                reserved_bookdays=reserved_bookdays*400*reserved_books
                            if lost_books>0 or borrowed_bookdays>3 or reserved_bookdays>7:
                                self.fine_amount=lost_books+borrowed_bookdays+reserved_bookdays
                                print("Your total fine is: ",self.fine_amount)
                                f.write(str(self.fine_amount))
                                f.write('\n')
                    else:
                        print("Use id not found")
        if not self.found1:
            print("Type not found")
            
        elif self.usertype.casefold()=="Student".casefold():
                found = False
                with open("files/Student.txt",'r') as f:
                    for line in f:  
                        stored_id,stored_password,stored_username,stored_type,stored_email = line.strip().split("\t")
                        if stored_id==self.id:
                            found=True  
                            with open("files/BookInfo.txt",'a') as f:  
                                borrowed_books=int(input("Enter the no. of borrowed books: "))
                                borrowed_bookdays=int(input("enter the no. of days u borrowed book: "))
                                reserved_books=int(input("Enter the no. of reserved books: "))
                                reserved_bookdays=int(input("enter the no. of days u reserved book: "))
                                returned_books=int(input("Enter the no. of returned books: "))
                                lost_books=int(input("Enter the no. of lost books: "))
                                f.write(str(self.id)+'\t',self.usertype+'\t',str(borrowed_books)+'\t',str(reserved_books)+'\t',str(returned_books)+'\t',str(lost_books)+'\n')
                                if(lost_books>0):
                                    lost_books=lost_books*500
                                if borrowed_bookdays>3:
                                    borrowed_bookdays=borrowed_bookdays*200*borrowed_books
                                if reserved_bookdays>3:
                                    reserved_bookdays=reserved_bookdays*400*reserved_books
                                if lost_books>0 or borrowed_bookdays>3 or reserved_bookdays>7:
                                   self.fine_amount=lost_books+borrowed_bookdays+reserved_bookdays
                                   print("Your total fine is: ",self.fine_amount)
                                   f.write(str(self.fine_amount))
                                   f.write('\n')
                            if not found:
                              print("Use id not found")
                    else:
                        print("Type not found")
            
        elif self.usertype.casefold()=="Staff".casefold():
            with open("files/Staff.txt",'r') as f:
                found = False
                for line in f:
                    stored_id,stored_password,stored_username,stored_type,stored_email = line.strip().split("\t")
                    if stored_id==self.id:
                        found=True
                        with open("files/BookInfo.txt",'a') as f:
                            borrowed_books=int(input("Enter the no. of borrowed books: "))
                            borrowed_bookdays=int(input("enter the no. of days u borrowed book: "))
                            reserved_books=int(input("Enter the no. of reserved books: "))
                            reserved_bookdays=int(input("enter the no. of days u reserved book: "))
                            returned_books=int(input("Enter the no. of returned books: "))
                            lost_books=int(input("Enter the no. of lost books: "))
                            f.write(str(self.id))
                            f.write('\t')
                            f.write(self.usertype)
                            f.write('\t')
                            f.write(str(borrowed_books))
                            f.write('\t')
                            f.write(str(reserved_books))
                            f.write('\t')
                            f.write(str(returned_books))
                            f.write('\t')
                            f.write(str(lost_books))
                            f.write('\t')
                            if(lost_books>0):
                                lost_books=lost_books*500
                            if borrowed_bookdays>3:
                                borrowed_bookdays=borrowed_bookdays*200*borrowed_books
                            if reserved_bookdays>3:
                                reserved_bookdays=reserved_bookdays*400*reserved_books
                            if lost_books>0 or borrowed_bookdays>3 or reserved_bookdays>7:
                                self.fine_amount=lost_books+borrowed_bookdays+reserved_bookdays
                                print("Your total fine is: ",self.fine_amount)
                                f.write(str(self.fine_amount))
                                f.write('\n')
                    else:
                        print("Use id not found")
            if not found:
                print("Type not found")
        else:
            print("Invallid user type")
        pause()
        self.Menu()

            
    def Menu(self):
         print("   1.   To calculate fine")
         print("   2.   Return to Main")
         accountchoice=int(input("Enter your choice: "))
         match accountchoice:
            case 1:
             self.Calculate_fine()
             
            case 2:
                lms=LMS()
                lms.Main_Menu()
            case __:
                print("Invalid choice")
            
class Librarian():
    
    def Verify_Librarian(self):
        self.email=input("Enter your email for verification: ")
        with open("files/Librarian.txt",'r') as f:
          for line in f:
            stored_id,stored_password,stored_username,stored_type,stored_email = line.strip().split("\t")
            if(stored_type.casefold()=="Librarian".casefold()):
                found = False
                if(self.email==stored_email):
                    found=True
                    number=random.randint(100006,456789)
                    print("Your verification code is: ",number)
                    verify=int(input("Enter your verification code: "))
                    if(number==verify):
                        print("You are verified")
                    else:
                        print("Invalid verification code")     
        if not found:
            print("Type not found.")
        pause()
        self.Menu()
          
     
    def Search_Librarian(self):
        self.id=input("Enter the librarian id u want to search: ")
        with open("files/Librarian.txt",'r') as f:
            for line in f:
                stored_id,stored_password,stored_name,stored_type,stored_email=line.strip().split("\t")
                if(self.id==stored_id):
                    print("Librarian with id {stored_id} found")
                else:
                    print("Librarian with id {stored_id} not found")
        
        pause()
        self.Menu()
                    
                
    def Menu(self):
            print("     1.  To Verify Librarian")
            print("     2.  To Search LIbrarian")
            print("     3.  Return to Main")
            librarianchoice=int(input("Enter your choice: "))
            match librarianchoice:
                case 1:
                    self.Verify_Librarian()
                case 2:
                    self.Search_Librarian()
                case 3:
                    lms=LMS()
                    lms.Main_Menu()
                case __:
                    print("Invalid choice")
            
class Book:
    def Duedate():
        pass
    
    def Reservation_status():
        pass
    
    def Feedback():
        pass
    
    def Book_request():
        pass
    
    def Renew_info():
        pass 
    
    def Menu(self):
        print("     1.  To Show Publication Date")
        print("     2.  Reservation Status      ")
        print("     3.  To Give Feedback        ")
        print("     4.  Book Request            ")
        print("     5.  Re-new Information      ")
        print("     6.  Return to Main          ")
        bookchoice=int(input("Enter your choice: "))
        match bookchoice:
            case 1:
                self.Duedate()
                
            case 2:
                self.Reservation_status()  
                
            case 3:
                self.Feedback()
                
            case 4:
                self.Book_request()
                
            case 5:
                self.Renew_info()
                
            case 6:
                lms=LMS()
                lms.Main_Menu()
                
            case __:
                print("Invalid choice")   
 
class Date:
    def __init__(self):
        self.dd =[]
        self.mm=[]
        self.yy=[]
           
class Librarydatabase:
    
    def __init__(self):
        self.d=Date()
        self.book_id=[]
        self.book_title=[]
        self.book_author=[]
        self.ISBN=[]
          
    def Add(self):
        self.id=int(input("Enter book id: "))
        self.book_id.append(self.id)
        self.title=input("Enter book title: ")
        self.book_title.append(self.title)
        self.author=input("Enter Book Author name: ")
        self.book_author.append(self.author)
        self.date=(input("Enter publication date dd-mm-yyyy"))
        self.stored_day,self.stored_month,self.stored_year=self.date.strip().split(" ")
        self.d.dd.append(self.stored_day)
        self.d.mm.append(self.stored_month)
        self.d.yy.append(self.stored_year)
        self.isbn=input("Enter ISBN code: ")
        self.ISBN.append(self.isbn)
        self.File_Handling()
       
    def File_Handling(self):
        for i in range(len(self.book_title)):
            with open("files/LibraryDatabase.txt",'a') as f:
                f.write(str(self.book_id[i]))
                f.write("\t")
                f.write(self.book_title[i])
                f.write("\t")
                f.write(self.book_author[i])
                f.write("\t")
                f.write(f"{self.d.dd[i]}-{self.d.mm[i]}-{self.d.yy[i]}")
                f.write("\t")
                f.write(self.ISBN[i])
                f.write("\n")
        
     
    
    def Delete(self):
        id=int(input("Enter book id u want to delete: "))
        for i in range(len(self.book_id)):
            if id==self.book_id:
             del self.book_id[i],self.book_title[i],self.book_author[i],self.public_date[i],self.ISBN[i]
             print(f"Book with id {self.book_id[i]} deleted successfully")
             
            else:
                print("Id not found")
        pause()
        self.Main()
         
    
    def Display(self):
        with open("files/Librarydatabase.txt",'r')as f:
            while True:
                self.line=f.readline()
                print(self.line)
                if not self.line:
                     pause()
                     self.Main()
                    
    
    def Update(self):
        pass
    
    
    def Search(self):
        self.id=int(input("Enter book id for which u want to search: "))
        for i in range(len(self.book_id)):
            if(len(self.book_id)) == 0 :
                print("No record found")
                pause()
                self.Main()
            if self.id==self.book_id[i]:
                print(f"Book with id {self.id} found")
                pause()
                self.Main()
            else:
                print(f"Book with id {self.id} not found")
                pause()
                self.Main()
    
    def Main(self):
        print("    1.  Add Book")
        print("    2.  Delete Book")
        print("    3.  Display Book List")
        print("    4.  Search Book")
        print("    5.  Update Book")
        print("    6.  Return back to Main")
        databasechoice=int(input("Enter your choice: "))
        if databasechoice==1:
            while True:
                self.Add()
                choice=int(input("Press 1 to add more records and 0 to stop: "))
                if choice == 0:
                    libdata=Librarydatabase()
                    self.Main()

                 
        elif databasechoice==2:
            self.Delete()
                
        elif databasechoice==3:
            self.Display()
                
        elif databasechoice==4:
            self.Search()
                
        elif databasechoice==5:
            self.Update()
                
        elif databasechoice==6:
            lms=LMS()
            lms.Main_Menu() 
            
print("        =====================================")
print("        =                                   =")
print("        =                                   =")
print("        =      LIBRARY MANAGEMENT SYSTEM    =")
print("        =                                   =")
print("        =                                   =")
print("        =====================================")
pause()
time.sleep(0.5)
ClearScreen()

lms= LMS()
print("        =====================================")
print("        =          1. Login                 =")
print("        =          2. Register              =")
print("        =          3. Logout                =")
print("        =====================================")
choice=int(input("Enter your choice: "))
ClearScreen()
match(choice):
    case 1:
        lms.Login()
    
    case 2:
        lms.Register()
        
    case 3:
        lms.Logout()
        
    case __:
        print("Invalid choice")
        
    



