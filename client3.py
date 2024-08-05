################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price)/2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Update this function ------------- """
    if (price_b == 0):
        return
    else:
        return price_a/price_b


# Main
if __name__ == "__main__":
    # checks whether script is being run as a module OR the main program
    # Query the price once every N seconds.
    #__name__ is a special built-in variable which sets to __main__ when script is executed directly
    # when a script is imported as a module, the name is set to __name__
    # code will only run when script is run directly
    for _ in iter(range(N)):
        # creates iterator that iterates N times
        #(range(N) generates a sequence of numbers from 0 to N-1)
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
        # opens a URL and retrieves data from it
        #random.random is a placeholder for introducinf variability
        #json.loads parses the JSON data retrieved from the URL into a python dictionary or list

        """ ----------- Update to get the ratio --------------- """
        prices = {}
        # creates empty dictionary
        for quote in quotes:
            #iterates through each quote in the quote list and proceses it
            #getdatapoint(quote) extracts the data points of each quote
            stock, bid_price, ask_price, price = getDataPoint(quote)
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
            # formats extracted data into string
        print("Ratio %s" % getRatio(prices["ABC"], prices["DEF"]))
