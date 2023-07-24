import mysql.connector as connector

class myDB: #made class
    def __init__(self):  #made contructor
        #made opject and used connect method to make a connection, then made requirements to connect
        self.con = connector.connect(host='localhost',
                                    database='registration',
                                    user='root',
                                    password='pakhi')

        query = '''create table if not exists 
                    user(userId int primary key, 
                    userName varchar(100),
                    phone varchar(12))'''
        #A cursor keeps track of the position in the result set, and allows you to perform multiple operations row by row.
        cur = self.con.cursor()
        cur.execute(query)
        # print("created")

    #insert
    #to insert we will make a method(func)
    def insert_user(self,userId,userName,phone):
        query = "insert into user(userId,userName,phone) values({},'{}','{}')".format(userId,userName,phone)
        # print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("saved")

    #fetch all
    def fetch_all(self):
        query="select * from user" 
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id : ", row[0])
            print("User Name : ", row[1])
            print("User Phone : ", row[2])
            print()

    #delete user
    def delete_user(self,userId):
        query = "delete from user where userId = {}".format(userId)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

    #update
    def update_user(self,userId,newName,newPhone):
        query = "update user set userName='{}', phone={} where userId='{}'".format(newName,newPhone,userId)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("updated")