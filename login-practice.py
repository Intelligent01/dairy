import tkinter as tk
from tkinter import ttk,messagebox

# from PIL import Image, ImageTk

# def resize_image(image_path, new_width, new_height):
#     original_image = Image.open(image_path)
#     resized_image = original_image.resize((new_width, new_height))
#     return ImageTk.PhotoImage(resized_image)


root=tk.Tk()
img=tk.PhotoImage(file='img.png')
root.iconphoto(False,img)
root.config(background='#ff0')
root.title('dairy')

frame1=tk.Frame(root,background='#ff0')

username_=tk.StringVar()
label=ttk.Label(frame1,text='username',background='#ff0')
label.pack(fill='x')

text1=ttk.Entry(frame1,textvariable=username_,)
text1.pack(pady=10)

password_=tk.StringVar()
password=ttk.Label(frame1,text='password',background='#ff0')
password.pack(fill='x',expand=True,pady=10)

btn_mode=True

def eye():
    global btn_mode
    if btn_mode:
        btn.config(image=small_openi)
        text2.config(show='')
        btn_mode=False
    else:
        btn.config(image=small_closei)
        text2.config(show='*')
        btn_mode=True

open_eye=tk.PhotoImage(file='openi.png')
close_eye=tk.PhotoImage(file='closei.png')
small_openi=open_eye.subsample(3,3)
small_closei=close_eye.subsample(3,3)
btn=tk.Button(frame1,image=small_closei,command=eye,bg='#ff0',bd=-1,activebackground='#f00',activeforeground='#00f')
btn.place(x=110,y=45)


def user_in(e):
    text2.delete(0,'end')
    text2.config(show='*')

def user_out(e):
    name=username_.get()
    if name =='':
        text2.insert(0,'password')
        text2.config(show='')

text2=ttk.Entry(frame1,textvariable=password_)
text2.bind('<FocusIn>',user_in)
text2.bind('<FocusOut>',user_out)
text2.pack()

login_i=tk.StringVar()

def login():
    if username_.get() == password_.get():
        login_i.set('login success')
        print(username_.get(),password_.get(),login_i.get())
    else:
        login_i.set('login fail')
        print(username_.get(),password_.get(),login_i.get())

login=ttk.Button(frame1,text='login',command=login)
login.pack()
l1=ttk.Label(frame1,textvariable=login_i,background='#ff0')
l1.pack()
frame1.pack()
root.minsize(400,500)
root.mainloop()
