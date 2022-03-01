import csv

def writecsv(data):
    # data =['timestamp','qty','price']
    with open('data.csv','a',newline='',encoding='utf-8') as file: #with when sucess just close() function auto!!!
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)
    print('success')

# d= ['2011-05-11 10:15:10',50,5000]
# writecsv(d)

def readcsv():
    with open('data.csv', newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        # print(list(fr))
        data = list(fr)
    return data

def sumdata():
    # ฟังชั่นใช้สำหรับการรวมค่าที่ได้จาก csv
    result = readcsv()
    sumlist = []
    print(result)
    #print(float(result[1][1]) * 10)
    for d in result:
        sumlist.append(float(d[1]))
    sumlist2_1 = [float(d[1]) for d in result]
    sumlist2_2 = sum([float(d[1]) for d in result])
    sumlist2_3 = sum([float(d[2]) for d in result])
    return (sumlist, sumlist2_1, sumlist2_2, sumlist2_3)


result = sumdata()
print(result)