import json

def readjson():
    with open('data.json',encoding='utf-8') as file:
        data = json.load(file)
        print(type(data))
        print(data)
        print(data[0]['point'])
    return data

def writejson(data):
    jsonobject = json.dumps(data, ensure_ascii=False,indent=4)
    with open('fruit.json','w',encoding='utf-8') as file:
        file.write(jsonobject)


data = {'111':['Banana',100,5],
        '222':['Durian',150,6],
        '333':['Apple',200,10],
        '444':['ภาษาไทย',300,20]}

writejson(data)