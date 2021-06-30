import tkinter as tk
import datetime
now = datetime.datetime.now()
from tkinter import messagebox
password=tk.Tk()
password.geometry("1000x600+0+0")
file=open("Data.txt",'r')
user=file.read()
file.close()
print (user)



w=tk.Label(password, text="Change Password", fg="white", bg="black", font=("Helvetica", 25))
w.pack()

age=tk.Label(password, text="Please enter your age for security reasons:", fg="white", bg="black", font=("Helvetica", 15))
age.pack()

age1=tk.Entry(password)
age1.pack()
age1.insert(0,"Age")

def change():
    file=open(user+'2.txt','r')
    ageof=file.readlines()
    file.close()
    age2=age1.get()
    if age2==ageof[1]:
        thanks=tk.Label(password, text="Thank you for confirming your age.", fg="white", bg="black", font=("Helvetica", 15))
        thanks.pack()
        file=open(user+".txt",'w')
        n=tk.Label(password, text="Enter your name:", fg="white", bg="black", font=("Helvetica", 15))
        n.pack()
        name=tk.Entry(password)
        name.pack()
        name.insert(0,"Name")

        new=tk.Label(password, text="Enter new password:", fg="white", bg="black", font=("Helvetica", 15))
        new.pack()
        newpass=tk.Entry(password)
        newpass.pack()
        newpass.insert(0,"")

        def done():
            file=open(user+".txt",'w')
            newpass1=newpass.get()
            name1=name.get()

            file.write(newpass1)
            file.close()
            file=open(user+'2.txt','w')
            file.write(name1)
            file.write('\n')
            file.write(age2)

            done1=tk.Label(password, text="You have successfully changed your password!!", fg="white", bg="black", font=("Helvetica", 15))
            done1.pack()
            file.close()

            transcreate6="Account: You have Changed your account Password on "+now.strftime('%d-%B-%y')+" at "+now.strftime('%H:%M:%S %p')
            file.write('\n'+transcreate6)
            file.close()

        changebutt=tk.Button(password, text = 'CHANGE', command = done)
        changebutt.pack()
    else:
        if messagebox.showinfo("ERROR", "Incorrect AGE!!!"):
            print ("CLOSED!!!!!!")
        
cont=tk.Button(password, text = 'CONTINUE', command = change)
cont.pack()
       
password.mainloop()










            


        

