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


def send_long_order(data):

    """
    This function sends long orders to the exchange.
    :param data: python dict, with keys as the API parameters.
    :return: the response from the exchange.
    """
    Lkey = "HOOTz1ETAGRInP0jJZ"
    Lsec = "nedtaSftBjXfdEJaWfiDg2Zovp0Iy0U3ONwD"

    client = bybit.bybit(test=True, api_key=Lkey, api_secret=Lsec)

    print(' LONG RESULT ')

    # Open position
    order = client.Order.Order_new(
                    side='Buy',
                    symbol=data['symbol'],
                    order_type=data['type'],
                    qty=data['amount'],
                    price=None,
                    time_in_force="GoodTillCancel")

    print(order.result())


def send_short_order(data):
    """
    This function sends short orders to the exchange.
    :param data: python dict, with keys as the API parameters.
    :return: the response from the exchange.
    """
    Skey = "J3LPXXcKthvHKsVR5x"
    Ssec = "pcCMmVTZOcVNFiEplakxcRwAFeL3hB1lzHmx"

    client = bybit.bybit(test=True, api_key=Skey, api_secret=Ssec)

    print(' SHORT RESULT ')
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

    print(order.result())

def set_trailing(data):
    Lkey = "HOOTz1ETAGRInP0jJZ"
    Lsec = "nedtaSftBjXfdEJaWfiDg2Zovp0Iy0U3ONwD"

    client = bybit.bybit(test=True, api_key=Lkey, api_secret=Lsec)
    priceObject = client.Positions.Positions_myPosition(symbol=data['symbol']).result()
    price = priceObject[0]['result'][0]['data']['entry_price']
    print("PRICE CHECK", price )
    ts = str(0.03 * float(price))

    trailing = client.Positions.Positions_tradingStop(
                    symbol=data['symbol'], 
                    trailing_stop=ts)
    print(trailing.result())















