import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

ordinal=[]

def popup_bonus():
    win = tk.Toplevel()
    win.wm_title("Ordinal Features")
    win.geometry("300x200+800+10")
    win.resizable(False,False)
    Label1 = tk.Label(win)
    Label1.place(relx=0, rely=0.5, height=20, width=44
            , bordermode='ignore')
    Label1.configure(background="#d9d9d9")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#000000")
    Label1.configure(text='''Column Number''')
    Label1.pack()
  
    Entry1 = tk.Entry(win)
    Entry1.place(relx=44, rely=0.5, height=20, relwidth=0.450
            , bordermode='ignore')

    Entry1.configure(background="white")
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(font="TkFixedFont")
    Entry1.configure(foreground="#000000")
    Entry1.configure(insertbackground="black")
    Entry1.configure(width=10)
    Entry1.pack()
    
    
        
    Label2 = tk.Label(win)
    Label2.place(relx=0, rely=0.5, height=20, width=44
            , bordermode='ignore')
    Label2.configure(background="#d9d9d9")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(foreground="#000000")
    Label2.configure(text='''Enter Ordinal Features separated by comma''')
    Label2.pack()
    
  
    
    Entry2 = tk.Entry(win)
    Entry2.place(relx=44, rely=0.5, height=20, relwidth=0.450
            , bordermode='ignore')

    Entry2.configure(background="white")
    Entry2.configure(disabledforeground="#a3a3a3")
    Entry2.configure(font="TkFixedFont")
    Entry2.configure(foreground="#000000")
    Entry2.configure(insertbackground="black")
    Entry2.configure(width=100)
    Entry2.pack()
    
    
    def add_feature():
        num=int(Entry1.get())
        val=Entry2.get()
        Entry1.delete(0,'end')
        Entry2.delete(0,'end')
        ordinal.append(dict([[num,val]]))


    def ordinal_feature():
        add_feature()
        win.destroy()

    
    b= tk.Button(win)
    
    b.place(relx=0.506, rely=0.450, height=24, width=100
        , bordermode='ignore')
    b.configure(activebackground="#ececec")
    b.configure(activeforeground="#000000")
    b.configure(background="#d9d9d9")
    b.configure(disabledforeground="#a3a3a3")
    b.configure(foreground="#000000")
    b.configure(highlightbackground="#d9d9d9")
    b.configure(highlightcolor="black")
    b.configure(pady="0")
    b.configure(text='''Process Features''')
    b.configure(width=177)
    b.configure(command=ordinal_feature)
    
    b2=tk.Button(win)
    
    b2.place(relx=0.100, rely=0.450, height=24, width=100
        , bordermode='ignore')
    b2.configure(activebackground="#ececec")
    b2.configure(activeforeground="#000000")
    b2.configure(background="#d9d9d9")
    b2.configure(disabledforeground="#a3a3a3")
    b2.configure(foreground="#000000")
    b2.configure(highlightbackground="#d9d9d9")
    b2.configure(highlightcolor="black")
    b2.configure(pady="0")
    b2.configure(text='''ADD Another''')
    b2.configure(width=150)
    b2.configure(command=add_feature)
    
    
    
    