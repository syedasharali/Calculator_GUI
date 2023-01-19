from tkinter import *
root=Tk()

root.title('Calculator')
root.geometry('400x400')
root.iconbitmap('calc.ico')
root.resizable(0,0)

entry=StringVar()

def n9():
    enter.insert(END,9)

def n8():
    enter.insert(END,8)
    
def n7():
    enter.insert(END,7)

def n6():
    enter.insert(END,6)
    
def n5():
    enter.insert(END,5)

def n4():
    enter.insert(END,4)
    
def n3():
    enter.insert(END,3)

def n2():
    enter.insert(END,2)
    
def n1():
    enter.insert(END,1)

def nplus():
    flag=True
    if entry.get()!='':
        for i in list('+x/'):
            if entry.get()[-1]==i:
                flag=False
        if flag==True:
            if entry.get()[-1]=='-':
                enter.delete(len(entry.get())-1,len(entry.get()))
            enter.insert(END,'+')
    
def nminus():
    if entry.get()!='':
        if entry.get()[-1]!='-':
            if entry.get()[-1]=='+':
                enter.delete(len(entry.get())-1,len(entry.get()))
            enter.insert(END,'-')
    else:
        enter.insert(END,'-')

def nx():
    if entry.get()!='':
        if entry.get()[-1] in list('+-x/'):
            enter.delete(len(entry.get())-1,len(entry.get()))
        enter.insert(END,'x')
    
def ndivide():
    if entry.get()!='':
        if entry.get()[-1] in list('+-x/'):
            enter.delete(len(entry.get())-1,len(entry.get()))
        enter.insert(END,'/')
        
def n0():
    if entry.get()!='0':
        enter.insert(END,0)
    
def ndot():
    if entry.get()=='.':
        pass
    elif entry.get()=='':
        enter.insert(END,'0.')
    elif entry.get()[-1]=='.':
        pass
    else:
        enter.insert(END,'.')

def nexp():
    if entry.get()!='':
        if entry.get()[-1] not in list('+-x/'):
            enter.insert(END,'e')
    
def nequal():
    entryget=entry.get()
    if 'x' in list(entryget):
        entryget=list(entry.get())
        (entryget)[entryget.index('x')]='*'
        entryget=''.join(entryget)
    res=eval(entryget)
    if res==int(res):
        res=int(res)
    enter.delete(0,END)
    enter.insert(0,res)

def clear():
    enter.delete(len(entry.get())-1,len(entry.get()))
    
def clear_all():
    enter.delete(0,END)
    


enter=Entry(root,textvariable=entry,bd=2,font='Helvetica 20')
enter.grid(columnspan=5,padx=5,pady=10,ipadx=35,ipady=18)

Button(root,text='7',font='Helvetica 20',command=n7).grid(row=1,column=0,ipadx=19,ipady=8,padx=4,pady=2)
Button(root,text='8',font='Helvetica 20',command=n8).grid(row=1,column=1,ipadx=19,ipady=8,pady=2)
Button(root,text='9',font='Helvetica 20',command=n9).grid(row=1,column=2,ipadx=19,ipady=8,padx=1.9,pady=2)
Button(root,text='/',font='Helvetica 20',command=ndivide).grid(row=1,column=3,ipadx=19,ipady=8,pady=2)
Button(root,text='C',font='Helvetica 20',command=clear_all).grid(row=1,column=4,ipadx=13,ipady=8,padx=1.9,pady=2)

Button(root,text='4',font='Helvetica 20',command=n4).grid(row=2,column=0,ipadx=19,ipady=8,padx=1.9,pady=2)
Button(root,text='5',font='Helvetica 20',command=n5).grid(row=2,column=1,ipadx=19,ipady=8,pady=2)
Button(root,text='6',font='Helvetica 20',command=n6).grid(row=2,column=2,ipadx=19,ipady=8,padx=1.9,pady=2)
Button(root,text='x',font='Helvetica 20',command=nx).grid(row=2,column=3,ipadx=19,ipady=8,pady=2)
Button(root,text='<-',font='Helvetica 20',command=clear).grid(row=2,column=4,ipadx=11,ipady=8,padx=1.9,pady=2)

Button(root,text='1',font='Helvetica 20',command=n1).grid(row=3,column=0,ipadx=19,ipady=8,padx=1.9,pady=2)
Button(root,text='2',font='Helvetica 20',command=n2).grid(row=3,column=1,ipadx=19,ipady=8,pady=2)
Button(root,text='3',font='Helvetica 20',command=n3).grid(row=3,column=2,ipadx=19,ipady=8,padx=1.9,pady=2)
Button(root,text='+',font='Helvetica 20',command=nplus).grid(rowspan=2,row=3,column=3,ipadx=17,ipady=46,pady=2)
Button(root,text='-',font='Helvetica 20',command=nminus).grid(row=3,column=4,ipadx=19,ipady=8,padx=1.9,pady=2)

Button(root,text='0',font='Helvetica 20',command=n0).grid(row=4,column=0,ipadx=19,ipady=8,padx=1.9,pady=2)
Button(root,text='.',font='Helvetica 20',command=ndot).grid(row=4,column=1,ipadx=21,ipady=8,pady=2)
Button(root,text='e',font='Helvetica 20',command=nexp).grid(row=4,column=2,ipadx=17,ipady=8,padx=1.9,pady=2)
Button(root,text='=',font='Helvetica 20',command=nequal).grid(row=4,column=4,ipadx=15.6,ipady=8,padx=1.9,pady=2)

root.mainloop()