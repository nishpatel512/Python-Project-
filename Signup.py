import tkinter as tk
import datetime
import sys
import os
now = datetime.datetime.now()

signup = tk.Tk()
signup.geometry("1000x500+200+50")
we=tk.Label(signup,text="WELCOME TO EXTREME BANKS!!",font=("Helvetica",25))
we.pack()

i=tk.Label(signup,text="What is your name?",font=("Helvetica",15))
i.place(x=0,y=50)
name=tk.Entry(signup)
name.place(x=0,y=80)
name.insert(0, "Name")


age=tk.Label(signup,text="What is your age?",font=("Helvetica",15))
age.place(x=0,y=110)
ageof=tk.Entry(signup)
ageof.place(x=0,y=140)
ageof.insert(0, "Age")


user=tk.Label(signup,text="Enter a username for this account:",font=("Helvetica",15))
user.place(x=0,y=170)
username=tk.Entry(signup)
username.place(x=0,y=200)
username.insert(0, "Username")


passw=tk.Label(signup,text="Enter a password for this account:",font=("Helvetica",15))
passw.place(x=0,y=230)
password=tk.Entry(signup)
password.place(x=0,y=260)
password.insert(0, "Password")


def create():
    pas=password.get()
    user=username.get()
    n=name.get()
    a=ageof.get()
    f=open(user+'1.txt','w')
    print (n)
    print (user)
    print (pas)
    file=open(user+'.txt','w')
    file.write(pas)
    file.close()
    file=open(user+'2.txt','w')
    file.write(n)
    file.write('\n')
    file.write(a)
    file.close()
    file=open('Users.txt','a')
    userinfo=n+' : '+user+'\n'
    file.write(userinfo)
    file.close()

    money=tk.Label(signup,text="How much money you want to add in your account:",font=("Helvetica",15))
    money.place(x=0,y=320)
    mon=tk.Entry(signup)
    mon.place(x=0,y=350)
    mon.insert(0, "")
    

    def money():
        x=mon.get()
        print (x)
        f.write(x)
        f.close()
        file=open(user+'t.txt','a')
        transcreate="Created Account on "+now.strftime('%d-%B-%y')+" at "+now.strftime('%H:%M:%S %p')
        transcreate2="Balance: You have credited "+str(x)+"$ in your account on "+now.strftime('%d-%B-%y')+" at "+now.strftime('%H:%M:%S %p')
        file.write(transcreate)
        file.write('\n'+transcreate2)
        file.close()
        finish1=tk.Label(signup,text="You have successfully created an account with our bank",font=("Helvetica",15))
        finish1.place(x=0,y=410)
        finish2=tk.Label(signup,text="For choosing our bank we have credited an amount of $250 in your account.",font=("Helvetica",15))
        finish2.place(x=0,y=440)
        finish3=tk.Label(signup,text="THANK YOU!!",font=("Helvetica",15))
        finish3.place(x=0,y=470)
        file=open(user+'1.txt','r')
        balmon=file.read()
        file.close()
        file=open(user+'1.txt','w')
        file.write(str(int(balmon)+250))
        file.close()
        file=open(user+'t.txt','a')
        transcreate3="Balance: A gift of  "+str(250)+"$  from X-Treme Bank has been credited to your account on "+now.strftime('%d-%B-%y')+" at "+now.strftime('%H:%M:%S %p')
        file.write('\n'+transcreate3+'\n')
        file.close()
        lastlogin=now.strftime('%d-%B-%y'+'    '+'%H:%M:%S %p')
        file=open(user+'3.txt','w')
        file.write(lastlogin)
        file.close()
            
            
    Add=tk.Button(signup, text = 'ADD', command = money)
    Add.place(x=0,y=380)
    

    
create=tk.Button(signup, text = 'Create', command = create)
create.place(x=50,y=290)

    

signup.mainloop()
