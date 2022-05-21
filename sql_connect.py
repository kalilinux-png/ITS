import datetime as dt
import mysql.connector

class Database:

    def __init__(self) -> None:
        print("[INFO] Starting Connection With Database")
        self.mydb = mysql.connector.connect(
        host="mysql-76243-0.cloudclusters.net",
        user="leader",
        password="password",
        port=18905,
        database='test')
        self.mycursor = self.mydb.cursor(buffered=True)
        
    def get_fields(self,tablename):
        print("[INFO] Successfully Connected to Database")
        self.mycursor.execute(f"SELECT * FROM {tablename}")
        dataset=[] 
        for column in self.mycursor:
            # data=list(map(float,column[0:4]))
            # print(round(int(data[2]),-2))
            print(column)
            id,time,strike,stoploss,exit,status,order_id,order_type,stop_loss_order_id,orderstatus=column[0],column[1],round(float(column[2]),-2),float(column[3]),column[4],column[5],column[6],column[7],column[8],column[9]
            dataset.append({"id":id,"time":time,"stoploss":stoploss,"exit":exit,"status":status,"strike":strike,"order_type":order_type,"stop_loss_order_id":stop_loss_order_id,"order_id":order_id,"orderstatus":orderstatus})
        return dataset
    
    def update_orderstatus(self,tablename,id,orderstatus,token_no):
        sql=f"UPDATE {tablename} SET orderstatus='{orderstatus}',token_no={token_no} WHERE id={id};"
        print(sql)
        self.mycursor.execute(sql)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record inserted.")

    def custom_update(self,this,where):
        sql=f"UPDATE OrderTable SET {this} WHERE {where};"
        print(sql)
        self.mycursor.execute(sql)
        db.mydb.commit()
        print(db.mycursor.rowcount, "record inserted.")
    
    def custom_command(self,command):
        # self.mydb.commit()
        print(command)
        self.mycursor.execute(command)
        ans = self.mycursor.fetchone()
        print(self.mycursor.rowcount,"record inserted.")
        return ans
    
        

if __name__=="__main__":
    db=Database()
    # print(db.custom_command("SELECT *  from PE  WHERE order_id is NOT NULL AND stop_loss_order_id is NOT NULL;"))
    # db.custom_update(f"order_id=\"this\",order=1","id=1")
    # print(db.custom_command("SELECT * from OrderTable WHERE id=1;"))

    # print(db.get_fields("OrderTable"))
    # db.update_field(2,"fakeorderid")
    
    # # mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    # data=[
    # ("09015010","17820.65","17814.65","0","CE","Sell",100),
    # ("09015010","17820.65","17814.65","0","CE","Modify",200),
    # ("09015010","17820.65","17814.65","0","PE","Modify",300),
    # ("09015010","17820.65","12432.65","0","PE","Sell",400),
    # ("09015010","17820.65","17814.65","0","PE","Buy",200)
    # ]
    # for val in data:
    #     sql = f"INSERT INTO PE  (time,entry,stoploss,clrpos,status,order_type,candlecrossed) VALUES {val}"
    #     db.mycursor.execute(sql)

    #     db.mydb.commit()
    # print(sql)

    # # # # # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    # # # # # val = ("John", "Highway 21")
    # # # # mycursor.execute(sql)


    print(db.mycursor.rowcount, "record inserted.")