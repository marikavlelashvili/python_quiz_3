import requests
import sqlite3
import json


connection = sqlite3.connect("game_of_thrones_database.db")
cursor = connection.cursor()

creating_database = '''CREATE TABLE IF NOT EXISTS  GOMCHARACHTERS(id INTEGER PRIMARY KEY ,
                                                                 firstname VARCHAR(45),
                                                                 lastname VARCHAR(45),
                                                                 fullname VARCHAR(45),
                                                                 title VARCHAR(45),
                                                                 family VARCHAR(45),
                                                                 imagename VARCHAR(45),
                                                                 imageURL VARCHAR(100))
'''
cursor.execute(creating_database)
print("in this program you can create a random game of thrones plot")
ID = int(input("input id between 0 and 53:"))
read_data = cursor.execute("select * from GOMCHARACHTERS").fetchall()
for each in read_data:
    if ID == each[0]:
        print("this character is already in plot")
        print("input new id")
        ID = int(input("input id between 0 and 53:"))
        response = requests.get(f"https://thronesapi.com/api/v2/Characters/{ID}")
        data = json.loads(response.text)
        print("your random character is:")
        print(json.dumps(data, indent=6))
        break
    else:
        response = requests.get(f"https://thronesapi.com/api/v2/Characters/{ID}")
        data = json.loads(response.text)
        print("your random character is:")
        print(json.dumps(data, indent=6))
        break


inserting_data =''' insert into GOMCHARACHTERS(id,firstname,lastname,fullname,title,family,imagename,imageURL) 
                    values (?,?,?,?,?,?,?,?)'''
values = (data['id'], data['firstName'], data['lastName'], data['fullName'], data['title'], data['family'], data['image'], data['imageUrl'])
cursor.execute(inserting_data, values)
connection.commit()
print("information was inserted")

print("your random plot")
read_data = cursor.execute("select * from GOMCHARACHTERS").fetchall()
for each in read_data:
    print(each)

connection.close()



