import time
from sql_connect import Database 
from kotak_connect import kotak

db=Database()
kotk=kotak()
global oid
oid=0
def start():
    global oid
    while True:
        db_order=db.get_fields() # order details from database 
        print(db_order['order_status'],db_order['order_id'],'db_order')
        if not (db_order['order_id'] and db_order['order_status']):
            stock_code=kotk.get_stock_code(db_order['exchange'],db_order['stock_name'])
            try:
                order_details = kotk.place_order(type=db_order['order_type'],instrument_token=stock_code,quantity=db_order['quantity']) # ,price=db_order['order_price']) # order details like order id , order status 

            except Exception as error:
                print("Error",error)
            db.update_orderstatus(db_order['id'],db_order['id'],oid)
            time.sleep(2)
            oid+=1
        else:
            print("No New Order")

start() 