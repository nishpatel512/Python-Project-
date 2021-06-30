import tkinter as tk


balance=tk.Tk()

balance.geometry("500x200+200+50")

file=open("Data.txt",'r')
user=file.read()
file.close()
print (user)
ac=tk.Label(balance,text="Account Balance",fg="white",bg="black",font=("Helvetica",25))
ac.pack()

file=open(user+'1.txt','r')
bal=tk.Label(balance,text="Your Account balance as of today is:",fg="white",bg="black",font=("Helvetica",15))
bal.pack()
ba=tk.Label(balance,text=file.read(),fg="white",bg="black",font=("Helvetica",15))
ba.pack()



balance.mainloop()
