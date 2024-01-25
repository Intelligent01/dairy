import tkinter as tk

root=tk.Tk()


gender=tk.StringVar()
e_male=tk.Radiobutton(root,text='male',value='male',variable=gender).pack()
e_female=tk.Radiobutton(root,text='female',value='female',variable=gender).pack()

root.mainloop()