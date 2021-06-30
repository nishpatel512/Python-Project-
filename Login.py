import tkinter as tk
import datetime
import subprocess
now = datetime.datetime.now()

login=tk.Tk()
login.geometry("1000x500+200+50")

file=open("Data.txt",'r')
user=file.read()
file.close()
print (user)
file=open(user+'2.txt','r')
info=file.readlines()
file.close()

file=open(user+"3.txt",'r')
info2=file.read()
file.close()
file=open(user+'3.txt','w')
file.write(now.strftime('%d-%B-%y'+'    '+'%H:%M:%S %p'))
file.close()


we=tk.Label(login,text="Welcome Back"+" "+info[0],fg="white",bg="black",font=("Helvetica",25))
we.pack()
file=open(user+'3.txt','r')
la=tk.Label(login,text="Last Loged in on:"+" "+info2,fg="white",bg="black",font=("Helvetica",15))
la.pack()
file.close()
q=tk.Label(login,text="What do you want to do?",fg="white",bg="black",font=("Helvetica",15))
q.pack()

def Balance():
    print("Balance")
    subprocess.call('Balance.py',shell=True)

def Transfer():
    print("Transfer")
    subprocess.call('Transfer.py',shell=True)
def Withdraw():
    print("Withdraw")
    subprocess.call('Withdrawl.py',shell=True)
def Add():
    print("ADD")
    subprocess.call('Add.py',shell=True)

def ChangePass():
    print("CHANGED")
    subprocess.call('ChangePass.py',shell=True)

def CheckTrans():
    print("CHECKED")
    subprocess.call('Check.py',shell=True)


def LOG():
    login.destroy()

ch1=tk.Button(login, text = 'Check your balance',command=Balance).place(x=460,y=160)
ch2=tk.Button(login, text = 'Transfer money',command=Transfer).place(x=470,y=200)
ch3=tk.Button(login, text = 'Withdraw money',command=Withdraw).place(x=465,y=240)
ch4=tk.Button(login, text = 'Add money',command=Add).place(x=480,y=280)
ch5=tk.Button(login, text = 'Change Password',command=ChangePass).place(x=465,y=320)
ch6=tk.Button(login, text = 'Check your Recent Transactions',command=CheckTrans).place(x=430,y=360)
ch7=tk.Button(login, text = 'Logout',command=LOG).place(x=500,y=400)

    
    

    






login.mainloop()
