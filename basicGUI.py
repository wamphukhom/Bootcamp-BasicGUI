from cProfile import label
from email.mime import image
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
from turtle import stamp
import csv
import sqlite3
#######################

def fddate(thai=True):
    if thai == True:
        ddate = datetime.now()
        ddate = ddate.replace(year=ddate.year+543)# บวกเป็น พศ
        ddate = ddate.strftime('%Y-%m-%d %H:%M:%S')
    else:
        ddate = datetime.now()
        ddate = ddate.strftime('%Y-%m-%d %H:%M:%S')
    
    return ddate

#######################

def writetext(quantity,price):
    
    ddate = fddate()
    total = quantity*price
    filename = 'data.txt'
    with open(filename, 'a',encoding='utf-8') as file:
        file.write('\n'+' วัน: {} สั่งดุเรียนทั้งหมด {:,.2f} กิโลกรัม ราคากิโลกรัมล่ะ {:,.2f} บาท ราคารวมทั้งหมด: {:,.2f} บาท'.format(ddate,quantity,price,total))

#######################

def writecsv(data):
    # data =['timestamp','qty','price']
    with open('data.csv','a',newline='',encoding='utf-8') as file: #with when sucess just close() function auto!!!
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)
    print('success')

#######################

def readcsv():
    with open('data.csv', newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        # print(list(fr))
        data = list(fr)
    return data

#######################

def sumdata():
    # ฟังชั่นใช้สำหรับการรวมค่าที่ได้จาก csv
    result = readcsv()
    sumlist = []
    print(result)
    print(float(result[1][1]) * 10)
    for d in result:
        sumlist.append(float(d[1]))
    sumlist2_1 = [float(d[1]) for d in result]
    sumlist2_2 = sum([float(d[1]) for d in result])
    sumlist2_3 = sum([float(d[2]) for d in result])
    return (sumlist, sumlist2_1, sumlist2_2, sumlist2_3)

#######################

GUI = Tk()
GUI.geometry('500x800')
GUI.title('โปรแกรม FMC v.0.0.1')

file = PhotoImage(file='matamask.png')
IMG = Label(GUI,image=file)
IMG.pack()

L1 = Label(GUI, text='FMC Stock', font=('Angsana New',30,'bold'),fg='green')
L1.pack() # .plasc(x,y) , .grid(row=0,column=0)

L2 = Label(GUI, text='กรุณากรอกจำนวนทุเรียน/กิโล', font=('Angsana New',20,'bold'))
L2.pack() # .plasc(x,y) , .grid(row=0,column=0)

vvalue1 = StringVar() # var = '';
vvalue2 = StringVar() # var = '';

E1 = ttk.Entry(GUI,textvariable=vvalue1,font=('impact',30))
E1.pack(pady=20)

L3 = Label(GUI, text='ราคา/กิโล', font=('Angsana New',20,'bold'))
L3.pack() # .plasc(x,y) , .grid(row=0,column=0)

E2 = ttk.Entry(GUI,textvariable=vvalue2,font=('impact',30))
E2.pack(pady=20)

def calculate(event=None):#none ฟังชั่นไหนต้องการทั้งปุ่มกดและคีย์บอร์ดต้องใส่
    quantity = float(vvalue1.get())
    price = float(vvalue2.get())
    call = quantity * price
    ddate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # writetext(quantity,price)
    data = [fddate(), quantity, price]
    writecsv(data)

    title = 'ยอดที่ลูกค้าต้องจ่าย'
    messagebox.showinfo(title, 'ดุเรียน {:,.2f} กิโลกรัม ราคาทั้งหมด: {:,.2f} บาท'.format(quantity,call))

    vvalue1.set('')# clear text
    vvalue2.set('')
    E1.focus()
    
s = ttk.Style()
s.configure('my.TButton', font=('Angsana New', 20, 'bold'))
B1 = ttk.Button(GUI, text='คำนวณ',command=calculate, style='my.TButton')
B1.pack(ipadx=30, ipady=20, pady=10)

E2.bind('<Return>', calculate)#enter ช่องที่ 2

def SummaryData(event=None):
    # alert
    sm = sumdata()
    title2 = 'ยอดขายรายวัน'
    messagebox.showinfo(title2, 'จำนวนที่ขายได้ : {:,.2f} ลูก \n ยอดขาย : {:,.2f} บาท'.format(sm[2],sm[3]))

GUI.bind('<F1>',SummaryData)

B2 = ttk.Button(GUI, text='รายงาน',command=SummaryData, style='my.TButton')
B2.pack(ipadx=30, ipady=20, pady=10)

E1.focus()
GUI.mainloop()