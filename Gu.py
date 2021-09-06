from tkinter import *
from tkinter import messagebox
import zipfile as zp
import os
import time

checker = 0
tst = 0

def ext(zipname , password):
    try:
        z = zp.ZipFile(zipname , 'r')
        ps = password.encode()
        z.extractall(pwd=ps)
        z.close
        print('[+] password is ==>> ' + password)
        global tst
        tst+=1
    except:
        pass


def mainF(zname , passname):
    while True:
        try:
            zp.ZipFile(zname)
        except:
            print('unknown file')
            time.sleep(3)
            break
        zfile = zname
        passfile = open(passname)
        c = 0
        for line in passfile.readlines():
            password = line.split()
            password=password[0]
            c+=1
            print('try : '+str(c)+'| trying password')
            btr = ext(zfile , password)
            global tst
            if tst == 1:
                result = Tk()
                result.title('result')
                lab = Label(result,text='password is >> '+password)
                lab.pack()
                btnr = Button(result,text='Ok',command=result.destroy)
                btnr.pack()
                result.mainloop()
                break
                



x = 180 
y = 20
root = Tk()
root.title('Zcracker')
root.geometry('200x200')
lb = Label(root,text="zip file address or name ")
lb.place(x=395,y=345)
lb.pack()
text1=Entry(root)
text1.place(x=390,y=340)
text1.pack()
lb2 = Label(root,text="password file")
lb2.place(x=385 , y=345)
lb2.pack()
text2=Entry(root)
text2.place(x=400 , y = 350)
text2.pack()

def check(text1=text1, text2=text2):
    global tst
    v1 = text1.get()
    v2 = text2.get()
    if tst==0:
        try:
            zp.ZipFile(v1)
            open(v2)
            print('informations are true')
            print('cracking....')
            mainF(v1 , v2)
        except:
            msg = messagebox.showwarning('error',message="Enter correct informations !! ")




btn3 = Button(root,text='check',command=check)
btn3.pack()
lb2 = Label(root,text='password file address')




root.mainloop()