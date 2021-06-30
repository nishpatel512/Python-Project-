import tkinter as tk
import datetime
now = datetime.datetime.now()
from tkinter import messagebox
transfer=tk.Tk()

transfer.geometry('500x800+200+50')

tr=tk.Label(transfer,text="Transfer Money",fg="white",bg="black",font=("Helvetica",25))
tr.pack()
file=open("Data.txt",'r')
user=file.read()
file.close()
print (user)

file=open(user+'1.txt','r')
bal=tk.Label(transfer,text="Your Account balance as of today is:",fg="white",bg="black",font=("Helvetica",15))
bal.place(x=80,y=80)
ba=tk.Label(transfer,text=file.read(),fg="white",bg="black",font=("Helvetica",15))
ba.place(x=230,y=130)
file.close()



def trans():
    def users1():
        file=open("Users.txt",'r')
        usersavail=file.readlines()
        s=len(usersavail)
        count=1
        print (s)
        for i in range(s):
            messagebox.showinfo("USERS",usersavail[i])


            
            '''us=Label(transfer,text="User"+str(count)+":-"+" "+usersavail[i],fg="white",bg="black",font=("Helvetica",10))
            us.pack()
            count+=1'''
    users=tk.Button(transfer, text = 'Check the available users',command=users1)
    users.place(x=180,y=280)
    tra=tk.Label(transfer,text="Enter the username of the recipient:",fg="white",bg="black",font=("Helvetica",10))
    tra.place(x=150,y=200)
    transto=tk.Entry(transfer)
    transto.place(x=200,y=240)
    transto.insert(0,"Username")
    
    tran=tk.Label(transfer,text="Enter the Amount of money you want to transfer:",fg="white",bg="black",font=("Helvetica",10))
    tran.place(x=110,y=320)
    transmoney=tk.Entry(transfer)
    transmoney.place(x=200,y=360)
    transmoney.insert(0,"")

    file=open(user+'1.txt','r')
    balmon=file.read()
    file.close()
    print (type(balmon))

    file=open("Users.txt",'r')
    listof=file.readlines()
    file.close()
    print (listof)
    def moneytransfer():
        
        done=tk.Label(transfer,text="Your Money has been Transfered Successfully!!!",fg="white",bg="black",font=("Helvetica",15))
        done.place(x=30,y=440)
        transto1=transto.get()
        print (transto1)
        transmoney1=transmoney.get()
        
        
        file=open(transto1+'1.txt','r')
        balmon1=file.read()
        file.close()
        if int(transmoney1)<=int(balmon):
            file=open(user+"1.txt",'w')
            sub=int(balmon)-int(transmoney1)
            print (sub)
            file.write(str(sub))
            file.close()
            file=open(transto1+'1.txt','w')
            add=int(balmon1)+int(transmoney1)
            print (add)
            file.write(str(add))
            file.close()
            
            transcreate7="Balance: An Amount of "+str(transmoney1)+"$ has been sent to an Account named "+transto1+" On"+now.strftime('%d-%B-%y')+" at "+now.strftime('%H:%M:%S %p')
            transcreate8="Balance: An Amount of "+str(transmoney1)+"$ has been sent from an Account named "+user+" On "+now.strftime('%d-%B-%y')+" at "+now.strftime('%H:%M:%S %p')

            file=open(user+'t.txt','a')
            file.write('\n'+transcreate7)
            file.close()
            file=open(transto1+'t.txt','a')
            file.write('\n'+transcreate8)
            file.close()
        else:
            tk.Label(transfer,text="Insuficient Funds to send, Check your Balance!!",fg="white",bg="black",font=("Helvetica",10)).pack()
    transfer1=tk.Button(transfer, text = 'TRANSFER',command=moneytransfer)
    transfer1.place(x=220,y=400)
        
        


proceed=tk.Button(transfer, text = 'PROCEED',command=trans)
proceed.place(x=210,y=170)
transfer.mainloop()
    
    
