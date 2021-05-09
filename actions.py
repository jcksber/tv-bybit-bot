import bybit
import ast

readKey = "CRvv5XZDRs6oiZfmdh"
readSec = "mNjWGDZrrDLh0k4343eVWArdhsAwamHAZ7IF"
read_client = bybit.bybit(test=True, api_key=readKey, api_secret=readSec)

writeKey = "HOOTz1ETAGRInP0jJZ"
writeSec = "nedtaSftBjXfdEJaWfiDg2Zovp0Iy0U3ONwD"    
exec_client = bybit.bybit(test=True, api_key=writeKey, api_secret=writeSec)

posKey = "vgARhPB3Lx14hpp6lm"
posSec = "RzsigX6Wndc3ADb0gyKJ5fk37MwtYlI2JTJW"
pos_client = bybit.bybit(test=True, api_key=posKey, api_secret=posSec)


def parse_webhook(webhook_data):

    """
    This function takes the string from tradingview and turns it into a python dict.
    :param webhook_data: POST data from tradingview, as a string.
    :return: Dictionary version of string.
    """

    data = ast.literal_eval(webhook_data)
    return data


def calc_price(given_price):

    """
    Will use this function to calculate the price for limit orders.
    :return: calculated limit price
    """

    if given_price == None:
        price = given_price
    else:
        price = given_price
    return price


def send_long_order(data):

    """
    This function sends long orders to the exchange.
    :param data: python dict, with keys as the API parameters.
    :return: the response from the exchange.
    """
    print(' LONG RESULT ')

    # Open position
    order = exec_client.Order.Order_new(
                    side='Buy',
                    symbol=data['symbol'],
                    order_type=data['type'],
                    qty=data['amount'],
                    price=None,
                    time_in_force="GoodTillCancel")

    print(order.result()[0])


def set_trailing(data):
    priceObject = read_client.Positions.Positions_myPosition(symbol=data['symbol']).result()
    price = priceObject[0]['result'][0]['data']['entry_price']
    print("PRICE CHECK", price)
    ts = str(0.0215 * float(price))

    trailing = pos_client.Positions.Positions_tradingStop(
                    symbol=data['symbol'], 
                    trailing_stop=ts)
    print(trailing.result())



# def send_short_order(data):
#     """
#     This function sends short orders to the exchange.
#     :param data: python dict, with keys as the API parameters.
#     :return: the response from the exchange.
#     """
#     Skey = "J3LPXXcKthvHKsVR5x"
#     Ssec = "pcCMmVTZOcVNFiEplakxcRwAFeL3hB1lzHmx"

#     client = bybit.bybit(test=True, api_key=Skey, api_secret=Ssec)

#     print(' SHORT RESULT ')
#     if data['side'] == 'Sell':
#         order = client.Order.Order_new(
#                         side='Sell',
#                         symbol=data['symbol'],
#                         order_type=data['type'],
#                         qty=data['amount'],
#                         price=calc_price(data['price']),
#                         time_in_force="GoodTillCancel")
#     else:
#         order = client.Order.Order_new(
#                         reduce_only=True,
#                         side='Buy',
#                         symbol=data['symbol'],
#                         order_type=data['type'],
#                         qty=data['amount'],
#                         price=calc_price(data['price']),
#                         time_in_force="GoodTillCancel")
#     print(order.result())










