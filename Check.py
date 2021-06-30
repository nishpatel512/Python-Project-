import tkinter as tk

check=tk.Tk()
check.geometry('1000x500+0+0')



we=tk.Label(check,text="Your Recent Transactions/Changes"+" ",fg="white",bg="black",font=("Helvetica",25))
we.pack()

file=open("Data.txt",'r')
user=file.read()
file.close()
print (user)



file=open(user+'t.txt','r')
wholetext=file.readlines()
file.close()

for i in wholetext:
    
    inf=tk.Label(check,text=i,fg="white",bg="black",font=("Helvetica",15))
    inf.pack()

check.mainloop()
