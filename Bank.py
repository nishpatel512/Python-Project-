import tkinter as tk
import subprocess  


root=tk.Tk()

tkimage = tk.PhotoImage(file="darsu.ppm")
myvar=tk.Label(root,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)

w = tk.Label(root, text="WELCOME", fg="white", bg="black", font=("Helvetica", 25))
w.place(x=620,y=100)

n= tk.Label(root, text="New here??",fg="white", bg="black", font=("Helvetica", 15))
n.place(x=640,y=400)


u = tk.Entry(root)
u.place(x=640,y=300)
u.insert(0,"Username")

p = tk.Entry(root, show="*", width=20)
p.place(x=640,y=320)

p.insert(0,"")


def login():
    pas=p.get()
    user=u.get()
    print (pas)
    print (user)
    f=open("Data.txt",'w')
    f.write(user)
    f.close()
    
    file=open(user+'.txt','r')
    passwrd=file.read()
    file.close()
    file=open(user+'2.txt','r')
    info=file.readlines()
    file.close()
    ch=0
    
    if pas==passwrd:
        subprocess.call('Login.py',shell=True)
    else:
        print ("Wrong Password!!!")
        
       
                        
def Signup():
        subprocess.call('Signup.py',shell=True) 


log = tk.Button(root, text = 'Sign Up', command = Signup)
log.place(x=683, y = 430)
root.geometry('1366x768+0+0')
log = tk.Button(root, text = 'Login', command = login)
log.place(y=350, x = 683)




root.mainloop()


