import ttkbootstrap as tk
import mysql.connector as mysql
from tkinter import messagebox as msg
from PIL import ImageTk,Image


try:
    conn=mysql.connect(host='localhost',user='intel',password='1234',database='customer')
    query=conn.cursor()
    query.execute('select * from c_detail')
    sql1=query.fetchall()
    for x in sql1:
        print(x)
    

except Exception as e:
    print(e)


root=tk.Window('dairy','darkly')

root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

frm1=tk.Frame(root,relief='flat')
frm1.grid(row=0,column=0)

img=Image.open('img.png')
img=ImageTk.PhotoImage(img.resize((50,50),Image.ADAPTIVE))
imglbl=tk.Label(frm1,image=img)
imglbl.pack(pady=15)

lb1=tk.Label(frm1,text='username')
lb1.pack(anchor='w')
usr=tk.StringVar()
en1=tk.Entry(frm1,textvariable=usr)
en1.pack(anchor='center',pady=10)

root.geometry('400x400')
root.columnconfigure(0,weight=1)

lb2=tk.Label(frm1,text='password')
lb2.pack(anchor='w')
pwd=tk.StringVar()
en2=tk.Entry(frm1,textvariable=pwd,show='*')
en2.bind('<Return>',lambda e:auth(usr.get(),pwd.get()))
en2.pack(anchor='center',pady=10)


def auth(usr,pwd):
    if usr=='' or pwd=='':
        msg.showinfo('invalid','please enter the values in the text box')
    elif(usr==sql1[0][1]) and(pwd==sql1[0][4]):
        msg.showinfo('login',f'login successful {sql1[0][1]}')
    else:
        msg.showerror('failed',f'login failed to {sql1[0][1]}')

btn=tk.Button(frm1,text='login',command=lambda:auth(usr.get(),pwd.get()))
btn.pack(anchor='center',pady=10)

root.mainloop()