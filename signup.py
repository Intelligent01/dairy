import tkinter as tk
from tkinter import messagebox

root=tk.Tk(className='weclome')
root.geometry('1100x600')
root.grid

f1=tk.Frame(root,bg='orange',pady=10)
f1.pack(fill='x')
f1.grid_columnconfigure((0),weight=3)
f1.grid_columnconfigure(1,weight=1)

title=tk.Label(f1,text='Customer Registry',font=('',24,'bold'),bg='orange')
title.grid(row=0,column=0,sticky='e',)

e_search=tk.Entry(f1,font=('',20),width=16,)
e_search.grid(row=0,column=1,sticky='e',padx=20,)

f2=tk.Frame(root,bg='blue',pady=10)
f2.pack(fill='x')
f2.grid_columnconfigure((0,1,2,3,4),weight=1)

l_no=tk.Label(f2,text='no',bg='blue')
l_no.grid(row=0,column=0,sticky='e',padx=10)
e_no=tk.Entry(f2,font=('',))
e_no.grid(row=0,column=1,sticky='w')

lf1=tk.LabelFrame(root,text='Personal Det                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       +ail')
l_date=tk.Label(f2,text='Date',bg='blue')
l_date.grid(row=0,column=2,sticky='e',padx=10)
e_date=tk.Entry(f2,)
e_date.focus()
e_date.grid(row=0,column=3,sticky='w')

e_name=tk.Entry()
e_village=tk.Entry()
e_phone=tk.Entry()
e_aadhar=tk.Entry()
gender=tk.StringVar()
e_male=tk.Radiobutton(f1,text='male',value='male',variable=gender)
e_female=tk.Radiobutton(f1,text='female',value='female',variable=gender)
e_bank=tk.Entry()
e_branch=tk.Entry()
e_accno=tk.Entry()
e_reaccno=tk.Entry()
e_ifsc=tk.Entry()






root.mainloop()