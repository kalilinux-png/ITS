import time
from sql_connect import Database 
from kotak_connect import kotak

db=Database()
kotk=kotak()
global oid
def start():
    while True:
        db_order=db.get_fields() # order details from database 
        print(db_order['order_status'],db_order['order_id'],'db_order')
        if not (db_order['order_id'] and db_order['order_status']):
            stock_code=kotk.get_stock_code(db_order['exchange'],db_order['stock_name'])
            try:
                order_details = kotk.place_order(type=db_order['order_type'],instrument_token=stock_code,quantity=db_order['quantity'] ,price=db_order['order_price']) # order details like order id , order status 
                print(order_details)
                message=order_details['message']
                orderId=order_details['orderId']
            except Exception as error:
                print("Error",error)
                message=error['fault']['message']
                orderId=0
            db.update_orderstatus(db_order['id'],message,orderId)
            time.sleep(2)
        else:
            print("No New Order")

start() 