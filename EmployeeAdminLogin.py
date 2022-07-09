
from tkinter import *
from tkinter import messagebox
import sqlite3


def save_as():
                name=e2.get()
                DOB=e3.get()
                Age=e4.get()
                country=c.get()
                salary=e6.get()
                conn=sqlite3.connect('EmployeeMAnagementSystem.db')
                with conn:
                                cursor=conn.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS Employee  (Name TEXT,DOB TEXT,Age TEXT,Country TEXT,Salary TEXT)')
                cursor.execute('INSERT INTO Employee (Name,DOB,Age,Country,Salary) values(?,?,?,?,?)',(name,DOB,Age,country,salary,))
                conn.commit()

                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                c.set("Select country")
                e6.delete(0,END)

                
               










def user():
           
               global e2,e3,e4,e6,c
               screen1=Toplevel(root)
               screen1.title("Employee Management System")
               screen1.geometry("550x500")
               l1=Label(screen1,text="****Employee Management System****",font=("arial",25),bg="blue",fg="yellow")
               l1.pack()
               l2=Label(screen1,text="Employee Name",font=("gulim",18),bg="black",fg="yellow")
               l2.place(x=65,y=80)

               e2=Entry(screen1,width=30)
               e2.place(x=310,y=85)

               l3=Label(screen1,text="Date Of Birth",font=("gulim",18),bg="black",fg="yellow")
               l3.place(x=65,y=150)

               e3=Entry(screen1,width=30)
               e3.place(x=310,y=155)


               l4=Label(screen1,text="Age",font=("gulim",18),bg="black",fg="yellow")
               l4.place(x=65,y=220)


               e4=Entry(screen1,width=30)
               e4.place(x=310,y=225)

               l5=Label(screen1,text="Country",font=("gulim",18),bg="black",fg="yellow")
               l5.place(x=65,y=290)
               list1=['India','America','England','SouthAfrica','Japan','WestIndies']
               c=StringVar()

               droplist=OptionMenu(screen1,c,*list1)
               droplist.config(width=15)
               c.set("Select  country")
               droplist.place(x=310,y=295)


               l6=Label(screen1,text="Salary",font=("gulim",18),bg="black",fg="yellow")
               l6.place(x=65,y=360)


               e6=Entry(screen1,width=30)
               e6.place(x=310,y=365)


               button=Button(screen1,text="Submit",width=16,font=("arial",12),bg="blue",fg="yellow",command=save_as)
               button.place(x=200,y=425)



               



def user_valid():
                
        if entry2.get()=="San" or entry2.get()=="san" and entry3.get()=="rak@11":
                        user()
        else:
                        messagebox.showinfo("Error","Invalid User")
                      
                




root=Tk()
root.title("PythonCoder")
root.geometry("360x340")

label=Label(root,text="LogIn Page",font=("calibri",25),bg="red",fg="blue")
label.pack()

label2=Label(root,text="UserName",font=("arial",16),fg="Blue")
label2.place(x=50,y=80)

entry2=Entry(root,width=25)
entry2.place(x=190,y=80)



label3=Label(root,text="Password",font=("arial",16),fg="green")
label3.place(x=50,y=140)

entry3=Entry(root,width=25)
entry3.place(x=190,y=140)



button=Button(root,text="Login",font=("arial",15),command=user_valid)
button.place(x=220,y=190)






root.mainloop()




























                



