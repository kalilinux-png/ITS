
from ks_api_client import ks_api
import json,requests
from  creds import *

class kotak:
    def __init__(self,access_code=None):
        '''creates a new session from an old session_token'''
        ip = '127.0.0.1'
        self.client = ks_api.KSTradeApi(
            access_token, user_id, consumer_key, ip, app_id)
        self.client.login(pwd)
        if  access_code:
            self.client.session_2fa(access_code)
        else:
            self.login(self.client,consumer_key,access_token,app_id,user_id,pwd)

        print("Login Done Successfully !!")
        
        '''Login On Intialization'''


    
    
    def login(self,client,consumer_key,access_token,app_id,user_id,password):
        headers={'accept':'application/json','consumerKey':consumer_key,'ip':'127.0.0.1','appId':app_id,'Content-Type':'application/json','Authorization':"Bearer "+access_token}
        data=json.dumps({'userid':user_id,'password':password})
        response= requests.post("https://tradeapi.kotaksecurities.com/apim/session/1.0/session/login/userid",headers=headers,data=data).json()
        url = "https://tradeapi.kotaksecurities.com/apim/session/1.0/session/2FA/oneTimeToken"
        headers["oneTimeToken"] = response['Success']['oneTimeToken']
        client.one_time_token=headers['oneTimeToken']
        data = json.dumps({"userid":user_id})
        resp = requests.post(url, headers=headers, data=data).json()
        client.session_token=resp['success']['sessionToken']
        print("Logged In  Successfully")
        return client

    def get_stock_code(self,exchange:str,stock_name:str):
        "Returns Stock Code For an Exchange"
        # # # return requests.get(f"https://googleoauthentication.herokuapp.com/code/{exchange.lower()}/{stock_name.lower()}").json()


    def ltp(self, code):
        '''Returns Ltp in form of float'''
        return float(self.client.quote(code, 'LTP')['success'][0]['lastPrice'])

    def ask_bid(self, name):
        '''Returns ask bid in form of buy,buy_q,sell,sell_q'''

        data = self.client.quote(name, 'DEPTH')['success']['depth'][0]

        buy = data['buy'][0]

        sell = data['sell'][0]

        return float(buy['price']), float(buy['quantity']), float(sell['price']), float(sell['quantity'])

    def modify_order(self, order_id, price, quantity=1, disclosed_quantity=0, trigger_price=0, validity='GFD'):
        ''' This Function is Used In Modification Of A Order '''

  

        try:
            self.client.modify_order(
                str(order_id), price, quantity, disclosed_quantity, trigger_price, validity)
        except Exception as e:
            print(e)

    def place_order(self, type='None', instrument_token=None, quantity=1, price=0, trigger_price=0, validity='GFD',tag=''):

        type = type.upper()

        # change's are made from this refernce list(place_order('buy', code, price=buy_price, quantity=quantity,tag='')[
        #          'Success'].values())[0]

        order_details = list(self.client.place_order(order_type="N", instrument_token=instrument_token, transaction_type=type,
                                                    quantity=quantity, price=price, disclosed_quantity=0, trigger_price=trigger_price, validity=validity,tag=tag)['Success'].values())[0]

        return order_details

    def order_status(self, order_Id):
        ''' This Function Is Used To Get Order Status Like Pending Or Traded ['staus'] == TRAD OR OPN OR CAN ['statusMessage']==Open or Completely Traded Order'''

        return self.client.order_report(order_Id)['success'][-1]['status']
        
        
    def cancel_order(self,order_id):
        try:
            print(self.client.cancel_order(order_id))
        except Exception as e:
            print('ERROR === > ', e)

    def order_report(self,client,orderId:int):
        for order in client.order_report()['success']:
            if order['orderId']==orderId:
                print("order found")
                return order

if __name__=="__main__":
   k=kotak()
   code=k.get_stock_code('nSe','VeDL')
   print(type(code))
   k.client.quote(int(code))        