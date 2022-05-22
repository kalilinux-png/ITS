from sql_connect import Database 
from kotak_connect import kotak

db=Database()
kotk=kotak()
def start():
    while True:
        db_order=db.get_fields() # order details from database 
        stock_code=kotk.get_stock_code(db_order['exchange'],db_order['stock_name'])
        order_details = kotk.place_order(type=db_order['order_type'],instrument_token=stock_code,quantity=db_order['quantity'],price=db_order['price']) # order details like order id , order status 
        
