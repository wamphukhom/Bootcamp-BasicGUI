from datetime import datetime

quantity = 10
price = 10

#บันทึกข้อมูล
def writetext(quantity,price):
    ddate = datetime.now()
    ddate = ddate.replace(year=ddate.year+543)# บวกเป็น พศ
    ddate = ddate.strftime('%Y-%m-%d %H:%M:%S')
    
    total = quantity*price
    filename = 'data.txt'
    with open(filename, 'a',encoding='utf-8') as file:
        file.write('\n'+' วัน: {} สั่งดุเรียนทั้งหมด {:,.2f} กิโลกรัม ราคากิโลกรัมล่ะ {:,.2f} บาท ราคารวมทั้งหมด: {:,.2f} บาท'.format(ddate,quantity,price,total))

#writetext(11,22)
#writetext(12,23)
#writetext(13,24)
#writetext(14,25)