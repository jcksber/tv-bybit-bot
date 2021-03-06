import bybit
import ast


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


def send_order(data):

    """
    This function sends the order to the exchange.
    :param data: python dict, with keys as the API parameters.
    :return: the response from the exchange.
    """
    key = "cTiQyNqVmw2XOKJfg4"
    sec = "voULcJBEo9RhUxxuKOoGxl5g1p4pNUqnITL5"

    client = bybit.bybit(test=True, api_key=key, api_secret=sec)

    positions = client.Positions.Positions_myPosition(symbol=data['symbol'])
    # print(positions.result())

    # if an open order already exists, and this is a buy order,
    # do nothing

    if data['move'] == 'Short':
        if data['side'] == 'Sell':
            order = client.Order.Order_new(
                            side='Sell',
                            symbol=data['symbol'],
                            order_type=data['type'],
                            qty=data['amount'],
                            price=calc_price(data['price']),
                            time_in_force="GoodTillCancel")
        else:
            order = client.Order.Order_new(
                            reduce_only=True,
                            side='Buy',
                            symbol=data['symbol'],
                            order_type=data['type'],
                            qty=data['amount'],
                            price=calc_price(data['price']),
                            time_in_force="GoodTillCancel")
    else: # LONG
        if data['side'] == 'Buy':
            order = client.Order.Order_new(
                            side='Buy',
                            symbol=data['symbol'],
                            order_type=data['type'],
                            qty=data['amount'],
                            price=calc_price(data['price']),
                            time_in_force="GoodTillCancel")
        else:
            order = client.Order.Order_new(
                            reduce_only=True,
                            side='Sell',
                            symbol=data['symbol'],
                            order_type=data['type'],
                            qty=data['amount'],
                            price=calc_price(data['price']),
                            time_in_force="GoodTillCancel")





    print("ORDER RESULT")
    print(order.result())
