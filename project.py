from tkinter import *
import random
import datetime
import tkinter.messagebox
import smtplib
import time;


root=Tk()
root.title("a")
root.configure(background='yellow')
root.geometry("1200x800")


topf=Frame(root,width=1200,height=150,bd=5,relief="raise")
topf.pack(side=TOP)
topf.configure(background="green")

leftf=Frame(root,width=600,height=650,bd=5,relief="raise")
leftf.pack(side=LEFT)

rightf=Frame(root,width=600,height=650,bd=5,relief="raise")
rightf.pack(side=RIGHT)

rightf1=Frame(rightf,width=600,height=450,bd=5,relief="raise")
rightf1.pack(side=TOP)

rightf2=Frame(rightf,width=600,height=200,bd=5,relief="raise")
rightf2.pack(side=BOTTOM)

breakf=Frame(leftf,width=600,height=450,bd=5,relief="raise")
breakf.pack(side=TOP)

breakf2=Frame(leftf,width=600,height=200,bd=5,relief="raise")
breakf2.pack(side=BOTTOM)



title=Label(topf,font=('arial',20,'bold'),text="Laundry Anna",bd=5)
title.grid(row=0,column=0)

email_wap=StringVar()
name_wap=StringVar()
phone_wap=StringVar()

nam=Label(topf,font=('arial',20,'bold'),text="Name",bd=7)
nam.grid(row=0,column=1,sticky="w")
name=Entry(topf,font=('arial',20,'bold'),width=9,bd=2,justify="left",textvariable=name_wap)
name.grid(row=0,column=2)

pho=Label(topf,font=('arial',20,'bold'),text="Phone num",bd=7)
pho.grid(row=0,column=3,sticky="w")
phone=Entry(topf,font=('arial',20,'bold'),bd=7,width=9,justify="left",textvariable=phone_wap)
phone.grid(row=0,column=4)

ema=Label(topf,font=('arial',20,'bold'),text="Email",bd=7)
ema.grid(row=0,column=5,sticky="w")
email=Entry(topf,font=('arial',20,'bold'),bd=7,width=15,justify="left",textvariable=email_wap)
email.grid(row=0,column=6)

type1=Label(breakf,font=('arial',10,'bold'),text="Weight(in kg)",bd=5)
type1.grid(row=1,column=1)

type2=Label(breakf,font=('arial',10,'bold'),text="no of garments",bd=5)
type2.grid(row=1,column=2)

#==================================================================

var1=IntVar()
var2=IntVar()
var3=IntVar()




a_wap=DoubleVar()
a_wap.set("0")
a_wap1=DoubleVar()
a_wap1.set("0")

w_wap=DoubleVar()
w_wap.set("0")
w1_wap=DoubleVar()
w1_wap.set("0")

p_wap=DoubleVar()
p_wap.set("0")
p1_wap=DoubleVar()
p1_wap.set("0")

tkg1_wap=StringVar()
tgm1_wap=StringVar()
tax1_wap=StringVar()
total1_wap=StringVar()



def buttonvalue():
    if(var1.get()==1):
        wap.configure(state=NORMAL)
        wap1.configure(state=NORMAL)
    elif var1.get()==0:
        wap.configure(state=DISABLED)
        a_wap.set("0")
        wap1.configure(state=DISABLED)
        a_wap1.set("0")
    if(var2.get()==1):
        w.configure(state=NORMAL)
        w1.configure(state=NORMAL)
    elif var1.get()==0:
        w.configure(state=DISABLED)
        w_wap.set("0")
        w1.configure(state=DISABLED)
        w1_wap.set("0")
    if(var3.get()==1):
        p.configure(state=NORMAL)
        p1.configure(state=NORMAL)
    elif var3.get()==0:
        p.configure(state=DISABLED)
        p_wap.set("0")
        p1.configure(state=DISABLED)
        p1_wap.set("0")

def TotalCost():
    a1=float(a_wap.get())
    a2=float(w_wap.get())
    a3=float(p_wap.get())
    a4=a_wap1.get()
    a5=w1_wap.get()
    a6=p1_wap.get()

    totalweight=a1+a2+a3
    totalitems=a4+a5+a6
    
    tkg1_wap.set(totalweight)
    tgm1_wap.set(totalitems)
    tax1_wap.set(0.10)
    totalcost=a1*59+a2*49+a3*10
    totalcost1=totalcost+0.10*totalcost
    total1_wap.set(totalcost1)
 





type1=Checkbutton(breakf,text="Wash and Press",variable=var1,onvalue=1,offvalue=0,font=('arial',40,'bold'),command=buttonvalue)
type1.grid(row=2,column=0,sticky="w")

wap=Entry(breakf,font=('arial',50,'bold'),bd=5,width=4,justify='left',textvariable=a_wap,state=DISABLED)
wap.grid(row=2,column=1)

wap1=Entry(breakf,font=('arial',50,'bold'),bd=5,width=4,justify='left',textvariable=a_wap1,state=DISABLED)
wap1.grid(row=2,column=2)


type2=Checkbutton(breakf,text="only wash",variable=var2,onvalue=1,offvalue=0,font=('arial',40,'bold'),command=buttonvalue)
type2.grid(row=3,column=0,sticky="w")

w=Entry(breakf,font=('arial',50,'bold'),bd=5,width=4,justify='left',textvariable=w_wap,state=DISABLED)
w.grid(row=3,column=1)

w1=Entry(breakf,font=('arial',50,'bold'),bd=5,width=4,justify='left',textvariable=w1_wap,state=DISABLED)
w1.grid(row=3,column=2)


type3=Checkbutton(breakf,text="only press",variable=var3,onvalue=1,offvalue=0,font=('arial',40,'bold'),command=buttonvalue)

type3.grid(row=4,column=0,sticky="w")

p=Entry(breakf,font=('arial',50,'bold'),bd=5,width=4,justify='left',textvariable=p_wap,state=DISABLED)
p.grid(row=4,column=1)

p1=Entry(breakf,font=('arial',50,'bold'),bd=5,width=4,justify='left',textvariable=p1_wap,state=DISABLED)
p1.grid(row=4,column=2)
#===========================================
def aExit():
    aExit=tkinter.messagebox.askyesno("Quit System","Do you want to quit")
    if aExit>0:
        root.destroy()
        return
def reset():
    
    fromaddr="laundryanna03@gmail.com"
    toaddr=email_wap.get()
    message="Laundry anna\n"+str(name_wap.get())+"\n"+"total garments= "+str(tgm1_wap.get())+"\ntotal cost= "+str(total1_wap.get())
    password="laundry@anna1"
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(fromaddr,password)
    server.sendmail(fromaddr,toaddr,message)
    server.quit()


    tkg1_wap.set("")
    tgm1_wap.set("")
    tax1_wap.set("")
    total1_wap.set("")

    var1.set("0")
    var2.set("0")
    var3.set("0")

    a_wap.set("0")
    a_wap1.set("0")
    w_wap.set("0")
    w1_wap.set("0")
    p_wap.set("0")
    p1_wap.set("0")

    wap.configure(state=DISABLED) 
    wap1.configure(state=DISABLED)
    w.configure(state=DISABLED)
    w1.configure(state=DISABLED)
    p.configure(state=DISABLED)
    p1.configure(state=DISABLED)

receipt_ref=StringVar()
DateofOrder=StringVar()   

DateofOrder.set(time.strftime("%d/%m/%Y"))


def eReceipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10000,400856)
    randomRef=str(x)
    receipt_ref.set("BILL "+randomRef)

    a1=float(a_wap.get())
    a2=float(w_wap.get())
    a3=float(p_wap.get())
    a4=a_wap1.get()
    a5=w1_wap.get()
    a6=p1_wap.get()

    totalweight=a1+a2+a3
    totalitems=a4+a5+a6

    tkg1_wap.set(totalweight)
    tgm1_wap.set(totalitems)
    tax1_wap.set(0.10)
    totalcost=a1*59+a2*49+a3*10
    totalcost1=totalcost+0.10*totalcost
    total1_wap.set(totalcost1)


    txtReceipt.insert(END,'Receipt ref.\t\t'+receipt_ref.get()+'\t'+DateofOrder.get()+"\n")
    txtReceipt.insert(END,'Name   '+name_wap.get()+"\n")
    txtReceipt.insert(END,'Phone no   '+phone_wap.get()+"\n")
    txtReceipt.insert(END,'Total clothes   '+tgm1_wap.get()+"\n")
    txtReceipt.insert(END,'Total weight   '+tkg1_wap.get()+"\n")
    txtReceipt.insert(END,'tax   '+tax1_wap.get()+"\n")
    txtReceipt.insert(END,'Total cost   '+total1_wap.get()+"\n")





Receipt=Label(rightf1,font=('arial',20,'bold'),text="Receipt",bd=7,anchor="w")    
Receipt.grid(row=0,column=0,sticky=W)
txtReceipt=Text(rightf1,width=50,height=20,bg="white",bd=8,font=('arial',12,'bold'))
txtReceipt.grid(row=1,column=0)






btnTotal=Button(rightf2,padx=130,pady=10,fg="black",font=('arial',10,'bold'),width=3,text="Total",command=TotalCost)
btnTotal.grid(row=0,column=0)

btnReceipt=Button(rightf2,padx=130,pady=10,fg="black",font=('arial',10,'bold'),width=3,text="Receipt",command=eReceipt)
btnReceipt.grid(row=1,column=0)

btnReset=Button(rightf2,padx=130,pady=10,fg="black",font=('arial',10,'bold'),width=3,text="Reset",command=reset)
btnReset.grid(row=2,column=0)

btnExit=Button(rightf2,padx=130,pady=10,fg="black",font=('arial',10,'bold'),width=3,text="Exit",command=aExit)
btnExit.grid(row=3,column=0)

#====================================================
tkg=Label(breakf2,font=('arial',20,'bold'),text="total weight(in kg)",bd=7)
tkg.grid(row=0,column=0,sticky="w")
tkg1=Entry(breakf2,font=('arial',20,'bold'),bd=7,width=8,justify="left",textvariable=tkg1_wap)
tkg1.grid(row=0,column=1,sticky="w")

tgm=Label(breakf2,font=('arial',20,'bold'),text="total garments",bd=7)
tgm.grid(row=1,column=0,sticky="w")
tgm1=Entry(breakf2,font=('arial',20,'bold'),bd=7,width=8,justify="left",textvariable=tgm1_wap)
tgm1.grid(row=1,column=1,sticky="w")


tax=Label(breakf2,font=('arial',20,'bold'),text="tax",bd=7)
tax.grid(row=0,column=2,sticky="w")
tax1=Entry(breakf2,font=('arial',20,'bold'),bd=7,width=8,justify="left",textvariable=tax1_wap)
tax1.grid(row=0,column=3,sticky="w")

total=Label(breakf2,font=('arial',20,'bold'),text="total price",bd=7)
total.grid(row=1,column=2,sticky="w")
total1=Entry(breakf2,font=('arial',20,'bold'),bd=7,width=8,justify="left",textvariable=total1_wap)
total1.grid(row=1,column=3,sticky="w")

tkg1_wap.set("")
tgm1_wap.set("")
tax1_wap.set("")
total1_wap.set("")

root.mainloop()







                                         
