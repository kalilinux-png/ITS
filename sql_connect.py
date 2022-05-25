import datetime as dt
import mysql.connector
from creds import *


class Database:
    def __init__(self) -> None:
        print("[INFO] Starting Connection With Database")
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database)
        self.mycursor = self.mydb.cursor(buffered=True)

    def get_fields(self):
        print("[INFO] Successfully Connected to Database")
        self.mycursor.execute(
            f"SELECT * from order_table ORDER BY id DESC LIMIT 1")
        for column in self.mycursor:
            # data=list(map(float,column[0:4]))
            # print(round(int(data[2]),-2))
            print(column)
            return {"id": column[0], "time": column[1], "exchange": column[2], "stock_name": column[3], "order_price": column[4], "order_status": column[5], "order_id": column[6], "quantity": column[7], "order_type": column[8]}

    def update_orderstatus(self, table_id, order_status, order_id):
        sql = f"UPDATE order_table  SET order_status='{order_status}',order_id={order_id} WHERE id={table_id};"
        print(sql)
        self.mycursor.execute(sql)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record inserted.")

    def custom_update(self, this, where):
        sql = f"UPDATE OrderTable SET {this} WHERE {where};"
        print(sql)
        self.mycursor.execute(sql)
        db.mydb.commit()
        print(db.mycursor.rowcount, "record inserted.")

    def custom_command(self, command):
        # self.mydb.commit()
        print(command)
        self.mycursor.execute(command)
        ans = self.mycursor.fetchone()
        print(self.mycursor.rowcount, "record inserted.")
        return ans

    def create_table(self):
        print("Setting Up Database  ...")
        db.custom_command('''CREATE TABLE `order_table` (
            `id` int NOT NULL AUTO_INCREMENT,
            `time` datetime DEFAULT CURRENT_TIMESTAMP,
            `exchange` varchar(45) DEFAULT NULL,
            `stock_name` varchar(45) DEFAULT NULL,
            `order_price` float,
            `order_status` varchar(455) DEFAULT NULL,
            `order_id` BIGINT,
            `quantity` BIGINT,
            `order_type` varchar(45) DEFAULT NULL,
            PRIMARY KEY (`id`)
            ) ; 
        ''')
        print("Order Table Created Successfully")


if __name__ == "__main__":
    db = Database()
    print(db.custom_command(" SELECT * from order_table ORDER BY id DESC LIMIT 1"))
