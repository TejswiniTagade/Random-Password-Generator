from tkinter import *
import random
root=Tk()
root.geometry("300x200")
#created function for generating password
def password_generator(n):
    string1="abcedefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    s1=[]
    for i in range(0,n):
        charecter=random.choice(string1)
        s1.append(charecter)      
    return "".join(s1)

#created function to call the password_generator, take input from user and display the password 
def onclick():
    pas=password_generator(Num.get())
    passwrd.set(pas)
    
root.title("random password genrator")

Number=Label(root,text="enter length of password")
Number.grid(row=0,column=4)

Num=IntVar()

enter_number=Entry(root,textvariable=Num)
enter_number.grid(row=0,column=15)

#take input from onclick function
Button1=Button(root,text="click here",command=onclick)
Button1.grid(row=5,column=15)

passwrd=StringVar()

paaword=Label(root,text="password")
paaword.grid(row=6,column=4)

entry_password=Entry(root,textvariable=passwrd)
entry_password.grid(row=6,column=15)

root.mainloop()
