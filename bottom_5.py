

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 00:32:46 2023

@author: hp
"""

from tkinter import *
import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
import mysql.connector
def back():
    root.destroy()
    import report_t
root=Tk()
db=mysql.connector.connect(host="localhost",user="akshay", password="akshay")
cur=db.cursor()

def show():

    t1="""select doctor_id,  count(p_id) as x from hospital.appointment group by doctor_id having x<6 order by x ;"""
    cnt=cur.execute(t1)
    cnt=cur.fetchall()
    print(cnt)
    
    l1=Label(root,text="Total number of appointments per doctor:",font="Times 13 bold")
    l1.grid(row=5,column=1, padx=10, pady=5)
    l2=Label(root,text="Doctor Name",font="Times 13 bold")
    l2.grid(row=6,column=1, padx=10, pady=5)
    l3=Label(root,text="Appointments",font="Times 13 bold")
    l3.grid(row=6,column=2, padx=10, pady=5)
    c=1
    for i in cnt:
        print(i[0])
        t1="""select d_name from hospital.doctor where doctor_id= %s """
        t2=[i[0]]
        r=cur.execute(t1,t2)
        r=cur.fetchall()
        print(r)
        l2=Label(root,text=r[0][0],font="Times 13 bold")
        l2.grid(row=6+c,column=1, padx=10, pady=5)
        l3=Label(root,text=i[1],font="Times 13 bold")
        l3.grid(row=6+c,column=2, padx=10, pady=5)
        c+=1
        if c==6:
            break
    butequal=Button(root, padx=5, pady=5, bd=4,bg='white',command=back,text="Back",font=("Courier New",16,'bold')) 
    butequal.grid(row=4, column=2, padx=5, pady=5)    
        
    
    
    

root.title("Reports")
db=mysql.connector.connect(host="localhost",user="akshay", password="akshay")
cur=db.cursor() 
thelabel=Label(root,text="Doctors with less than 5 Appointments",font="Times 13 bold")
thelabel.grid(row=0,columnspan=2,sticky="ew", padx=10, pady=5)


try:
    butequal=Button(root, padx=5, pady=5, bd=4,bg='white',command=show,text="Show",font=("Courier New",16,'bold')) 
    butequal.grid(row=4, column=2, padx=5, pady=5)
except mysql.connector.Error as error:
    print("Input correct values")
root.mainloop()