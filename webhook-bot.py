"""
Tradingview-webhooks-bot is a python bot that works with tradingview's webhook alerts!
This bot is not affiliated with tradingview and was created by @robswc

You can follow development on github at: github.com/robswc/tradingview-webhook-bot

I'll include as much documentation here and on the repo's wiki!  I
expect to update this as much as possible to add features as they become available!
Until then, if you run into any bugs let me know!
"""

from actions import send_short_order, send_long_order, parse_webhook
from auth import get_token
from flask import Flask, request, abort
import os
import hashlib

############### AUTH.PY #####################################################
"""
Planning to add more here eventually, for now will be used for handling keys.
"""

# Set this to something unique.
pin = '6969'


# Generate unique token from pin.  This adds a marginal amount of security.
def get_token():
    token = hashlib.sha224(pin.encode('utf-8'))
    return token.hexdigest()
#############################################################################


# Create Flask object called app.
app = Flask(__name__)


# Create root to easily let us know its on/working.
@app.route('/')
def root():
    return ""


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Parse the string data from tradingview into a python dict
        data = parse_webhook(request.get_data(as_text=True))
        # Check that the key is correct
        if get_token() == data['key']:
            print(' ---------- TradingView Alert Received!! ---------- ')
            if data['move'] == 'Long':
                send_long_order(data)
            else:
                send_short_order(data)
            return '', 200
        else:
            abort(403)
    else:
        abort(400)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

