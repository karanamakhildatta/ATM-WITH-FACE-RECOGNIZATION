from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
import cv2
import face_recognition
from time import sleep

class ATM:
    def __init__(self,root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("ATM")

        self.primary_buttons()

        # =========================================
        self.accountnumber = StringVar()
        self.current = StringVar()
        self.ammount = StringVar()
        self.pin = StringVar()
        
        # =========================================

        # =========================================
        self.current.set("")
        # =========================================

    def bg(self):
        img = Image.open("images/frontend/bg.jpg").resize((800,600))
        photoImage = ImageTk.PhotoImage(img)
        label = Label(image=photoImage)
        label.image = photoImage
        label.place(x=0,y=0,width=800,height=600)
        label = Label(self.root,text="WELCOME TO OUR SECURED ATM",font=("times new roman",26,"bold"),bg="gold",fg="black",bd=4,relief=RIDGE)
        label.pack(fill=X)
    def primary_buttons(self):
        self.destroy_frame()
        self.bg()
        button = Button(self.root,text="With Card",font=("times new roman",20,"bold"),bg="#0AFD28",command=self.with_card_buttons)
        button.place(x=255,y=250)

        button1 = Button(self.root,text="Without Card",font=("times new roman",20,"bold"),bg="#0AFD28",command=self.withoutcard_command)
        button1.place(x=255,y=370)
    def destroy_frame(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()
    def with_card_buttons(self):
        self.destroy_frame()
        self.bg()
        button2 = Button(self.root,text="Own Card",font=("times new roman",20,"bold"),bg="#0AFD28",command=self.owncard_command)
        button2.place(x=255,y=250)

        button3 = Button(self.root,text="Others Card",font=("times new roman",20,"bold"),bg="#0AFD28",command=self.othercard_command)
        button3.place(x=255,y=370)

    def ATM_buttons(self):
        self.destroy_frame()
        self.bg()

        button1 = Button(self.root,text="1",font=("times new roman",20,"bold"),command=lambda:self.onclick("1"))
        button1.place(x=450,y=160)

        button2 = Button(self.root,text="2",font=("times new roman",20,"bold"),command=lambda:self.onclick("2"))
        button2.place(x=500,y=160)

        button3 = Button(self.root,text="3",font=("times new roman",20,"bold"),command=lambda:self.onclick("3"))
        button3.place(x=550,y=160)
        
        button4 = Button(self.root,text="4",font=("times new roman",20,"bold"),command=lambda:self.onclick("4"))
        button4.place(x=450,y=220)
        
        button5 = Button(self.root,text="5",font=("times new roman",20,"bold"),command=lambda:self.onclick("5"))
        button5.place(x=500,y=220)
        
        button6 = Button(self.root,text="6",font=("times new roman",20,"bold"),command=lambda:self.onclick("6"))
        button6.place(x=550,y=220)

        button7 = Button(self.root,text="7",font=("times new roman",20,"bold"),command=lambda:self.onclick("7"))
        button7.place(x=450,y=280)
        
        button9 = Button(self.root,text="8",font=("times new roman",20,"bold"),command=lambda:self.onclick("8"))
        button9.place(x=500,y=280)
        
        button9 = Button(self.root,text="9",font=("times new roman",20,"bold"),command=lambda:self.onclick("9"))
        button9.place(x=550,y=280)

        clear_button = Button(self.root,text="clear",font=("times new roman",16,"bold"),command=self.clear)
        clear_button.place(x=600,y=160,height=55,width=80)

        cancel_button = Button(self.root,text="cancel",font=("times new roman",16,"bold"),command=self.primary_buttons)
        cancel_button.place(x=600,y=220,width=80,height=55)

        button0 = Button(self.root,text="0",font=("times new roman",20,"bold"),command=lambda:self.onclick("0"))
        button0.place(x=600,y=280,height=55,width=80)

    def accountNumber(self):
        label = Label(self.root,text="PLEASE ENTER YOUR ACCOUNT NUMBER",font=("times new roman",16,"bold"))
        label.place(x=25,y=100)

        label2 = Label(self.root,text=f"ACCOUNT:{self.current.get()}",font=("times new roman",16,"bold"))
        label2.place(x=25,y=150)

        btn = Button(self.root,text="Submit",font=("times new roman",16,"bold"),command=self.AccountNumberSubmit)
        btn.place(x=650,y=550)


    def Ammount(self):
        label = Label(self.root,text="PLEASE ENTER YOUR AMMOUNT",font=("times new roman",16,"bold"))
        label.place(x=25,y=100)

        label2 = Label(self.root,text=f"AMMOUNT:{self.current.get()}",font=("times new roman",16,"bold"))
        label2.place(x=25,y=150)

        btn = Button(self.root,text="Submit",font=("times new roman",16,"bold"),command=self.ammountSubmit)
        btn.place(x=650,y=550)
    
    def PIN(self):
        label1 = Label(self.root,text="PLEASE ENTER YOUR PIN",font=("times new roman",16,"bold"))
        label1.place(x=25,y=100)

        btn = Button(self.root,text="Submit",font=("times new roman",16,"bold"),command=self.withcardsubmit)
        btn.place(x=650,y=550)

    def owncard_command(self):
        self.destroy_frame()
        self.bg()
        self.ATM_buttons()
        self.accountNumber()

    def othercard_command(self):
        self.root.destroy()
        self.screen = Tk()
        With_Other_Card(self.screen)
        self.screen.mainloop()

    def withoutcard_command(self):
        self.root.destroy()
        self.window = Tk()
        Withoutcard(self.window)

# ====================================== WITH CARD FUNCTIONS  ===================================================================

    def AccountNumberSubmit(self):
        self.accountnumber.set(self.current.get())
        self.current.set("")
        con = sqlite3.connect("./main.db")
        cursor = con.cursor()
        cursor.execute(f"select * from Users where s_no = {self.accountnumber.get()}")
        r = cursor.fetchone()
        print(r[6])

        key = cv2. waitKey(1)
        webcam = cv2.VideoCapture(0) 
        sleep(1)
        print('press S to save')
        print('press q to exit')
        while True:

            try:
                check, frame = webcam.read()
                cv2.imshow("Capturing", frame)
                key = cv2.waitKey(1)
                if key == ord('s'): 
                    cv2.imwrite(filename='saved_img.jpg', img=frame)
                    webcam.release()
                    print("Processing image...")
                    img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                    gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                    img_ = cv2.resize(gray,(28,28))
                    print("Image saved!")
                    
                    break
                
                elif key == ord('q'):
                    webcam.release()
                    cv2.destroyAllWindows()
                    break
                
            except(KeyboardInterrupt):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break

        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.XML')
        img = cv2.imread(r[6])
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        faces = face_cascade.detectMultiScale(rgb_img, 1.1, 4)
        img_encoding = face_recognition.face_encodings(rgb_img)[0]

        for (x, y , w ,h) in faces:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)      
        cv2.imshow('img', img)

        img1 = cv2.imread("D:/python programs/saved_img.jpg")
        rgb_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        face = face_cascade.detectMultiScale(rgb_img1, 1.1, 4)
        img_encoding1 = face_recognition.face_encodings(rgb_img1)[0]

        for (x, y , w ,h) in face:
                cv2.rectangle(img1, (x,y), (x+w, y+h), (255, 0 , 0), 3)      
        cv2.imshow('img1', img1)

        result = face_recognition.compare_faces([img_encoding], img_encoding1)
        print("Result: ", result)
        cv2.destroyAllWindows()
        if(result[0]):
            # self.destroy_frame()
            self.destroy_frame()
            self.bg()
            self.ATM_buttons()
            self.Ammount()
        else:
            messagebox.showerror("ATM","Your face is not recognized!")

    def ammountSubmit(self):
        self.ammount.set(self.current.get())
        self.current.set("")
        self.destroy_frame()
        self.bg()
        self.ATM_buttons()
        self.PIN()

       
    def withcardsubmit(self):
        self.pin.set(self.current.get())
        self.current.set("")
        db = sqlite3.connect("main.db")
        cursor = db.cursor()
        cursor.execute(f"select * from Users where s_no = {self.accountnumber.get()}")
        r = cursor.fetchone()
        
        if (int(self.ammount.get())<=(int(r[4])*0.2)):
            if (int(self.pin.get() )== int(r[5])):
                # print("Transaction Successful")
                avl = int(r[4]) - int(self.ammount.get())
                # db = sqlite3.connect("main.db")
                cursor = db.cursor()
                cursor.execute(f"UPDATE Users set Balance = '{avl}' where s_no = {self.accountnumber.get()} ")
                db.commit()
                db.close()
                self.destroy_frame()

                self.accountnumber.set("")
                self.ammount.set("")
                self.pin.set("")
                self.current.set("")
                self.destroy_frame()
                self.bg()
                self.ATM_buttons()
                self.accountNumber()
                messagebox.showinfo("ATM",f"Transaction success \n current bal is {avl}")
                self.destroy_frame()
                self.bg()
                self.primary_buttons()
            else:
                return messagebox.showerror("ATM",f"PIN doesn't match")                  
        else:
            return messagebox.showerror("ATM","Ammount is too high")
             
    def onclick(self,text):
        currentText = self.current.get()
        currentText = currentText+text
        self.current.set(currentText)
        m = self.root.winfo_children()[15]
        if "ACCOUNT" in m['text']:
            self.destroy_frame()
            self.bg()
            self.ATM_buttons()
            self.accountNumber()
        elif "AMMOUNT" in m['text']:
            self.destroy_frame()
            self.bg()
            self.ATM_buttons()
            self.Ammount()
        else:
            self.destroy_frame()
            self.bg()
            self.ATM_buttons()
            self.PIN()  
            print(self.current.get())


    def clear(self):
        self.accountnumber.set("")
        self.ammount.set("")
        self.pin.set("")
        self.current.set("")
        self.destroy_frame()
        self.bg()
        self.ATM_buttons()
        self.accountNumber()



# =========================================================================================================

class With_Other_Card:
    def __init__(self,root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("ATM")


        self.accountnumber = StringVar()
        self.pin = StringVar()
        self.HoldermobileNumber = StringVar()
        self.ammount = StringVar()
        self.current = StringVar()
        
        self.bg()
        self.ATM_buttons()
        self.accountNumber()
        
    def bg(self):
        img = Image.open("images/frontend/bg.jpg").resize((800,600))
        photoImage = ImageTk.PhotoImage(img)
        label = Label(image=photoImage)
        label.image = photoImage
        label.place(x=0,y=0,width=800,height=600)
        label = Label(self.root,text="WELCOME TO OUR SECURED ATM",font=("times new roman",26,"bold"),bg="gold",fg="black",bd=4,relief=RIDGE)
        label.pack(fill=X)

    
    def accountNumber(self):
        label = Label(self.root,text="PLEASE ENTER YOUR ACCOUNT NUMBER",font=("times new roman",16,"bold"))
        label.place(x=25,y=100)

        label2 = Label(self.root,text=f"ACCOUNT:{self.current.get()}",font=("times new roman",16,"bold"))
        label2.place(x=25,y=150)

        btn = Button(self.root,text="Submit",font=("times new roman",16,"bold"),command=self.accountNumberSubmit)
        btn.place(x=650,y=550)

    def accountNumberSubmit(self):
        self.accountnumber.set(self.current.get())
        self.current.set("")
        con = sqlite3.connect("./main.db")
        cursor = con.cursor()
        cursor.execute(f"select s_no from Users where s_no = {int(self.accountnumber.get())}")
        r = cursor.fetchone()
        try:
            len(r)>0
            self.mobilenumber()
        
        except:
            messagebox.showerror("ATM","Invalid Account Number")
            self.clear()

    def mobilenumber(self):
            self.destroy_frame()
            self.bg()
            self.ATM_buttons()
            label = Label(self.root,text="PLEASE ENTER CARD HOLDER'S MOBILE NUMBER",font=("times new roman",16,"bold"))
            label.place(x=25,y=100)
            print(self.current.get())
            label2 = Label(self.root,text=f"MOBILE:{self.current.get()}",font=("times new roman",16,"bold"))
            label2.place(x=25,y=150)

            btn = Button(self.root,text="Submit",font=("times new roman",16,"bold"),command=self.mobilenumbersubmit)
            btn.place(x=650,y=550)

    def mobilenumbersubmit(self):
        self.HoldermobileNumber.set(self.current.get())
        self.current.set("")
        con = sqlite3.connect("./main.db")
        cursor = con.cursor()
        cursor.execute(f"select s_no from Users where s_no = {int(self.accountnumber.get())} and mobile = {self.HoldermobileNumber.get()}")
        r = cursor.fetchone()
        try:
            len(r)>0
            self.PIN()
        except:
            messagebox.showerror("ATM","Account is Unavailable")
            self.destroy_frame()
            self.clear()

    def PIN(self):
        self.destroy_frame()
        self.bg()
        self.ATM_buttons()
        label = Label(self.root,text="PLEASE ENTER PIN",font=("times new roman",16,"bold"))
        label.place(x=25,y=100)

        btn = Button(self.root,text="Submit",font=("times new roman",16,"bold"),command=self.PINSubmit)
        btn.place(x=650,y=550)
    def PINSubmit(self):
        self.pin.set(self.current.get())
        self.current.set("")
        con = sqlite3.connect("./main.db")
        cursor = con.cursor()
        cursor.execute(f"select s_no from Users where s_no = {int(self.accountnumber.get())} and mobile = {self.HoldermobileNumber.get()} and pin = {self.pin.get()}")
        r = cursor.fetchone()
        try:
            len(r)>0
            self.Amount()
        except:
            messagebox.showerror("ATM","Invalid Credentials")
            self.clear()
    def Amount(self):
        self.destroy_frame()
        self.bg()
        self.ATM_buttons()
        label = Label(self.root,text="PLEASE ENTER AMMOUNT",font=("times new roman",16,"bold"))
        label.place(x=25,y=100)
        label2 = Label(self.root,text=f"AMMOUNT:{self.current.get()}",font=("times new roman",16,"bold"))
        label2.place(x=25,y=150)
        btn = Button(self.root,text="Submit",font=("times new roman",16,"bold"),command=self.AmountSubmit)
        btn.place(x=650,y=550)
    
    def AmountSubmit(self):
        self.ammount.set(self.current.get())
        con = sqlite3.connect("./main.db")
        cursor = con.cursor()
        cursor.execute(f"select * from Users where s_no = {int(self.accountnumber.get())} and mobile = {self.HoldermobileNumber.get()} and pin = {self.pin.get()}")
        r = cursor.fetchone()
        try:
            len(r)
            if int(self.ammount.get()) < (int(r[4])*0.5):
                key = cv2. waitKey(1)
                webcam = cv2.VideoCapture(0) 
                sleep(1)
                print('press S to save')
                print('press q to exit')
                while True:

                    try:
                        check, frame = webcam.read()
                        cv2.imshow("Capturing", frame)
                        key = cv2.waitKey(1)
                        if key == ord('s'): 
                            cv2.imwrite(filename='saved_img.jpg', img=frame)
                            webcam.release()
                            print("Processing image...")
                            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                            img_ = cv2.resize(gray,(28,28))
                            print("Image saved!")
                            webcam.release()
                            cv2.destroyAllWindows()
                            break
                        
                        elif key == ord('q'):
                            webcam.release()
                            cv2.destroyAllWindows()
                            return
                
                    except(KeyboardInterrupt):
                        print("Turning off camera.")
                        webcam.release()
                        print("Camera off.")
                        print("Program ended.")
                        cv2.destroyAllWindows()
                        return messagebox.showerror("ATM","Unable to Process")
                am = int(r[4])- int(self.ammount.get())
                cursor.execute(f"UPDATE Users set balance = '{am}' where s_no = {self.accountnumber.get()}")
                con.commit()
                con.close()
                messagebox.showinfo("ATM",f"Transaction Successfull \n Current Bal is {am}")
                self.front_place()
            else:
                messagebox.showerror("ATM","Invalid Amount")
                self.clear()

        except:
            messagebox.showerror("ATM","Unable to precess")
            self.clear()
    
    def ATM_buttons(self):
        self.destroy_frame()
        self.bg()

        button1 = Button(self.root,text="1",font=("times new roman",20,"bold"),command=lambda:self.onclick("1"))
        button1.place(x=450,y=160)

        button2 = Button(self.root,text="2",font=("times new roman",20,"bold"),command=lambda:self.onclick("2"))
        button2.place(x=500,y=160)

        button3 = Button(self.root,text="3",font=("times new roman",20,"bold"),command=lambda:self.onclick("3"))
        button3.place(x=550,y=160)
        
        button4 = Button(self.root,text="4",font=("times new roman",20,"bold"),command=lambda:self.onclick("4"))
        button4.place(x=450,y=220)
        
        button5 = Button(self.root,text="5",font=("times new roman",20,"bold"),command=lambda:self.onclick("5"))
        button5.place(x=500,y=220)
        
        button6 = Button(self.root,text="6",font=("times new roman",20,"bold"),command=lambda:self.onclick("6"))
        button6.place(x=550,y=220)

        button7 = Button(self.root,text="7",font=("times new roman",20,"bold"),command=lambda:self.onclick("7"))
        button7.place(x=450,y=280)
        
        button9 = Button(self.root,text="8",font=("times new roman",20,"bold"),command=lambda:self.onclick("8"))
        button9.place(x=500,y=280)
        
        button9 = Button(self.root,text="9",font=("times new roman",20,"bold"),command=lambda:self.onclick("9"))
        button9.place(x=550,y=280)

        clear_button = Button(self.root,text="clear",font=("times new roman",16,"bold"),command=self.clear)
        clear_button.place(x=600,y=160,height=55,width=80)

        cancel_button = Button(self.root,text="cancel",font=("times new roman",16,"bold"),command=self.front_place)
        cancel_button.place(x=600,y=220,width=80,height=55)

        button0 = Button(self.root,text="0",font=("times new roman",20,"bold"),command=lambda:self.onclick("0"))
        button0.place(x=600,y=280,height=55,width=80)
    def front_place(self):
        self.root.destroy()
        self.screen = Tk()
        ATM(self.screen)
    def clear(self):
        self.accountnumber.set("")
        self.ammount.set("")
        self.pin.set("")
        self.current.set("")
        self.HoldermobileNumber.set("")
        self.destroy_frame()
        self.bg()
        self.ATM_buttons()
        self.accountNumber()

    def onclick(self,text):
        currentText = self.current.get()
        currentText = currentText+text
        self.current.set(currentText)
        m = self.root.winfo_children()[15]
        if "ACCOUNT" in m['text']:
            self.destroy_frame()
            self.bg()
            self.ATM_buttons()
            self.accountNumber()
        elif "MOBILE" in m['text']:
            self.mobilenumber()

        elif "AMMOUNT" in m['text']:
            self.Amount()  
            print(self.current.get())
        else:
            self.destroy_frame()
            self.bg()
            self.ATM_buttons()
            self.PIN()  
            print(self.current.get())

    def destroy_frame(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()

class Withoutcard:
    def __init__(self,root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("ATM")


        self.accountnumber = StringVar()
        self.pin = StringVar()
        self.aadhaarnumber = StringVar()
        self.ammount = StringVar()
        self.current = StringVar()
    
        self.bg()
        self.ATM_buttons()
        self.accountNumber()

    def bg(self):
        img = Image.open("images/frontend/bg.jpg").resize((800,600))
        photoImage = ImageTk.PhotoImage(img)
        label = Label(image=photoImage)
        label.image = photoImage
        label.place(x=0,y=0,width=800,height=600)
        label = Label(self.root,text="WELCOME TO OUR SECURED ATM",font=("times new roman",26,"bold"),bg="gold",fg="black",bd=4,relief=RIDGE)
        label.pack(fill=X)

    
    def accountNumber(self):
        label = Label(self.root,text="PLEASE ENTER YOUR ACCOUNT NUMBER",font=("times new roman",16,"bold"))
        label.place(x=25,y=100)

        label2 = Label(self.root,text=f"ACCOUNT:{self.current.get()}",font=("times new roman",16,"bold"))
        label2.place(x=25,y=150)

        btn = Button(self.root,text="Submit",font=("times new roman",16,"bold"),command=self.accountNumberSubmit)
        btn.place(x=650,y=550)

    def accountNumberSubmit(self):
        self.accountnumber.set(self.current.get())
        self.current.set("")
        con = sqlite3.connect("./main.db")
        cursor = con.cursor()
        cursor.execute(f"select s_no from Users where s_no = {int(self.accountnumber.get())}")
        r = cursor.fetchone()
        try:
            len(r)>0
            self.Adharnumber()
        
        except:
            messagebox.showerror("ATM","Invalid Account Number")
            self.clear()

    def Adharnumber(self):
            self.destroy_frame()
            self.bg()
            self.ATM_buttons()
            label = Label(self.root,text="PLEASE ENTER AADHAAR NUMBER",font=("times new roman",16,"bold"))
            label.place(x=25,y=100)
            print(self.current.get())
            label2 = Label(self.root,text=f"AADHAAR:{self.current.get()}",font=("times new roman",16,"bold"))
            label2.place(x=25,y=150)

            btn = Button(self.root,text="Submit",font=("times new roman",16,"bold"),command=self.AdharNumberSubmit)
            btn.place(x=650,y=550)

    def AdharNumberSubmit(self):
        self.aadhaarnumber.set(self.current.get())
        self.current.set("")
        con = sqlite3.connect("./main.db")
        cursor = con.cursor()
        cursor.execute(f"select s_no from Users where s_no = {int(self.accountnumber.get())} and aadhaar = {self.aadhaarnumber.get()}")
        r = cursor.fetchone()
        try:
            len(r)>0
            self.PIN()
        except:
            messagebox.showerror("ATM","Account is Unavailable")
            self.destroy_frame()
            self.clear()

    def PIN(self):
        self.destroy_frame()
        self.bg()
        self.ATM_buttons()
        label = Label(self.root,text="PLEASE ENTER PIN",font=("times new roman",16,"bold"))
        label.place(x=25,y=100)

        btn = Button(self.root,text="Submit",font=("times new roman",16,"bold"),command=self.PINSubmit)
        btn.place(x=650,y=550)
    def PINSubmit(self):
        self.pin.set(self.current.get())
        self.current.set("")
        print(self.accountnumber.get())
        print(self.aadhaarnumber.get())
        print(self.pin.get())
        con = sqlite3.connect("./main.db")
        cursor = con.cursor()
        cursor.execute(f"select * from Users where s_no = {int(self.accountnumber.get())} and aadhaar = {self.aadhaarnumber.get()} and pin = {self.pin.get()}")
        r = cursor.fetchone()

        print(r)
        try:
            len(r)>0
            key = cv2. waitKey(1)
            webcam = cv2.VideoCapture(0)
            sleep(1)
            print('press S to save')
            print('press q to exit')
            while True:

                try:
                    check, frame = webcam.read()
                    cv2.imshow("Capturing", frame)
                    key = cv2.waitKey(1)
                    if key == ord('s'): 
                        cv2.imwrite(filename='saved_img.jpg', img=frame)
                        webcam.release()
                        print("Processing image...")
                        img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                        gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                        img_ = cv2.resize(gray,(28,28))
                        print("Image saved!")
                        
                        break
                    
                    elif key == ord('q'):
                        webcam.release()
                        cv2.destroyAllWindows()
                        break
                
                except(KeyboardInterrupt):
                    print("Turning off camera.")
                    webcam.release()
                    print("Camera off.")
                    print("Program ended.")
                    cv2.destroyAllWindows()
                    break

            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.XML')
            img = cv2.imread(r[6])
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            faces = face_cascade.detectMultiScale(rgb_img, 1.1, 4)
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            for (x, y , w ,h) in faces:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)      
            cv2.imshow('img', img)

            img1 = cv2.imread("D:/python programs/saved_img.jpg")
            rgb_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
            face = face_cascade.detectMultiScale(rgb_img1, 1.1, 4)
            img_encoding1 = face_recognition.face_encodings(rgb_img1)[0]

            for (x, y , w ,h) in face:
                    cv2.rectangle(img1, (x,y), (x+w, y+h), (255, 0 , 0), 3)      
            cv2.imshow('img1', img1)

            result = face_recognition.compare_faces([img_encoding], img_encoding1)
            cv2.destroyAllWindows()
            print("Result: ", result)
            if (result[0] == True):
                self.Amount()
            else:
                messagebox.showerror("ATM","Invalid User")
                self.clear()

        except:
            messagebox.showerror("ATM","Invalid Credentials")
            self.clear()
    def Amount(self):
        self.destroy_frame()
        self.bg()
        self.ATM_buttons()
        label = Label(self.root,text="PLEASE ENTER AMMOUNT",font=("times new roman",16,"bold"))
        label.place(x=25,y=100)
        label2 = Label(self.root,text=f"AMMOUNT:{self.current.get()}",font=("times new roman",16,"bold"))
        label2.place(x=25,y=150)
        btn = Button(self.root,text="Submit",font=("times new roman",16,"bold"),command=self.AmountSubmit)
        btn.place(x=650,y=550)
    
    def AmountSubmit(self):
        self.ammount.set(self.current.get())
        con = sqlite3.connect("./main.db")
        cursor = con.cursor()
        cursor.execute(f"select * from Users where s_no = {int(self.accountnumber.get())} and aadhaar = {self.aadhaarnumber.get()} and pin = {self.pin.get()}")
        r = cursor.fetchone()
        try:
            len(r)
            if int(self.ammount.get()) < (int(r[4])*0.2):
                am = int(r[4]) - int(self.ammount.get())
                cursor.execute(f"UPDATE Users set balance = '{am}' where s_no = {self.accountnumber.get()}")
                con.commit()
                con.close()
                messagebox.showinfo("ATM",f"Transaction Successful \n Available Balance {am}")
                self.clear()
            else:
                messagebox.showerror("ATM","Invalid Amount")
                self.clear()
        except:
            messagebox.showerror("ATM","Unable to precess")
            self.clear()
    
    def ATM_buttons(self):
        self.destroy_frame()
        self.bg()

        button1 = Button(self.root,text="1",font=("times new roman",20,"bold"),command=lambda:self.onclick("1"))
        button1.place(x=450,y=160)

        button2 = Button(self.root,text="2",font=("times new roman",20,"bold"),command=lambda:self.onclick("2"))
        button2.place(x=500,y=160)

        button3 = Button(self.root,text="3",font=("times new roman",20,"bold"),command=lambda:self.onclick("3"))
        button3.place(x=550,y=160)
        
        button4 = Button(self.root,text="4",font=("times new roman",20,"bold"),command=lambda:self.onclick("4"))
        button4.place(x=450,y=220)
        
        button5 = Button(self.root,text="5",font=("times new roman",20,"bold"),command=lambda:self.onclick("5"))
        button5.place(x=500,y=220)
        
        button6 = Button(self.root,text="6",font=("times new roman",20,"bold"),command=lambda:self.onclick("6"))
        button6.place(x=550,y=220)

        button7 = Button(self.root,text="7",font=("times new roman",20,"bold"),command=lambda:self.onclick("7"))
        button7.place(x=450,y=280)
        
        button9 = Button(self.root,text="8",font=("times new roman",20,"bold"),command=lambda:self.onclick("8"))
        button9.place(x=500,y=280)
        
        button9 = Button(self.root,text="9",font=("times new roman",20,"bold"),command=lambda:self.onclick("9"))
        button9.place(x=550,y=280)

        clear_button = Button(self.root,text="clear",font=("times new roman",16,"bold"),command=self.clear)
        clear_button.place(x=600,y=160,height=55,width=80)

        cancel_button = Button(self.root,text="cancel",font=("times new roman",16,"bold"),command=self.front_place)
        cancel_button.place(x=600,y=220,width=80,height=55)

        button0 = Button(self.root,text="0",font=("times new roman",20,"bold"),command=lambda:self.onclick("0"))
        button0.place(x=600,y=280,height=55,width=80)
    def front_place(self):
        self.root.destroy()
        self.screen = Tk()
        ATM(self.screen)
    def clear(self):
        self.accountnumber.set("")
        self.ammount.set("")
        self.pin.set("")
        self.current.set("")
        self.aadhaarnumber.set("")
        self.destroy_frame()
        self.bg()
        self.ATM_buttons()
        self.accountNumber()

    def onclick(self,text):
        currentText = self.current.get()
        currentText = currentText+text
        self.current.set(currentText)
        m = self.root.winfo_children()[15]
        if "ACCOUNT" in m['text']:
            self.destroy_frame()
            self.bg()
            self.ATM_buttons()
            self.accountNumber()
        elif "ADHAAR" in m['text']:
            self.Adharnumber()

        elif "AMMOUNT" in m['text']:
            self.Amount()  
            print(self.current.get())
        else:
            self.destroy_frame()
            self.bg()
            self.ATM_buttons()
            self.PIN()  
            print(self.current.get())

    def destroy_frame(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()


if __name__ == "__main__":
    
    root = Tk()
    ATM(root)
    root.resizable(False,False)
    root.mainloop()