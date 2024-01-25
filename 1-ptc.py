import ttkbootstrap as ttk
from tkinter import messagebox

root=ttk.Window('signup','darkly')
root.geometry('400x300')
label1=ttk.Label(root,anchor='e',text='Email : poornachandran24680@gmail.com',background='#f3f',compound='',)
label1.pack(side='top',fill='x')
label=ttk.Label(root,anchor='center',text='signup Form',font=('',30,'bold'),background='#33f')
label.pack(side='top',fill='x')

def msg(e):
    print("valuse passed",e)
    messagebox.showinfo('value','you are pressed enter')

entry=ttk.Entry(root,width=20)
entry.bind('<Return>',msg)
entry.pack()


month=ttk.StringVar()
cb=ttk.Combobox(root,textvariable=month)
cb.bind('<Return>',lambda x:print(month.get()))
cb.pack()
months=('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')
cb.config(values=months)

year=ttk.IntVar()
sb=ttk.Spinbox(root,from_=1990,to=2030,textvariable=year)
sb.pack()

value=ttk.DoubleVar()
value.set(10.5)
pb=ttk.Progressbar(root,orient='horizontal',length=250,maximum=25.0,mode='determinate',variable=value)
pb.pack()
pb.start()

scale=ttk.Scale(root,from_=0.0,to=25.0,length=350,orient='horizontal',variable=value)
scale.pack()

f1=ttk.Frame(root,relief='solid',width=200,height=100)
f1.pack()
f2=ttk.Frame(root,relief='solid',width=400,height=200)
f2.pack()

lf=ttk.Labelframe()

nb=ttk.Notebook(root,width=100)
nb.pack()
nb.add(f1,text='one',padding=(20,50))
nb.add(f2,text='two',padding=(40,100))

root.mainloop()